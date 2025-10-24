# trabajando con archivos
## para linux generalmente la codificacion es "utf-8"
## puedes consultar la configuracion del sistema operativo
## prorpiedades de la funcion read()
### leer un numero determinado de caracteres (incluso solo uno) y devolverlos como cadena
### leer todo el contenido del archivo y devolverlo como una cadena
### si no hay mas que leer (el cabezal de lectura virtual llega al final del archivo), la funcion devuelve una cadena vacia

from os import strerror

try:
    counter = 0
    stream = open("text.txt", "rt")
    char = stream.read(1)
    while char != "":
        print(char, end="")
        counter += 1
        char = stream.read(1)
    stream.close()
    print()
    print()
    print("Total de caracteres leidos:", counter)
except IOError as e:
    print("Error al abrir el archivo:", strerror(e.errno))

## se usa read() sin argumento o argumento None, cuando estas seguro que si acaba en la memoria asi que leerlo de una vez
## recuerda que leer un archivo muy grande (en terabytes) usando este método puede danar tu sistema operativo
## read() sin parametro lea todo el contenido del archivo y regresa una cadena
print("___________read_sin_parametro_______________")
try:
    counter = 0
    stream = open("text.txt", "rt")
    content = stream.read()
    print(content)
    for char in content:
        print(char, end="")
        counter += 1
    stream.close()
    print()
    print()
    print("Total de caracteres leidos:", counter)
except IOError as e:
    print("Error al abrir el archivo:", strerror(e.errno))

# readline()
from os import strerror

print("_________readline_______________")
try:
    counter = linecount = 0
    stream = open("text.txt", "r")
    line = stream.readline()
    while line != '':
        linecount += 1
        for char in line:
            print(char, end="")
            counter += 1
        line = stream.readline()
    print(counter)
    print(linecount)
    stream.close()
except IOError as e:
    print("Error al abrir el archivo:", strerror(e.errno))

# readlines
## readlines sin parametro lea todo el archivo y regresa una lista de cadena
## lista de cadena vacia cuando al ultima linea del archivo
## readlines es mas efectivo por que menos invocaciones
from os import strerror

print("______________readlines_______________")

try:
    counter = linecount = 0
    stream = open("text.txt", "rt")
    lines = stream.readlines()
    print(lines)
    stream.close()
    for line in lines:
        linecount += 1
        for char in line:
            counter += 1
            print(char, end="")
    print(counter)
    print(linecount)
except IOError as e:
    print("Erreur rencontrée", strerror(e.errno))

print("______________readlines___con argumento____________")
from os import strerror

## readline con parametro regresa las lineas existentes dentro del numero del buffer
## 1 sera un byte (the hint)
## 20 sera 20 bytes de la linea
## python at least read one line even if it exceeds the hint
## regresa arreglo de cadenas
try:
    counter = retrieving = 0
    stream = open("text.txt", "rt")
    line = stream.readlines(50)
    print(line)
    stream.close()
except IOError as e:
    print("Erreur rencontrée", strerror(e.errno))

from os import strerror
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

## con iterator
print("______________iterator_______________")
try:
    counter = lines = 0
    for line in open("text.txt", "rt"):
        lines += 1
        for char in line:
            counter += 1
            print(char, end="")
    print(counter)
    print(lines)
except IOError as e:
    print("Error al abrir el archivo:", strerror(e.errno))

# manejo de archivo escribir
## write() con un flujo abierto
## mode "w" borra el archivo y crea una nueva si existe
## no escribe linea, entra que hacerlo tu
## write puede escribir caracter
try:
    stream = open("nex_text.txt", "wt")
    for i in range(10):
        line = "Hola numero" + str(i) + "\n"
        for char in line:
            stream.write(char)  # import time  # time.sleep(1)
    stream.close()
except IOError as e:
    print("Error", strerror(e.errno))

## tambien write puede escribir cadena
try:
    stream = open("nex_text2.txt", "wt")
    for i in range(10):
        stream.write("Hola numero" + str(i) + "\n")
        import time  # time.sleep(1)
    stream.close()
except IOError as e:
    print("Error", strerror(e.errno))

