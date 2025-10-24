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


print("attributes", len(dir(random)))
a = 0
for i in dir(random):
    if callable(getattr(random, i)):
        print(i, end="|")
        a += 1
print()
print("functions", a)
