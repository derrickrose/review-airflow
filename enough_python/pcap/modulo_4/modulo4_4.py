# datetime

# obtener la fecha local y crear objetos del tipo fecha
from datetime import date

## metodo datetime.date.today() devuelve la fecha de hoy (tipo date)
today = date.today()
print("hoy: ", today)
print("ano ", today.year)
print("mes ", today.month)
print("dia ", today.day)
print(type(today))
print(type(today.year))  ## datetime.date son solo de lectura

## today.year = 2026 AttributeError: attribute 'year' of 'datetime.date' objects is not writable
print(today.year)
## para crear un objeto fecha
data = date(2026, 12, 25)
print(data)

# fecha a partir de marca de tiempo epoch
## epoch 1 janvier 1970
import datetime
import time

help(time.time)
timestamp = time.time()
print("timestamp", timestamp)
d = datetime.date.fromtimestamp(timestamp)
print("fecha", d)

# creacion de un objeto de fecha usando el formato ISO
## ISO 8601 YYYY-MM-DD
print(datetime.date.fromisoformat("2026-12-25"))  # datetime.date.fromisoformat() se ha introducido desde python 3.7

# metodo replace
## ya hemos visto que date.year = 1111 genera una excepcion AttributeError
## ahora para cambiar la fecha, puedes usar date.replace()
fecha = datetime.date.fromisoformat("2026-12-25")
print(fecha.year)
# fecha.year = 2027
print(fecha.year)
fecha = fecha.replace(year=2027)  # date.replace() regresa un nuevo objeto date
print(fecha.year)

# que dia de la semana es ???
hoy = datetime.date.fromisoformat("2025-10-01")
print(hoy.weekday())  # from 0 to 6 # 0 lunes
## ISO 85601 regresa lunes como 1
print(hoy.isoweekday())  # from 1 to 7 # 1 lunes

# creando objeto time, datetime.time()
## time(
# hour, 0 to 23
# minute, 0 to 59
# second, 0 to 59
# microsecond, 0 to 1_000_000
# tzinfo, debe ser un objeto de la subclase tzinfo o None (por defecto) zona horarias y fold  tiempo de pared
# fold) 0 o 1, por defecto es cero DST or standard Day Saving Time
from datetime import time
from zoneinfo import ZoneInfo

tiempo = time(hour=12, minute=30, second=00, microsecond=00000000, tzinfo=ZoneInfo("Europe/Paris"), fold=0)
print(tiempo)
print(tiempo.hour)
print(tiempo.minute)
print(tiempo.second)
print(tiempo.microsecond)

## tiempo.hour = 13 # same AttributeError on asigning directly, over way to update

# el metodo time
import time

print("time seconds")
time.sleep(0.1)
print("end of sleep")

# la function ctime() devuelve hora
print(time.time())
print(time.ctime(9799399332))  # Thu Oct  2 09:15:32 2025 devolviendo hora desde timestamp
print(time.ctime())  # devuelve la hora actual

# gmtime() y localtime()
## time.struct_time(
# tm_year
# , tm_mon,
# tm_mday,
# tm_hour,
# tm_min,
# tm_sec,
# tm_wday, dia de la semana de 0 hasta 6
# tm_yday, dia del ano, 1 a 366
# tm_isdst, is day saving time especifica si le aplica el horario de verano 1 o 0 no o -1 no se sabe
# tm_zone,   sona horaria (valor en forma abreviada)
# tm_gmtoff)  especifica el desplazamento al este del UTC (valor en segundos)
## la clase struct_time tambien permite el acceso a valores usando indices
## 0 regresa year mientras que 8 regresa tm_idst
## excepciones es que tm_zone y tm_gmtoff no permite el accesso con indices
## usa timestamp, time.time() devuelve timestamp
## gmtime devuelve en utc , tm_isdst es siempre cero con este
## localtime
print(time.gmtime(
    time.time()))  # time.struct_time(tm_year=2025, tm_mon=10, tm_mday=2, tm_hour=7, tm_min=49, tm_sec=1, tm_wday=3, tm_yday=275, tm_isdst=0)
