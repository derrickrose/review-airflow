from __future__ import annotations

from datetime import timedelta
from typing import Any, Iterable, Mapping, Optional

import pendulum
from pendulum import Date, DateTime, Time, timezone as tz_factory
from pendulum.parsing.exceptions import ParserError

from airflow.timetables.base import DagRunInfo, DataInterval, TimeRestriction, Timetable

# Day name mapping for description
DAY_NAMES = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}

# Type aliases - all accept tuple, list, or set
# Days: 0=Mon, 6=Sun. Examples: {0,1,2,3,4} or [0,1,2,3,4] or (0,1,2,3,4)
DaysType = Iterable[int]

# Holidays: dates with optional names
# - set/list/tuple of dates: {"2026-01-01", "2026-12-25"} or ["2026-01-01"] or ("2026-01-01",)
# - dict of date -> name: {"2026-01-01": "New Year"}
# - list of dicts: [{"2026-01-01": "New Year"}]
HolidaysType = Iterable[str | Date | Mapping[str | Date, str]] | Mapping[str | Date, str]


def parse_date(date_input: str | Date) -> Date:
    """Parse a date from string (YYYY-MM-DD) or Date object."""
    if isinstance(date_input, Date):
        return date_input
    try:
        return pendulum.parse(date_input).date()
    except (ParserError, ValueError) as e:
        raise ValueError(f"Invalid date format: {date_input}") from e


def parse_holidays(holidays: HolidaysType) -> dict[Date, str]:
    """
    Parse holidays into a dict of Date -> description.

    Accepts:
    - Set of dates: {"2026-01-01", "2026-12-25"} -> dates with empty description (fastest)
    - Dict of date -> name: {"2026-01-01": "New Year", "2026-12-25": "Christmas"}
    - List/tuple of dates: ["2026-01-01", "2026-12-25"] -> dates with empty description
    - List of dicts: [{"2026-01-01": "New Year"}, {"2026-12-25": "Christmas"}]
    """
    if isinstance(holidays, Mapping):
        # Single dict: {"2026-01-01": "New Year", ...}
        result = {parse_date(k): v for k, v in holidays.items()}
        # Check for duplicates after parsing
        if len(result) != len(holidays):
            raise ValueError("Duplicate holidays detected after date parsing")
        return result

    result: dict[Date, str] = {}
    for item in holidays:
        if isinstance(item, Mapping):
            # Dict entry: {"2026-01-01": "New Year"}
            for k, v in item.items():
                parsed_date = parse_date(k)
                if parsed_date in result:
                    raise ValueError(f"Duplicate holiday date: {parsed_date}")
                result[parsed_date] = v
        else:
            # Plain date string or Date object
            parsed_date = parse_date(item)
            if parsed_date in result:
                raise ValueError(f"Duplicate holiday date: {parsed_date}")
            result[parsed_date] = ""
    return result


