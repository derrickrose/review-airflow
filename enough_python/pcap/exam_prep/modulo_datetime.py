############################################################################################### date
from datetime import date

# giving the current date
## local time
## 2025-10-07
print(date.today())

# creating date from iso
## iso 8601
f = date.fromisoformat("2026-12-25")
print("from iso format", f)
print(type(f))

# creating date from timestamp
## to check on timestamp, check the module time
## returns local date
print("here", date.fromtimestamp(1671145600))

# showing the date
d = date(2026, 12, 25)
print(d)
print(d.year)
print(d.month)
print(d.day)

# error while assigning directly to any of the attributes
# we cannot set directly the date <=> AttributeError: attribute 'year' of 'datetime.date' objects is not writable
# d.year = 2025

# replacing the date
d = date(2026, 10, 6)
print(d.year)
## it returns a new date
d = d.replace(year=2025)
print(d.year)

# to check the day of week
## 0 to 6
print(d.weekday())

# to check the day of week with isoformat
## 1 to 7
print(d.isoweekday())

# check day of year
print("yearday", d.timetuple().tm_yday)

# formateando fecha
print("formateando fecha", d.strftime("%Y-%m-%d"))

# parseando fecha
fecha = "2026-12-25"
print("parseando fecha", date.fromisoformat(fecha))

#############################################################################################         datetime

# creating datetime
## year, month, day are mandatory, the rest parameters are key argument so not mandatory
## have to import zoneinfo for the timezone
## fold is actually 1 if day saving time (summer), 0 if regular
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

dt = datetime(2025, 10, 6, 11, 25, 00, 000, tzinfo=ZoneInfo("Europe/Paris"), fold=0)
print(dt)
## minimum arguments 3
dt = datetime(2025, 10, 5)
print(dt)
## type is datetime.datetime
print(type(dt))

# error AttributeError while assigning directly
# dt.year = 2030

# modifying datetime
dt = datetime(2025, 10, 5)
dt = dt.replace(year=2030)
print(dt)
## creating a full datetime
## fold is actually ignored so both (even on ambiguous time are allowed)
dt = datetime(2025, 10, 26, 3, 0, 0, 0, tzinfo=ZoneInfo("Europe/Paris"), fold=1)
print(dt)
dt = datetime(2025, 10, 26, 3, 0, 0, 000, tzinfo=ZoneInfo("Europe/Paris"), fold=0)
print(dt)

# showing the attributes
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(type(dt.microsecond))
print(type(dt.tzinfo))
print(type(dt.fold))

# datetime.datetime().time()
print(dt.time())

# datetime.datetime().date()
print(dt.date())

# datetime.datetime.today()
## no acepta argumento
## regresa fecha de hoy con tiempo en tiempo local
print(datetime.today())

# datetime.datetime.now()
## por defecto regresa datetime en tiempo local
## pero acepta un timezone asi que puede regresar datetime en el timezone indicado
print("datetime.now() sin argumento", datetime.now())
print("datetime.now(Paris)", datetime.now(ZoneInfo("Europe/Paris")))
print("datetime.now(UTC", datetime.now(timezone.utc))

# obteniendo marca de tiempo
dt = datetime.now(ZoneInfo("Europe/Paris"))
print(dt.timestamp())  # 1759745312.373297

# obteniendo datetime desde marca de tiempo
## regresa localtime en caso que no viene el timezone
dt = datetime.fromtimestamp(1759745312.373297, )
print("datetime from timestamp without argument", dt)
## ModuleNotFoundError if the timezone does not exist
dt = datetime.fromtimestamp(1759745312.373297, tz=ZoneInfo("Europe/Paris"))
print("datetime from timestamp with argument", dt)

# formatando fecha y tiempo
dt = datetime(2025, 10, 6, 12, 0, 0, 0, tzinfo=ZoneInfo("Europe/Paris"), fold=0)
print(datetime.strftime(dt, "%Y-%m-%d %H:%M:%S"))

# parseando fecha
print(datetime.now(tz=ZoneInfo("Europe/Paris")))
## regresara algo como 2025-10-06 12:26:42.849110+02:00
dt = datetime.strptime("2025-10-06 12:26:42.849110+02:00", "%Y-%m-%d %H:%M:%S.%f%z")
## ValueError por si a caso el formateo no tiene mismo formato que la fecha
print(dt)
print(type(dt))

################################################################# operaciones con fecha y tiempo

# operacion con tiempo
dt = datetime(2025, 10, 6, 12, 0, 0, 0, tzinfo=ZoneInfo("Europe/Paris"), fold=0)
print(dt)
## type datetime.datetime
print(type(dt))
dt2 = datetime(2025, 10, 5, 12, 0, 0, 0, tzinfo=ZoneInfo("Europe/Paris"), fold=0)
print(dt2)
print(dt - dt2)
## type datetime.timedelta
print(type(dt - dt2))

# creando objeto timedelta
from datetime import timedelta

delta = timedelta()
print("delta", delta)
delta = timedelta(weeks=1, days=1, hours=12, minutes=30, seconds=00, microseconds=000000)
print("delta", delta)
print(delta.days)

# AttributeError on accessing on minutes
## since timedelta stores in only day, seconds and microseconds
## week is changed to days, hours, minutes into seconds , then microseconds
# print(delta.minutes)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)

# puede multiplicar delta o tambiem adicionarlo
delta = delta * 2
delta = delta + delta
print(delta)

# anexe
from datetime import datetime

d = datetime(2020, 11, 4, 14, 53, 0)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
## %y year without century
## %B full month e.g. November
## %p indicator de manana o tarde
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))

print("dia de la semana", d.strftime("%w"))
print("semana del ano", d.strftime("%W"))
print("dia del ano:", d.strftime("%j"))
## %a abbreviated weekday name e.g. Wen
print(d.strftime("%a"))
## %A full weekday name
print(d.strftime("%A"))
## % b abbreviated month e.g. Nov
print(d.strftime("%b"))
## %B full month e.g. November
print(d.strftime("%B"))
## %c local full date and time
print(d.strftime("%c"))
## %C century truncated e.g. 20th century 1900 -> 1999
print(d.strftime("%C"))
print("isoweek year last 2 digits", d.strftime("%g"))
print("isoweek year full", d.strftime("%G"))
