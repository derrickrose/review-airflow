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
import math
from typing import Callable

print("math.radians of 45", math.radians(45))
from math import radians

print(radians(45))  ### nocion importantes
### 180 (°) = pi (radian)
### tan = sin / cos
### 2 pi (rad) = 360°
### radian = 180/pi
### radian = 57.29577951308232°
### 90 (°) = pi/2 ()

# el modulo math tambien tiene sus analogos hiperbolicos de las funciones circulares
## sinh(x)
## cosh(x)
## tanh(x)
## asinh(x)
## acosh(x)
## atanh(x)

# existe otro grupo de las funciones de math relacionadas con la exponenciacion
## e numero de Euler 2.718281828459045
## exp(x)
## log(x) logaritmo natural de x
## log(x, b) el logaritmo de x con base b
## log10(x) logaritmo decimal de x (mas preciso que log(x, 10))
## log2(x) mas preciso que log(x,2)
## pow(x, y) x potencia y  => incorporada y no se tiene que importar
## n * log(x) = log(x^n)
print("exp1", math.exp(1))
print("pow", math.pow(math.e, 1))
print(math.exp(2))
print(math.pow(math.e, 2))

print("egualité", math.exp(2) == math.pow(math.e, 2))  # False

print(pow(3, 2))
print("log(e)", math.log(math.e))
print(math.exp(1))
print(pow(math.e, 1))
print("egalite", math.exp(1) == pow(math.e, 1))  # True
print("______________________________")
print(3 * math.log(3))
print(math.log(pow(3, 3)))
print(math.exp(math.log(math.e)) == math.e)  # True
print("__-_--_-__-_-_-_-_-")
print(pow(math.e, 1) == math.exp(math.log(math.e)))
print(pow(2, 2) == math.exp(2 * math.log(2)))
print(math.log(math.e, math.e) == math.exp(0))
print("tatatatata")
print(math.exp(math.log(2)) == math.log(math.exp(2)))

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

print("attributes", len(dir(math)))
a = 0
for i in dir(math):
    if callable(getattr(math, i)):
        print(i, end="|")
        a += 1
print()
print("functions", a)
