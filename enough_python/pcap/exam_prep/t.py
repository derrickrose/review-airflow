from dataclasses import dataclass
from datetime import datetime, date, timedelta


class fecha():
    def __init__(self):
        __now = datetime.now()
        self.year = __now.year
        self.month = __now.month
        self.day = __now.day
        self.hour = __now.hour
        self.minute = __now.minute
        self.second = __now.second
        self.microsecond = __now.microsecond
        self.tzinfo = __now.tzinfo

f = fecha()
print(f.__dict__)


from zoneinfo import ZoneInfo
tz = ZoneInfo('Europe/Paris')
print(tz)
from datetime import timezone
print(timezone.utc)

import time
timestamp = time.time()
struct_time = time.gmtime(timestamp)
## year, month, day, hour, minute, second, weekday, yearday, isdaysavingtime
## time.struct_time(
# tm_year=2025,
# tm_mon=10,
# tm_mday=5,
# tm_hour=14,
# tm_min=30,
# tm_sec=2,
# tm_wday=6,
# tm_yday=278,
# tm_isdst=0,
# tm_zone,
# tm_gmtoff
# allow access via indices, except for tm_zone and tm_gmtoff)
print(struct_time)
print(struct_time.tm_zone)
print(struct_time.tm_gmtoff)

import platform
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.python_version().__class__)
print(platform.python_version_tuple().__class__)