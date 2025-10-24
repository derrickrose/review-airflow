# returning timestamp
## timestamp epoch seconds from 1st january 1970 in gmt (UTC) time
## 10 to 13 digits
import time

timestamp = time.time()
print(timestamp)
## let's say the reasult is 1759674602
timestamp = 1759674602

# creating time.struct_time gmt
## will give current gmt time (UTC) coordinated universal time
time.sleep(2)
struct_time = time.gmtime()
print(struct_time)
## with an argument timestamp it will give the timestamp's struct_time
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

# creating time.struct_time local
print("local struct_time", time.localtime())
## same way if we set as argument the timestamp
## but it actually take the utc timestamp, and convert it to actual timezone's time
print("local struct_time", time.localtime(timestamp))

# getting the timestamp from the struct_time
## actually mktime() accept local time time_struct only
print(time.mktime(struct_time))  # this will always assume that it is the local time
print(time.mktime(time.gmtime()))  # WARNING never do that, better use local time
## let say we about to create a timestamp from a tuple
my_tuple = (2025, 10, 5, 14, 30, 2, 6, 278, 0)
## if one argument is missing, error TypeError: mktime(): illegal time tuple argument
new_timestamp = time.mktime(my_tuple)
print(new_timestamp)
a = time.localtime()
b = time.gmtime()
print(a)
# time.struct_time(tm_year=2025, tm_mon=10, tm_mday=5, tm_hour=14, tm_min=54, tm_sec=32, tm_wday=6, tm_yday=278, tm_isdst=0)
print(b)
# time.struct_time(tm_year=2025, tm_mon=10, tm_mday=5, tm_hour=16, tm_min=54, tm_sec=32, tm_wday=6, tm_yday=278, tm_isdst=1)
print(time.mktime(a))
# the result is timestamp
## never do that since it is b gmtime() not give it to mktime() since mktime() accept local only
print(time.mktime(b))

# error TypeError when creating a timestamp without a value
# print(time.mktime())

# create current time, in human readable date and time
## accepts unix timestamp at UTC and convert to human readable time in local time
## returns human readable local time Sun Oct  5 19:13:55 2025
ct = time.ctime()
## actually it shows the local time
print(ct)
## time.ctime() return str type
print(type(ct))
## this timestamp 1759739759.70534 represents the time Sun Oct  6 10:35 something in local time Paris
print("ctime from timestamp paris", time.ctime(1759739759.70534))

# getting the current date from the struct
## accept struct_time
## returs human readable localtime
local = time.localtime()  # return struct
print(local)
## asctime returns human readable time, and accept a tuple struct_time
## Sun Oct  5 19:42:57 2025
## if not provided, it uses the current local time
print(time.asctime(local))
print(type(time.asctime(local)))

# comparison ctime() and asctime()
## since they both give human readable time, without argument sent, they give same result
print("ctime == asctime", time.ctime() == time.asctime(local))

struct_time = time.localtime()
print("struct_time", struct_time)
timestamp = time.mktime(struct_time)
print("timestamp", timestamp)
ctime = time.ctime(timestamp)
print("ctime", ctime)
asctime = time.asctime(struct_time)
print("asctime", asctime)
print("ctime == asctime", ctime == asctime)

# formateando
timestamp = time.time()
print(timestamp)
print(time.gmtime(timestamp))
struct_time_local = time.localtime(timestamp)
print(struct_time_local)
print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time_local))

# parseando tiempo
## regresa una entidad struct_time
strtiempo = "2025-10-03 12:30:00"
print(strtiempo)
tiempo = time.strptime(strtiempo, "%Y-%m-%d %H:%M:%S")
print(type(tiempo))
print(tiempo.tm_year)

print("aca para probar acceso con indices de struct_time")
st = time.localtime()
print(st[8])

print("attributes", len(dir(time)))
a = 0
for i in dir(time):
    if callable(getattr(time, i)):
        print(i, end="|")
        a += 1
print()
print("functions", a)
