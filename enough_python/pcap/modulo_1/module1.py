# que es un modulo ?
## crecimiento de los codigos y desarolladores que lo mantengan
## solucion habra que dividirlo (el codigo muy grande de un archivo fuente) en partes
## reunir las partes creadas en un todo funcional
## por ejemplo :
### la interfaz de usuario (mediante widgets y una pantalla grafica)
### la logica (la parte que procesa los datos y produce resultados)
## cada parte todavia se puede dividir es la descomposicion
## como hacer eso ? => viene el modulo
## asi que un modulo es la manera de descomposicion de un software en partes pequenas y funcionales
# un archivo que contiene definiciones y sentencias de Python que se pueden importar y utilizar cuando sea necesario

# como hacer uso de un modulo ?
## se desea utilizar un modulo ya existente => usuario del modulo
## cuando se desea crear un modulo => provedor del modulo
## un modulo se identifica por su nombre
## se entrega una cantidad bastante grande de modulos junto con Python => equipamiento adicional de Python
## todos estos modulos junto con las funciones integradas forman la biblioteca estandar de python
## python library https://docs.python.org/3/library/index.html
## cada modulo consta de entidades (como libro consta de capitulos)## cada modulo consta de entidades (como libro consta de capitulos)
## estas entidades pueden ser funciones, variables, constantes, clases y objetos
## si se sabe como acceder a un modulo en particular, se puede utilizar cualquiera de las entidades que almacena
## ejemplo de modulos : math (su nombre) y consta de entidades (no solo funciones matematicas),
### ejemplo de funciones en el modulo math (mas usado) sin(), log() ...

# importando un modulo
## para que un modulo sea utilizable, hay que importarlo
## se realiza una instruccion llamada import (que tambien es una palabra reservada)
## la forma mas sencilla de importar un moduo
import math  # se puede colocarse en cualquier parte del codigo
import sys  # por si se desea importar otro modulo
import math, sys  # o se puede colocar un una linea

# namespace es un espacio (entendido en un contexto no fisico) en el que existen algunos nombres y los nombres no entran en conflicto
## dentro de un namespace, cada nombre debe permanecer unico
## eso significa que un nombre se puede desaparecer cuando entre un nuevo entidad ya conocido
## si el modulo de un nombre especificado existe y es accessible (un modulo es de hecho un archivo fuente de Python),
### Python importa su contenido, se hacen conocidos todos los nombres definidos en el modulo,
### pero no ingresan al namespace del codigo
### esto significa que puedes tener tus proprias entidades llamadas sin o pi y no seran afectadas en alguna manera por la importaccion
print(math.sin(60))  # acceder a una entidad del modulo math con solo moduloPUNTOnombreDeLaEntidad
## no importa si alguno de los nombres del codigo y del namespace del modulo estan en conflicto o no
### si va funcionar
sin = 2
print(sin)
print(math.sin(60))  # entrando al namespace de math
print(math.sin(math.pi / 2))


### evitar conflicto
def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None


pi = 3.14
print(sin(pi / 2))
print(math.sin(math.pi / 2))

# importacion con precision (cual entidad deseamos importar)
from math import pi  ## efecto de esta forma de importacion

### las entidades listadas son las unicas importadas del modulo indicado (no se importa otra entidades)
### los nombres de las entidades importadas pueden ser accedidas dentro del codigo sin especificar el nombre del modulo de origen
### no se puede importar otras entidades utilizando una linea como print(math.pi)
print(pi)  # como podemos ver el valor de pi es el nuevo valor
from math import sin, pi

print("---------------")
print(sin(pi / 2))
pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(
    sin(pi / 2))  # en conclusion es que se redefine pi y sin(), asi que nocion de namespace se modifica el nombre antiguo

# importando un modulo con *
## importa todas las entidas del modulo
from math import *
print(e) # constante de eudler
## pero no se debe usar por no tener conflicto en el namespace

# importar un modulo con la palabra clave reservada as
import math as m
print(m.pi)
## nota: despues de una importacion de un modulo con alias, el nombre original del modulo se vuelve inaccessible y no se debe usar
from math import pi as PI
print(PI)
from math import pi as PI, sin as SIN
print(SIN(PI / 2))