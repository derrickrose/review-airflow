# modulo calendar
## la biblioteca estandar de python proporciona un modulo calendar
## Lunes           0                 calendar.MONDAY
## Martes          1                 calendar.TUESDAY
## Miercoles       2                 calendar.WEDNESDAY
## Jueves          3                 calendar.THURSDAY
## Viernes         4                 calendar.FRIDAY
## Sabado          5                 calendar.SATURDAY
## Domingo         6                 calendar.SUNDAY

# mostrar el calendario
## el resultado es igual que el comando cal en UNIX
import calendar

print(calendar.calendar(2025))
## tipo str
print(type(calendar.calendar(2025)))

# w: ancho por defecto 2
# l: linea por defecto 1
# c: numero de espacios entre las columnas del mes por defecto 6
# m: numero de columnas por linea por defecto 3

# otra opcion que no requiere print()
import calendar

## toma mismos argumentos que calendar
calendar.prcal(2025)

# calendario para un mes especifico
import calendar

# print(calendar.month(2025, 10))
print("here")
calendar.prmonth(2025, 10)

# funcion setfirstweekday()
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2025, 10)
print()
print("calendar.weekday", calendar.weekday(2025, 10, 1))

# la funcion weekheader()
## returns Sun for Sunday
print()
print("calendar.weekheader 3", calendar.weekheader(3))
## returns Su for Sunday
print("calendar.weekheader 2", calendar.weekheader(2))

# comprobar que un ano es bisiesto
## regresa un valor boleano
print(calendar.isleap(2025))
## nombre de leapday entra los 2 anos
## un rago exclusivo <=> no toma en cuenta el ultimo
print(calendar.leapdays(2020, 2024))

# clases para creacion de calendarios
calendar.Calendar(firstweekday=calendar.SUNDAY)  # proporciona métodos para preparar datos de calendario y dar formato
calendar.TextCalendar(firstweekday=calendar.SUNDAY)  # para crear calendarios de texto regulares
calendar.HTMLCalendar(firstweekday=calendar.SUNDAY)  # se utiliza para crear calendarios HTML
calendar.LocaleTextCalendar(
    firstweekday=calendar.SUNDAY)  # el constructor toma el param locale, se utiliza para devolver los nombres apropriados de los meses y dias de la semana
calendar.LocaleHTMLCalendar(
    firstweekday=calendar.SUNDAY)  # el constructor toma el parametro locale, que se usa para devolver nombres de meses y dias de la semana

# creando objeto Calendar
## toma un parametro opcional llamado firstweekday cual por defecto es igual a 0
## el parametro firstweekday debe ser un valor entero entre 0-6
## para este proposito, podemos usar las constantes ya conocidas
import calendar

c = calendar.Calendar(calendar.SUNDAY)
print("____________iter weekdays_____")
for weekday in c.iterweekdays():
    ## regresa entero
    print(weekday, end="+")
print()

# metodo itermonthdates()
## TypeError if missing argument year and month
## itera todo los dia del mes en tipo datetime.date, y tambien para formar una semana toma igual los dias del mes adelante
## podria tambien tomar los dias del mes siguiente
print("____________itermonthdates_____")
for d in c.itermonthdates(2025, 10):
    ## typo datetime.date
    print(d, end="*")

print("d outside the iteration", d)

# metodo itermonthdays()
## los 0 al principio igual representan los dias del mes pasado para formar una semana completa
## igual al final el cero representa el dia que para formar una semana de domingo a sabado pero que esta fuera del mes
## asi que el final del mes es viernes por la misma razon, se termina en sabado el cero y pues obvio
print("____________itermonthdays_____")
for e in c.itermonthdays(2025, 10):
    print(e)

# el metodo monthdays2calendar()
## documentacion del objeto calendar
## https://docs.python.org/3/library/calendar.html
## cada linea una semana en arreglo
## cada semana el arreglo, unas tuplas que lleva el dia del mes y el dia de la semana (entero)
print("____________monthdays2calendar_____")
# [(0, 6), (0, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# [(5, 6), (6, 0), (7, 1), (8, 2), (9, 3), (10, 4), (11, 5)]
# [(12, 6), (13, 0), (14, 1), (15, 2), (16, 3), (17, 4), (18, 5)]
# [(19, 6), (20, 0), (21, 1), (22, 2), (23, 3), (24, 4), (25, 5)]
# [(26, 6), (27, 0), (28, 1), (29, 2), (30, 3), (31, 4), (0, 5)]
for i in c.monthdays2calendar(2025, 10):
    print(i)

print()
print("______________________________")
calendar.prmonth(2025, 10, 2)
