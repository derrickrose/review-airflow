# MODULO 4
# muy a menudo = très souvent
# escarbar = creuser
# descomposicion la manera de separar codigo en funciones para que se podria probar separados
# inconcebible = inconcevable
# de donde provienen las funciones
# de python mismo por ejemplo print(), se les llama funciones integradas
# modulos preinstalados (vienen junto a python), pero requiere un paso adicional
# tu mismo puedes escribir tus funciones
# existe otras mas pero se refieren en clases, se omitira por ahora
from copy import deepcopy
from datetime import datetime
from functools import lru_cache


# definir una funcion
def function_name():
    # body
    print("funcion ejecutada")  # se debe ser cauteloso = il est nécessaire d'être prudent


# una funcion y una variable no pueden tener el mismo nombre
# function_name = 1
# print(function_name())
# invocar una funcion no definida resulta un NameError
# lista completas de las funciones en python https://docs.python.org/3/library/functions.html
# NameError cuando no es definida
# TypeError cuando utilizas parametros pero no es de acuerdo con su definicion y viceversa

# funciones parametrizadas
# parametros solo dentro de una funcion
# argumentos existen fuera de la funcion
def mifuncion(param):
    print("imprimiendo", param)


var = "argumento"
mifuncion(var)


# es posible que el argumento y la parametro tiene mismo nombre
# esto activa un mecanismo denominado sombreado, el parametro x sombrea cualquier variable
# con el mismo nombre pero solo dentro de la funcion que define el parametro
def message(number):
    print("Ingresa un número:", number)


number = 1234
message(1)
print(number)


# funciones parametrizadas
# las funciones pueden tener mas de un parametro

# paso de parametros posicionales
# es la tecnica que asigna cada argumento al parametro correspondiente
def mifuncion(param1, param2):
    print("imprimiendo", param1, param2)


mifuncion(1,
          2)  # paso de parametros es la tecnica que asigna los argumentos a cada parametro correspondiente  # next https://edube.org/learn/python-essentials-1-esp-edube/c-oacute-mo-las-funciones-se-comunican-con-su-entorno-11


# paso de argumentos con palabra clave
def intro(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)


intro(last_name="Perez",
      first_name="Juan")  # la posicion no es relevante  # intro(surname="aha", last_name="dood") # TypeError intro() got an unexpected keyword argument 'surname'


# combinar argumentos posicionales y de palabra clave
# una regla inquebrantable es que colocar posicional antes y luego por clave
def calc(a, b, c):
    print(a + b + c)


calc(1, c=3, b=2)
calc(c=3, b=2, a=1)
# calc(a=1, 2, c=3) # este enrola una error SyntaxError, positional argument follows keyword argument
calc(b=2, a=1, c=3)  # without mentionning b=, it will raise an TypeError calc() got multipe values for argument a


# funciones parametrizadas, mas detalles
# valor predefinidos
def intro(first_name, last_name="Perez"):
    print("Hola, mi nombre es", first_name, last_name)


intro("Juan")
intro(first_name="Emanuel")
intro("Juan", "Torizo")


# efectos y resultados : la instruccion return
# return sin una expresion => provoca la terminacion inmediata de la ejecucion de la funcion y un retorno instantaneo
# si una funcion no es destinada a producir un resultado, emplear la instruccion return no es obligatorio,
# se ejecutara implicitamente al final de la function
# return sin expression
def happy_new_year(wishes=True):
    print("Tres")
    print("Dos")
    print("Uno")
    if not wishes:
        return
    print("Felicidades")


happy_new_year()
happy_new_year(0)  # aqui veamos que no imprime lo de Felicidades al final por lo que el argumento es falso


# return con expression
# provoca la terminacion inmediata de la funcion
# evalua la expression y regresa el resultado
def happy_new_year(wishes=True):
    print("Tres")
    print("Dos")
    print("Uno")
    if not wishes:
        return
    return "Felicidades"


x = happy_new_year()  # la instruccion return enriquecida con la expression transporta el valor al lugar donde se ha invocado la funcion
print(x)

# unas pocas palabras acerca de None
# un valor que es ninguno llamado None
# print(None + 2)  # causara un error TypeError: unsuported operand type(s) for +: 'NoneType' and 'int'
# 2 circunstancias en las que None se puede usar :
# cuando asigna a una variable (o se devuelve como el resultado de una funcion)
# cuando se compara con una variable para diagnositac sur estado interno
value = None
if value is None:
    print("value is None")


