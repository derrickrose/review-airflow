# paquete
## juega la funcion de una carpeta o directorio de los archivos por los modulos
## crear un modulo modulo.py
## crear un otro archivo main.py y importa modulo.py
## ejecutando main.py hay una nueva carpeta que se creo, se llama __pycache__
## y dentro veremos dos archivos main.cpython-312.pyc y modulo.cpython-312.pyc pyc viene de python compilado
## el directorio __pycache__ se ubica en el directorio de inicio del modulo
## no es un codigo compilado, es un codigo semi-compilado interno de Python, listo para ser ejecutado por el interprete de Python
## como tal archivo no requiere tantas comprobaciones como las de un archivo fuente, la ejecucion comienza mas rapido y tambien se ejecuta mas rapido
## gracias a eso las importaciones posteriores seran mas rapidas que interpretar el codigo fuente desde cero
## python puede verificar si el archivo fuente del modulo ha sido modificado (en este caso el archivo pyc sera reconstruido) o no
## (cuando el archivo pyc pueda ser ejecutado al instante)

# que pasa realmente
## cuando se importa un modulo, su codigo es ejecutado implicitamente por Python (una sola vez)
## esto significa si un modulo mod esta importado en modulo, y mod importado en main, solo se produce la primera importacion
## y silenciosamente omite la importaciones posteriores
## puede ser mucho mas que eso
from module1_2 import __name__ as nom

## dentro del modulo, el nombre es __main__ , pero fuera (importado a otro parte) __name__ tendra el nombre del archivo
## cuidado por que se ejecuta tambien el modulo importado
print(nom)  ## imprime module1_2
print(__name__)  ## imprime __main__

## con esto puedes saber el contexto en lo cual se activo tu codigo
## la mejora manera de utilizar la variable __name__ es para pruebas de las funciones en un modulo, se omitira eso cuando es importada

# no se puede ocultar una variable en python
## puedes acceder, cambiar, entonces solo se puede informar a los usuarios que no se debe por que es personal (pero no privada)
## poner un guillon bajo o dos guillones bajos para decir que es privado (pero solo es un convenio)
## nota el shabang para decir a un systema operativo linux con que programa se ejecuta
### se nomina tambien como shebang, hashbang, poundbang, hashpling
## una cadena quizas una multilinea doc-string para explicar brevemente el contenido del modulo

# ya vamos a separar los modulos y el programa principal en carpetas diferentes
## para lidiar con esto vamos a ver como python busca los modulos
## hay una variable especial (en realidad una lista) que almacena todas las ubicaciones (carpetas o directorios)
## que se buscan para encontrar un modulo que ha sido solicitado por la instruccion import
## python examina estas carpetas en el orden en que aparecen en la lista
### si el modulo no aparece en ninguno de estos directorios, la importacion falla
### de lo contrario se tomara en cuenta la primera carpeta que contenga un modulo con el nombre deseado
### si alguna carpeta restante contiene un modulo del mismo nombre, se ignorara
### la variable se llama path del modulo sys
import sys

for p in sys.path:
    print(p)  ### la carpeta en la cual se ejecuta el programa aparece en el primer elemento de la ruta

### tomando en cuenta que hay un arhivo zip en la ruta y esto no es un error, python puede tratar los zips como carpeta ordinaria
### para esto haremos un sys.append(""../modulo") en el codigo main ruta relativa
### nota que esto funciona solo si ejecutamos el main directamente en su carpeta inicial
### si no podemos hacer sys.append(""RUTA_COMPLETA") ruta absoluta
### tambien se puede usar insert()

# primer paquete
# continuar con https://edube.org/learn/python-essentials-2-esp/m-oacute-dulos-y-paquetes-15

# la estructura de los paquetes parece a la estructura de los directorios
## utilisar nuestro paquete la ubicacion de la funcion omega puede ser modulo1_3_paquete.good.best.omega.omega()
## ahora como decir a Python que es un paquete
## donde poner el superarbol raiz ?
### respuesta los paquetes como los modulos pueden requerir inicializacion
### para inicializar un paquete, debes poner un archivo __init__.py (que puede ser vacia)
### el archivo __init__.py se ejecuta cada vez que se importa cualquier modulo del paquete
### se puede al igual poner el __init__.py dentro cualquiera subdirectorio (subpaquete)
### podria ser util si alguno de los subpaquete necesita un tratamiento especial o inicializacion
## ahora es tiempo de usarlo el paquete modulo1_3_paquete
## no apunta directamente en el modulo si no la ruta del paquete
## el importa no apunta directamenente al modulo si no desde la parte superior del paquete
import sys

sys.path.insert(0, "modulo_1_3_paquete")
print(sys.path)
#
import good.best.omega

print(good.best.omega.funO())

import good.best.omega as o

print(o.funO())

from good.best.omega import funO

print(funO())  ## tambien es valido el la segunda forma
## ahora vamoz intentar usar un archivo zip
## y si funciona

sys.path.insert(0, "modulo1_3_paquete2.zip")
from bad.alpha import alpha

print(alpha())

sys.path.append("prueba_paquete")

import a.alpha as a


print(a.func_alpha())
print("contador despues de importar alpha", a.get_contador())
import b.beta as b
#
print("contador despues de importar beta", a.get_contador())
print(a.func_alpha())
print("contador despues de llamar una funcion de alpha", a.get_contador())
print(b.func_beta())
print("contador despues de llamar una funcion de beta", a.get_contador())

print(sys.path)
# sys.path.remove("prueba_paquete")
# sys.path.remove("/home/frils/Documents/reviews/review-airflow/enough_python/pcap/module_1/prueba_paquete")
print(sys.path)