class DailyTimetable(Timetable):
    """
    A timetable that schedules DAG runs on specific days at a specific time.

    Supports:
    - Custom scheduling time (hour/minute)
    - Timezone-aware scheduling
    - Weekday filtering (e.g., Mon-Fri only)
    - Holiday exclusion with optional names
    - Run immediately on DAG start

    Example:
        # Run every weekday at 9:30 AM EST, skipping holidays
        timetable = DailyTimetable(
            hour=9,
            minute=30,
            timezone="America/New_York",
            days=[0, 1, 2, 3, 4],  # Mon-Fri
            holidays={"2026-01-01": "New Year", "2026-12-25": "Christmas"}
        )
    """

    # Maximum days to search for a valid day (prevents infinite loops)
    MAX_SEARCH_DAYS = 730  # 2 years

    def __init__(
        self,
        hour: int = 0,
        minute: int = 0,
        timezone: str = "UTC",
        run_immediately: bool = False,
        days: DaysType = frozenset({0, 1, 2, 3, 4}),  # Mon-Fri. Accepts set, list, tuple
        holidays: HolidaysType | None = None,  # Accepts set, list, tuple, or dict
    ):
        # Validate hour and minute
        if not (0 <= hour <= 23):
            raise ValueError(f"hour must be 0-23, got {hour}")
        if not (0 <= minute <= 59):
            raise ValueError(f"minute must be 0-59, got {minute}")

        # Validate days
        if not days:
            raise ValueError("days cannot be empty")
        # Check that all elements are integers
        non_integers = [d for d in days if not isinstance(d, int)]
        if non_integers:
            raise ValueError(f"days must contain only integers, got invalid types: {non_integers}")
        invalid_days = [d for d in days if d not in range(7)]
        if invalid_days:
            raise ValueError(f"days must be 0-6 (Mon-Sun), got invalid: {invalid_days}")

        self._hour = hour
        self._minute = minute
        self._timezone_name = timezone
        try:
            self._tz = tz_factory(timezone)
        except Exception as e:
            raise ValueError(f"Invalid timezone: {timezone}") from e
        self._run_immediately = run_immediately
        self._days = tuple(sorted(set(days)))  # Ensure sorted unique tuple
        # Parse and store holidays as a dict of Date -> name
        self._holidays: dict[Date, str] = parse_holidays(holidays) if holidays else {}

    @property
    def description(self) -> str:
        days_str = ", ".join(DAY_NAMES[d] for d in self._days)
        base = f"Daily at {self._hour:02d}:{self._minute:02d} ({self._timezone_name}) on [{days_str}]"
        if self._holidays:
            base += f" (skipping {len(self._holidays)} holidays)"
        return base

    @property
    def time(self) -> Time:
        return Time(self._hour, self._minute)

    @property
    def summary(self) -> str:
        """Get a concise summary of the timetable configuration."""
        days_str = ", ".join(DAY_NAMES[d] for d in self._days)
        time_str = f"{self._hour:02d}:{self._minute:02d}"
        parts = [f"{time_str} {self._timezone_name}", f"on {days_str}"]
        if self._holidays:
            parts.append(f"({len(self._holidays)} holidays)")
        if self._run_immediately:
            parts.append("[run_immediately=True]")
        return " ".join(parts)

    def serialize(self) -> dict[str, Any]:
        return {
            "hour": self._hour,
            "minute": self._minute,
            "timezone": self._timezone_name,
            "run_immediately": self._run_immediately,
            "days": list(self._days),
            "holidays": {d.to_date_string(): name for d, name in self._holidays.items()} if self._holidays else None,
        }

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> "DailyTimetable":
        # Handle both old format (list) and new format (dict)
        holidays_data = data.get("holidays")
        if holidays_data is not None:
            if isinstance(holidays_data, list):
                holidays_data = {h: "" for h in holidays_data}
        return cls(
            hour=data["hour"],
            minute=data["minute"],
            timezone=data["timezone"],
            run_immediately=data.get("run_immediately", False),
            days=set(data.get("days", {0, 1, 2, 3, 4})),
            holidays=holidays_data,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DailyTimetable):
            return NotImplemented
        return (
            self._hour, self._minute, self._timezone_name,
            self._run_immediately, self._days,
            frozenset(self._holidays.items())
        ) == (
            other._hour, other._minute, other._timezone_name,
            other._run_immediately, other._days,
            frozenset(other._holidays.items())
        )  # Convert to hashable type

    def __hash__(self) -> int:
        return hash((
            self._hour, self._minute, self._timezone_name,
            self._run_immediately, self._days,
            frozenset(self._holidays.items())
        ))  # Convert to hashable type

    def __repr__(self) -> str:
        holidays_repr = f"{len(self._holidays)} holidays" if self._holidays else "no holidays"
        return (
            f"DailyTimetable(hour={self._hour}, minute={self._minute}, "
            f"timezone={self._timezone_name!r}, run_immediately={self._run_immediately}, "
            f"days={list(self._days)}, {holidays_repr})"
        )

    def is_holiday(self, date: Date) -> bool:
        """Check if a date is a holiday."""
        return date in self._holidays

    def get_holiday_name(self, date: Date) -> str | None:
        """Get the holiday name for a date, or None if not a holiday."""
        return self._holidays.get(date) or None

    def create_datetime(self, date: Date) -> DateTime:
        """
        Create a timezone-aware datetime for the given date at the configured time.
        Pendulum handles DST transitions automatically.
        """
        return pendulum.datetime(date.year, date.month, date.day, self._hour, self._minute, tz=self._timezone_name)

    def find_previous_valid_day(self, from_date: Date) -> Date:
        """Find the most recent valid day on or before from_date (skipping holidays)."""
        current = from_date
        # Early return for common case: from_date is already valid
        if current.weekday() in self._days and not self.is_holiday(current):
            return current

        # Search up to MAX_SEARCH_DAYS back
        for _ in range(self.MAX_SEARCH_DAYS):
            current = current - timedelta(days=1)
            if current.weekday() in self._days and not self.is_holiday(current):
                return current
        raise ValueError(
            f"Could not find a valid day within {self.MAX_SEARCH_DAYS} days before {from_date}. "
            f"Check your days configuration {self._days} and holidays."
        )

    def find_next_valid_day(self, from_date: Date) -> Date:
        """Find the next valid day on or after from_date (skipping holidays)."""
        current = from_date
        # Early return for common case: from_date is already valid
        if current.weekday() in self._days and not self.is_holiday(current):
            return current

        # Search up to MAX_SEARCH_DAYS ahead
        for _ in range(self.MAX_SEARCH_DAYS):
            current = current + timedelta(days=1)
            if current.weekday() in self._days and not self.is_holiday(current):
                return current
        raise ValueError(
            f"Could not find a valid day within {self.MAX_SEARCH_DAYS} days after {from_date}. "
            f"Check your days configuration {self._days} and holidays."
        )

    def infer_data_interval(self, run_after: DateTime) -> DataInterval:
        # Find the previous valid day before run_after
        yesterday = (run_after - timedelta(days=1)).date()
        start_date = self.find_previous_valid_day(yesterday)
        start = self.create_datetime(start_date)
        return DataInterval(start=start, end=(start + timedelta(days=1)))

    def next_dagrun_info(
        self,
        *,
        last_automated_data_interval: Optional[DataInterval],
        restriction: TimeRestriction,
    ) -> Optional[DagRunInfo]:
        if last_automated_data_interval is not None:  # There was a previous run on the regular schedule.
            last_start = last_automated_data_interval.start
            # Find the next valid day after last_start
            next_date = self.find_next_valid_day((last_start + timedelta(days=1)).date())
            next_start = self.create_datetime(next_date)
        else:  # This is the first ever run on the regular schedule.
            next_start = restriction.earliest
            if next_start is None:  # No start_date. Don't schedule.
                return None

            # Get current time in the configured timezone
            now = DateTime.now(self._tz)
            today_at_configured_time = self.create_datetime(now.date())

            if not restriction.catchup:
                # If the DAG has catchup=False, today is the earliest to consider.
                next_start = max(next_start, today_at_configured_time)

                # Check if the configured time has already passed today
                if now > today_at_configured_time and not self._run_immediately:
                    # Time has passed and run_immediately=False, skip to next day
                    next_start = self.create_datetime(now.date() + timedelta(days=1))
            else:
                # With catchup enabled, align to the configured time (no run_immediately check for historical runs)
                next_start = self.create_datetime(next_start.date())

            # Find the next valid day
            next_date = self.find_next_valid_day(next_start.date())
            next_start = self.create_datetime(next_date)

        # DAG runs at start of interval (next_start), processing data until end
        end = next_start + timedelta(days=1)
        if restriction.latest is not None and next_start > restriction.latest:
            return None  # Over the DAG's scheduled end; don't schedule.
        return DagRunInfo(run_after=next_start, data_interval=DataInterval(start=next_start, end=end))