print(time.localtime(time.time()))

# asctime() y mktime()
timestamp = time.time()
st = time.gmtime(timestamp)
print(time.asctime(st))  # convierte el objeto tupla en cadena
print(time.mktime(st))  # convierte el objeto tupla en timestamp epoch tupla de struct_time o tupla regula
print(time.localtime(252457200))
print(time.asctime(time.localtime(252457200)))

# objetos datetime
## en el modulo datetime, la fecha y la hora se pueden representar como objetos separados o como un solo objeto
## la clase que combina fecha y hora se llama datetime
## datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)
dt = datetime.datetime(2025, 1, 1, )
print(dt)
print(dt.date())
print(dt.time())

# metodos que devuelven la fecha y la hora actual
print("today")
print(datetime.datetime.today())
print(datetime.datetime.now())
# print(datetime.datetime.utcnow())  # deprecated

# obteniendo una marca de tiempo
## epoch
start = datetime.datetime.now()
print(datetime.datetime.timestamp(start))
print(start.timestamp())

# danto formato a la fecha y hora
formato = "%Y-%m-%d %H:%M:%S"
start = datetime.datetime.now()
print(start.strftime(formato))
formato = "%d-%B-%Y"
print(start.strftime(formato))  # 2025-10-03

# la funcion strftime() dentro del modulo datetime
## as method start.strftime(formato)
ti = time.gmtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", ti))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# el metodo parse time
## regresa un objeto time.struct_time con time.strptime()
d = time.strptime("2025-10-03 12:30:00", "%Y-%m-%d %H:%M:%S")
print(type(d))
## regresa un objeto datetime
## mucho mas usado ya que es mucho mas rico,
## tiene sumar directamente fechas ...
dt = datetime.datetime.strptime("2025-10-03 12:30:00", "%Y-%m-%d %H:%M:%S")
print(type(dt))

# operaciones con la fecha y hora
## utilizacion de timedelta
from datetime import date
from datetime import datetime
from datetime import timedelta

d = date(2025, 10, 3)
d2 = date(2024, 10, 3)
d3 = date(2024, 10, 3)
print("aqui")
print(d - d2)
print(type(d - d2))  ## el tipo es datetime.timedelta

d = datetime(2025, 10, 3, 12, 30, 00)
d2 = datetime(2024, 10, 3, 12, 30, 00)
## date, datetime iguales
print(d - d2)  # por ejemplo el resultado es 2 days, 0:00:00
print(type(d - d2))  #

# creando objeto timedelta
dlta = timedelta(days=1)
d0 = date(2025, 10, 2)
d1 = d0 + dlta
d2 = d0 - dlta
print(2 * dlta)
print(dlta / 2)
print(2 * dlta == dlta + dlta)
dlta = timedelta(weeks=1, days=0, hours=0, minutes=0, seconds=0,
                 microseconds=0)  # ejemplo completo de creacion de delta
print(dlta)
print(d0 + dlta)
print(datetime(2025, 10, 9, ))
## nota muy importante
## el objeto datetime.timedelta() solo almacena dias, segundos y microsegundos internamente
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Días:", delta.days)
## print(delta.weeks) # error por que no lo guarda como weeks pero se guarda en dias
## horas y minutos en segundos, milisegundos en microsegundos
print("Segundos:", delta.seconds)
print("Microsegundos:", delta.microseconds)
print(delta)
print(delta * 0.5)

from datetime import datetime

d = datetime(2020, 11, 4, 14, 53, 0)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))
print("dia de la semana", d.strftime("%w"))
print("semana del ano", d.strftime("%W"))
print("dia del ano:", d.strftime("%j"))
print(d.strftime("%a"))  # Wed as on wednesday
print(d.strftime("%A"))  # Wednesday
print(d.strftime("%b"))  # Nov
print(d.strftime("%B"))  # November
print(d.strftime("%c"))  # Wed Nov  4 14:53:00 2020
print(d.strftime("%C"))  # siecle ?
print(d.strftime("%g"))
