# trabanjo con modulos estandar
## la function dir() muestra todas las entidades en orden alfabeticamente de un modulo en particular
## habra que importarlo como un todo
from math import radians

print(dir(list))
## print(dir(math)) #ocasiona un error, habra que importar el modulo math
import math

print(dir(math))
## nota si el nombre del modulo tiene un alias al importarlo, tienes que usar el alias
import collections as c

print(dir(c))
# print(dir(collections)) NameError

# modulo math
## todas toman un argumento (una medida de angulo medidos en radianes)
## cuidado con tan(), no acepta todos argumentos
## primer grupo
### sin(x) seno
### cos(x) coseno
### tan(x) tangente de x
## tambien sus versiones inversas
### asin(x) arcoseno de x => buscar el angulo en radian sabiendo su sinus
### acos(x) arcocoseno de x
### atan(x) arcotangente de x
## para trabajar eficazmente con mediciones de angulos, el modulo math proporciona las siguientes entidades :
### pi
### radians(x) convierte de grados a radianes
### degrees(x) convierte de radianes a grados
print(math.radians(45))
print(radians(45))  ### nocion importantes
### 180° = pi * radian
### tan = sin / cos
### 2 pi rad = 360°
### radian = 180/pi
### radian = 57.02958°
### 90° = pi/2 rad

# el modulo math tambien tiene sus analogos hiperbolicos de las funciones circulares
## sinh(x)
## cosh(x)
## tanh(x)
## asinh(x)
## acosh(x)
## atanh(x)

# existe otro grupo de las funciones de math relacionadas con la exponenciacion
## e numero de Euler
## exp(x)
## log(x) logaritmo natural de x
## log(x, b) el logaritmo de x con base b
## log10(x) logaritmo decimal de x (mas preciso que log(x, 10))
## log2(x) mas preciso que log(x,2)
## pow(x, y) x potencia y  => incorporada y no se tiene que importar
## n * log(x) = log(x^n)
print(pow(3, 2))
print(math.log(math.e))
print(math.exp(1))
print(pow(math.e, 1))
print(math.exp(math.log(math.e)))
print(pow(math.e, 1) == math.exp(math.log(math.e)))
print(pow(2, 2) == math.exp(2 * math.log(2)))
print(math.log(math.e, math.e) == math.exp(0))

# funciones seleccionadas del modulo math
## ceil(x) devuelve el entero mas pequeno mayor o igual que x
## floor(x) el entero mas grande menor o igual que x
## trunc(x) el entero truncado de x
## factorial(x) devuelve x! (x tinene que ser un valor entero y no negativo)
print(math.ceil(1.5))  # 2
print(math.floor(1.5))  # 1
print(math.trunc(1.5))  # 1
print(math.factorial(3))  # 6
# print(math.factorial(4.0)) TypeError
# print(math.factorial(-2)) ValueError

# modulo random
## no es aleatorio natural, es pseudo aleatorio debido a que se calcula por un algoritmo con un valor de entrada llamada semilla
## luego produce otros valores semillas (pero se puede repetir aun que es fuera de nuera capacidad humana)
## la funcion random() produce un numero dentre 0.0 y 1.0
import random

for i in range(5):
    print(random.random())  # cada vez diferente
## la funcion seed()
## la funcion seed() es capaz de directamente establecer la semilla del generador
### seed() establece la semilla con la hora actual
### seed(int_value) establece la semilla con el valor entero int_value
random.seed(0)
print("seed(0)")
for i in range(5):
    print(
        random.random())  # cada vez diferente pero el orden de salida de los numeros se queden cada vez que establecemos el seed()
random.seed(0.)
print("seed(0)")
for i in range(5):
    print(
        random.random())  # # cada vez diferente pero el orden de salida de los numeros se queden cada vez que establecemos el seed()

# randrange y randint
## randrange(fin)
## randrange(inicio, fin)
## randrange(inicio, fin, incremento)
## eso toman un valor aleatorio (pseudo) del range(fin), range(inicio, fin), range(inicio, fin, incremento)
## randint(izquierda, derecha) igual a randrange(izquierda, derecha+1) <=> sin exclusion del lado derecha
## no se olvide de la exclusion implicita del lado derecho
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
print(randint(0, 1))

## esas funciones tienen una desventaja importante :
### pueden producir valores repetidos incluso si el numero de invocaciones posteriores no es mayor que el rango especificado
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

# las funciones choice y sample
## como podemos ver no es una buena opcion
## mejor usar choice(secuencia) y sample(secuencia, elementos_a_elegir=1)
## ventaja : no se puede predecir la salida
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))  # devuelve un valor aleatorio elegido de la lista
print(sample(my_list, 5))  # devuelve una lista que consta de 5 elementos elegidos de la lista de entrada
print(sample(my_list, 10))  # devuelve una lista de 10 valores elegidos de la lista

# como saber donde estas ?
## imagina el entorno de tu programa como una piramide que consta de varias capas o plataformas
###       -tu codigo--
###      --PYTHON-------
###     -System Operativo-
###    ------hardware------
### entonces crear un archivo pasa por todas esas capas hasta el final el hardware (disco duro donde se almacena el archivo)

# modulo platform
from platform import platform

print(platform())
print(platform(aliased=True))  # if the name is different to common name o cualquier valor distinto a cero
print(platform(terse=True))  # show minimum information about igual aqui
print(platform(True, True))
import platform

print(platform.machine())  # nombre generico del processador
print(platform.processor())  # nombre real del processador
print(platform.system())  # Linux
print(platform.version())  # version del sistema operativo

### la version de python que utilize
print(platform.python_implementation())  # CPython
print("tup", platform.python_version_tuple())  # ('3','12','3')
print(platform.python_version())
print("branch", platform.python_branch())

print("compiler", platform.python_compiler())
print("build", platform.python_build())
print("revision", platform.python_revision())

### los modulos de python aqui https://docs.python.org/3/py-modindex.html

# modulo math tiene 50 funciones y constances
# modulo random tiene 60 entidades
# modulo platform tiene 70 funciones

# pregunta
# habra manera de saber que si es un constante o una funcion lo que devuelve el dir()
## preguntando eso puede guiarse con saber como identificar una clase, funcion, ...