# que es un bytearray
## datos amorfos (que no tienen niguna forma) son solo serie de bytes
## esto no significa que estos bytes no puedan tener su proprio significado
## o que puedan representar ningun objeto util,
## ejemplo graficos de mapa de bits
## los datos amorfos no pueden almacenarse utilizando ninguno de los medios presentados anteriormente, no son cadenas ni listas
## debe haber un contenido especial capaz de manejar dichos datos
## Python tiene mas de un contenedor, uno de ellos es una clase especializada llamada bytearray
## bytearray como sun nombre indica es un arreglo conteniendo bytes
## crear dicho contenedor capaz de almacenar 10 bytes, y llena todo el arreglo con ceros
## es mutable
data = bytearray(10)
for i in data:
    print(i, end=" ")
print()
data[0] = 1
for i in data:
    print(i, end=" ")
## Bytearrays se semejan con arreglos en muchos aspectos (ressemblence)
## son mutables, susceptibles a la funcion len()
## puedes acceder a cualquiera de sus elementos usando indexacion como los arreglos
## no puedes poner un valor que no sea entero ==> TypeError
## valor demasiado grande ==> OverflowError
data = bytearray(10)
# data[0] = 256 ## ValueError valor debe ser de 0 hasta 255
# data[0] = 2.0 ## TypeError
data = bytearray()
print()  #
data.append(1)
print(data)  # bytearray(b'\x01')
print(data[0])
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

## escribir un arreglo de bits en un archivo binario
from os import strerror

data = bytearray(10)

for i in range(10):
    data[i] = 97 + i
## si se desea que el archivo sera lisible, habra que reemplazar el 10 con ord('a') ya que es 97
## stream.write() devuelve la cantidad de bytes escritos correctamente
try:
    stream = open("data.bin", "wb")
    stream.write(data)
    stream.close()
except IOError as e:
    print("error surgio", strerror(e.errno))

# leer un archivo binario
from os import strerror

print("______________leer un archivo binario read sin param_______________")
try:
    stream = open("data.bin", "rb")
    data = stream.read()
    data2 = bytearray(data)
    print(data, data2)
    stream.close()
    for a, b in zip(data, data2):
        print(a, b, hex(a), hex(b), chr(a), chr(b))
except IOError as e:
    print("error", strerror(e.errno))

## leer un binario mediente de read() con parametro
from os import strerror

print("______________leer un archivo binario_______________")
try:
    stream = open("data.bin", "rb")
    data = stream.read(1)
    while data != b'':
        data = stream.read(1)
        print(str(data), end='*')

    stream.close()
except IOError as e:
    print("error", strerror(e.errno))
print()
a = 0b1
print(a)
print(type(a))
print(bin(a))
print(str(a))

## leer un binario mediente de stream.readinto() sin parametro
print("______________leer un archivo binario con filter_______________")
data = bytearray(2048)
try:
    stream = open("data.bin", "rb")
    stream.readinto(data)
    stream.close()
    data = filter(lambda x: x != 'b' and x != 0b0, data)
    for b in data:
        print(hex(b))
except IOError as e:
    print("error", strerror(e.errno))

# copiando archivos
# fiavianaA = input("Ingrese el nombre del archivo a copiar: ")
# fiavianaA = "data.bin"
# try:
#     fiaviana = open(fiavianaA, "rb")
# except IOError as e:
#     print("Error al abrir el archivo:", strerror(e.errno), str(fiavianaA))
#     exit(e.errno)
# # alehaA = input("Ingrese el nombre del archivo destino: ")
# alehaA = "data2.bin"
# try:
#     aleha = open(alehaA, "wb")
# except IOError as e:
#     print("Error al abrir el archivo:", strerror(e.errno), str(alehaA))
#     fiaviana.close()
#     exit(e.errno)
# buffer = bytearray(65536)
# fiaviana.readinto(buffer)
# aleha.write(buffer)
# fiaviana.close()
# aleha.close()

## cuidado que debido a que el buffer es demasiado grande, lo llena el resto con cero, entonces
## en el archivo de destino se ha escrito muchos NULL


# resumen
