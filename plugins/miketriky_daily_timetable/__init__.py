from airflow.plugins_manager import AirflowPlugin

try:
    from .daily import DailyTimetable
except ImportError:
    from miketriky_daily_timetable.daily import DailyTimetable


class MiketrikyDailyTimetablePlugin(AirflowPlugin):
    name = "miketriky_daily_timetable"
    timetables = [DailyTimetable]