# si una funcion no devuelve un cierto valor utilizando una clausula de expression return,
# se asume que devuelve implicitamente None

# efectos y resultados : listas y funciones
# lista como parametro
def list_sum(list):
    result = 0
    for item in list:
        result += item
    return result


print(list_sum([1, 2, 3]))  # print(list_sum(5)) # TypeError int object is not iterrable


# lista como resultado
def list_n(n):
    return [i for i in range(n)]


print(list_n(5))


# isinstance(val, int)
# lab: check day of year
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False


#
# Tu código del LABORATORIO 4.3.1.6.
#

def days_in_month(year, month):
    LEAP_YEAR_MONTHLY_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    NORMAL_YEAR_MONTHLY_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        return LEAP_YEAR_MONTHLY_DAYS[month - 1]
    else:
        return NORMAL_YEAR_MONTHLY_DAYS[month - 1]


#
# Tu código del LABORATORIO 4.3.1.7.
#

def day_of_year(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return
    if not (1 <= month <= 12):
        return
    if not (1 <= day <= days_in_month(year, month)):
        return
    total = 0
    for i in range(1, month):
        total += days_in_month(year, i)
    return total + day


#
# Escribe tu código nuevo aquí.
#

print(day_of_year(2000, 12, 31))
print(day_of_year(2050, 1, 31))
print(day_of_year(2050, 2, 32))

# check prime number
import math


def is_prime(n):
    """
    Check if a number is prime using a basic O(√n) algorithm.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Handle special cases
    if n <= 1:
        return False  # Numbers <= 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisors from 5 to √n
    # We can skip even numbers directly by using `i` and `i + 2`
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  # Check both i and i + 2 (optimized)
            return False
        i += 6  # Skip multiples of 2 and 3 (increment by 6)

    return True  # If no divisors are found, n is prime


print(is_prime(13))


# HELP
# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.
# conversion from miles_gallo to liters_km and viceversa
def liters_100km_to_miles_gallon(liters):
    # on a consommation litre pour 100 km
    # on cherche distance por gallon
    # return miles / gallons
    # place aux calculs
    # 100 km à transfo en miles
    ## 1 mile = 1609.344 m
    ## mile = 1.609344 km
    ## miles = 100 Km
    ## miles = 100/1.609344
    # 1 galon =  3.785411784 lit
    ## galons = liters
    return (100 / 1.609344) / (liters / 3.785411784)


def miles_gallon_to_liters_100km(miles):
    # on cherche consommation pour 100 km
    # on a distance pour 1 gallon
    # 1 gallon => combien de liters
    # 1 mile => 1609.344 m
    # miles => miles * 1609.344 m
    # miles => miles * 1.609344 km
    # miles => (miles * 1.609344 /100)
    return 3.785411784 / (miles * 1.609344 / 100)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

va = 100
if type(va) == int:
    print("int")
print(int)


# las funciones y sus alcances
def scope_test():
    xx = "local"


# print(xx) NameError undefined

def do_local():
    tatanta = "local"  # la variable creada dentro de la funcion no es la misma que la de afuera
    # la variable dentro es una sombra de la que esta fuera
    print("do_local", tatanta)


tatanta = "global"  # la respuesta es una variable fuera de una funcion tiene alcance dentro de la funcion
do_local()
print(tatanta)


# de manera general podemos definir :
# una variable fuera de una funcion tiene alcance dentro de la funcion
# esto excluyendo una variable que tiene mismo nombre
# asignar un valor hace que la funcion cree su propria variable


def scot():
    # toro = "local"
    print("toro en local", toro)


toro = "global"
scot()
print(toro)
# palabra clave reservada global

ton = "ton"
print(ton)


def toto():
    global ton  # esto hace que python no crea una nueva varible, usa la que esta afuera
    ton = "tontont2"
    print("ton en local", ton)


toto()
print(ton)


# interacion de una funcion con sus argumentos
def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


var = 1
my_function(var)
print(var)  # en conclusion al recibir un valor, esto no se propaga fuera de la funcion


def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


n = 1
my_function(n)
print(n)


# aun que tiene mismo nombre la variable afuera y el parametro, no afecta el cambio afuera, para escalares
# una funcion recive el valor del argumento, no el argumento en si misma (cuando el valor es escalar)

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)  # misma regla, la funcion toma el valor del argumento no el argumento


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# cambiar el valor de la lista tiene alcance dentro de la funcion
# si se modifica la lista identificada por el parametro, la lista reflejara el cambio


var = [1, 2, 3]


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    my_list_1.append(0)
    print("Print #2:", my_list_1)
    print("Print #3:", var)


my_function(var)
print(var)

var = [1, 2, 3]


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    my_list_1.insert(0, 0)
    print("Print #2:", my_list_1)
    print("Print #3:", var)


my_function(var)
print(var)

varvarvar = [1, 2, 3]


def my_function(my_list_1):
    print("toto Print #1: mylist", my_list_1)
    global varvarvar
    del varvarvar
    print("toto Print #2: mylist", my_list_1)  # print("Print #3: varvarvar", varvarvar)


my_function(varvarvar)
# print(varvarvar) # NameError

vorvorvor = [1, 2, 3]


def my_function(my_list_1):
    print("Print #1: mylist", my_list_1)
    # del vorvorvor # UnboundLocalError cannot access local variable 'vorvorvor' where it is not associated with a value
    print("Print #2: mylist", my_list_1)  # print("Print #3: varvarvar", varvarvar)


my_function(vorvorvor)  # print(varvarvar) # NameError

cat = [1]
dog = cat
del cat
print(dog)
cat = dog
del dog
print(cat)
del cat  # print(cat)

print("-----------------")
cocorico = [1, 2, 3]


def co(my):
    print(my)
    my = [4, 5, 6]
    print(my)
    my = my[0:1]
    print(my)


co(cocorico)
print(cocorico)

print("--------------------")
tasa = [1]


def t(my):
    print(my)
    my += [4, 5, 6]  # del, insert, append(), += esto cambiara la lista
    print(my)
    my = my[0:1]
    print(my)


t(tasa)
print(tasa)

print("-----------------------------------")

taratasy = [1, 2, 3]


def tt(my):
    print(my)
    mini = my[:]
    print(mini)
    mini.append(4)
    print(my)
    print(mini)


tt(taratasy)
print(taratasy)  # for list of list better use deepcopy

print("-----------------------------------")
hola = [[1, 2], [3, 4]]

import copy


def greet(name):
    ti = name[:]
    ta = deepcopy(name)
    ta[0].append(1)
    ti.append([0])
    # ti[0].append(1)
    print(ta)
    print("Hello, ", name)
    print(ti)
    ti.append(888)
    print("ti", ti)


greet(hola)
print(
    hola)  # shallow copy (slicing) ta = [1,2,3] , to = ta[1:]  # they dont share the same reference until the values are also a list  # so to fix this behavior, better use copy.deepcopy()

postre = [1, 2, 2]
mal = postre
postre = [0]
postre.append(1)
print(postre)
print(mal)

bob = [0]


def bobito(a):
    b = a[:]
    b.append(2)
    print(a)


bobito(bob)
print(bob)


# next
# 4.5.1.1
# creando funciones con 2 parametros
def bmi(weight, height):
    if height <= 1.0 or height >= 2.5 or weight <= 20 or weight > 200:
        return None
    return weight / height ** 2


print(bmi(400, 1.72))


def lb_to_kg(weight):
    return weight * 0.45359237


def ft_and_inch_to_m(feet, inches=0.0):
    return feet * 0.3048 + inches * 0.0254


# so for someone 5'7" tall with 176 lbs what is the bmi
print(bmi(lb_to_kg(176), ft_and_inch_to_m(5, 7)))


# algunas funciones simples
# teorema de Pitagoras
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


# hypotenusa es la parte mas larga, al oposicion a los catetos
def is_right_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return False
    if c > b and c > a:
        return c ** 2 == a ** 2 + b ** 2
    if b > c and b > a:
        return b ** 2 == a ** 2 + c ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


# calculo del area de un triangulo
# la formula de heron
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))


# algunas funciones simples : fibonacci
def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    elmnt1 = elmnt2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elmnt1 + elmnt2
        elmnt1, elmnt2 = elmnt2, sum
    return sum


t1 = datetime.now()
print(fibonacci(10))
t2 = datetime.now()
print("iterative", t2 - t1)


# recursividad
def fibonacci_r(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)


t3 = datetime.now()
print(fibonacci_r(10))
t4 = datetime.now()
print("recursive", t4 - t3)


# algunas funciones simples : factoriales
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    produto = 1
    for i in range(2, n + 1):
        produto *= i
    return produto


def factorial_r(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_r(n - 1)


print(factorial_r(5))
print(factorial(5))

print(factorial(4))

# bucle infinito asi que arroja un error RecursionError : maximum recursion depth exceeded
# def factorial(n):
#     return n * factorial(n - 1)
import sys

print(sys.getrecursionlimit())

# tuplas y diccionarios
# tipo de secuencia es un tipo de dato en python el cual es capaz de almacenar mas de un valor
# # o ninguno (si la secuencia esta vacia), los cuales pueden ser secuencialmente examinados
# podemos definirlo asi tambien que una secuencia es un tipo de dato que puede ser escaneado por el bucle for
# mutabilidad
# los datos mutables pueden ser actualizados libremente en cualquier momento por eso se dice "in situ"
## e.g. list.append(1)
## los datos inmutables no pueden ser modificados de esta manera
# tupla
# una tupla en python es una lista que no se puede ser modificado, para modificar, tienes que crear una nueva
tupla = (1, 2, 3)
# nota cada elemento de una tupla puede ser de tipos diferentes
tupla2 = 4.2, 5., .125
print(tupla)
print(tupla2)
# crear una tupla con parentesis
tupla = ()
print(tupla)
# para asignar un solo valor
tupla = 1,
print(tupla)

# como utilizar un tupla
# para leerlo es como una lista
# pero no se puede modificar su valor
tupla = (1, 2, 3)
# tupla.append(0)# AttributeError tuple object has no attribute append
# del tupla[0] # TypeError tuple object doesnt support item deletion
# tupla[0] = 0  # TypeError tuple object does not support item assignment
print(tupla)
tupla = tupla + (4,)
print(tupla)

# como utilisar una tupla continuacion
# la funcion len() accepta tuplas tambien
# el operador + puede unir las tuplas
# el operador * puede multiplicar las tuplas, asi como las listas
# los operadores in y not in tambien
tupla = (1, 2, 3)
print(tupla)
if 1 in tupla:
    print("1 is in tupla")
if 4 not in tupla:
    print("4 is not in tupla")

# los elementos de una tupla pueden tambien ser variables no solamente literales
var = 1, 2, 3
t1 = 1,
t2 = 2,
t3 = var
print(t1, t2, t3)
# una de las propriedades de las tuplas mas utiles es que pueden aparecer en el lado izquierdo del operador
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

# diccionario
# tipo de dato en python, no es una secuencia pero puede adaptarse con un procesamiento secuencial
# es mutable
# funciona literal al diccionario real
# es un cojunto de claves y valores
# cada clave debe ser unica
# una clave puede ser un tipo de dato de cualquiera, podria ser un entero, flotante hasta incluso cadena
# funcion len() aplica tambien, regresa la cantidad de pares (clave-valor) en el diccionario
# es una herramienta de un solo sentido, significa que si es un diccionario frances-espagnol,
# puedes buscar una palabra en frances para encontrar su contraparte en espagnol
# un diccionario en python no guarda el orden
dico = {"chien": "perro", "chat": "gato"}
dico2 = {"jefe": 8126793166, "chico": 8126793167}
empty = {}
print(dico)
print(dico2)
print(len(dico))
# utilizar un diccionario es semejante a la indexacion (indexacion es recuperar valor de una lista)
print(dico["chien"])
print(dico2["jefe"])
print(
    empty)  # pero ojo, a partir de python 3.6x, los diccionarios se han convertido en colecciones ordenadas  # no se puede utilizar una clave que no existe
# dico["presidente"] # provocara un error KeyError
# afortunadamente, tenemos un remedio
words = ["chien", "chat", "presi"]
for word in words:
    if word in dico:
        print("la palabra es", dico[word])
    else:
        print("no se encontro la palabra", word)

# cuando un diccionario es mul larga, podemos utilizar la sangria francesa
dic = {"chien": "perro", "chat": "gato", "president": "trump", "ville": "boulogne billancourt", "tour": "operator",
       "main": "mano"}

# como utilizar un diccionario
# metodo keys()
for key in dico.keys():
    print(key, "->", dico[key])
# se puede ordenar tambien las claves
for key in sorted(dico.keys()):
    print(key, "->", dico[key])
# el metodo items()
for ke, value in dico.items():
    print(ke, "->", value)

# existe tambien el metodo .values() casi identico a .keys()
# pero casi no se usa
print(dico.values())

# modificar, agregar y eliminar valores de un diccionario
dico = {"perro": "chien"}
print(dico)
dico["gato"] = "chat"  # agregar
print(dico)
del dico["perro"]  # eliminar
print(dico)
dico["gato"] = "mimi"  # cambiar
print(dico)
# tambien se puede usar el metodo update
dico.update({"perro": "perro"})
print(dico)
dico.update({"perro": "wouuff"})
print(dico)  # del dico["tata"] # KeyError
dico.popitem()  # antes de version 3.6.7 elimina al azar (par hasard), pero despues elimina el ultimo agregadol
print(dico)
import sys

print(sys.version)

# las tuplas y los diccionarios trabajen juntos
# una programa que conteo los promedios de los alumnos indresando cada paso el nombre y luego las calificaciones
# tambien se puede utilizar la funcion tuple(), eso cuando se quiere convertir una lista en tuple
va = [0, 1]
print(type(va))
va = tuple(va)
print(type(va))
print(type(va := list(va)))
print(type(va))

# punto clave diccionario
dic = {"chien": "perro", "chat": "gato"}
print(dic["chien"])
print(dic.get("chien"))  # hace mismo efecto
print(type(dic.keys()))
print(type(dic.values()))

# eliminar todo elemento de un diccionario  uusar metodo clear
# del se puede usar tambien para eliminar un elemento o el diccionario entero
print(dic)
dic.clear()
print(dic)

# el metodo copy para copiar
dico = {"chien": "perro", "chat": "gato"}
print(dico)
dico2 = dico.copy()
print(dico2)
dico2["chien"] = "perra"
print(dico)
print(dico2)

# exo
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)

# we can count the number of duplicates elements in a tuple using the method .count(el valor por buscar)
tup = 1, 2, 3, 1, 2, 3, 8
print(tup.count(1))
a = [1, 2, 3, 1, 2, 3, 8]
print(a.count(1))

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

# for item in (d1, d2):
#     for k, v in item.items():
#         d3[k] = v
# print(d3)
# d3.clear()

for item in (d1, d2):
    d3.update(item)

print(d3)

colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = {}
for color in colors:
    colors_dictionary.update({color[0]: color[1]})
print(colors_dictionary)

colors_dictionary.clear()

for color in colors:
    colors_dictionary[color[0]] = color[1]
print(colors_dictionary)

colors_dictionary = dict(colors)
print(colors_dictionary)

colors = [["green", "#008000"], ["blue", "#0000FF"]]
colors_dictionary = dict(colors)
print("from list of list", colors_dictionary)

dic = {"chien": "perro", "chat": "gato"}
tup = tuple(dic.values())
print(tup)

# # 4.7.1.7 excepciones
# errores en los datos frente a erroers en el codigo
# depurar tu codigo <=> encontrar y eliminar errores
value = "c"

# no es la recomendacion de python
if type(value) is int:
    print("valor", 1 / int(value))  # ValueError invalid literal for int() with base 10: 'c'

# ahora la recomendacion de python
# palabras claves se genera/ se genero un excepcion
val = "0"
try:
    print(1 / int(val))
except ValueError:
    print("no se que hacer con el valor")
except ZeroDivisionError:
    print("no se puede dividir entre 0")
except:  # excepcion por defecto # debe ser el ultimo siempre
    print("otro error")

# algunas excepciones utiles
# ZeroDivisionError cuando se intenta dividir entre cero
# ValueError cuando una funcion como int() o float() esta utilizada con valores no adecuados
# TypeError cuando intentas aplicar cuyo dato no es aplicable, e.g. val = [], val[.5]=1
# AttributeError intentas activar un metodo que no existe, e.g. val = {}, val.append(1)
# SyntaxError linea que viola la gramatica de python
# KeyboardInterrupt

temp = 0

if temp > 0:
    print("Por encima de cero")
elif temp < 0:
    prin(
        "Por debajo de cero")  # error puesto intencionalmente para que vemos que python no lo cachea por que no pasa por este camino  # la importancia de probar cada camino
else:
    print("Cero")  # depurador IDLE

val = "0"
try:
    print(1 / int(val))
except (ValueError, ZeroDivisionError):  # puede combinar varias excepciones en una sola linea
    print("valor incorrecto o se ha rato la regla de division entre cero")
except:  # excepcion por defecto # debe ser el ultimo siempre
    print("otro error")

# 4.7.2.1  proyecto tic tac toe
import random
print("random")

