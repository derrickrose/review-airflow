# modulo platform
from platform import platform

print(platform())  # Linux-6.8.0-85-generic-x86_64-with-glibc2.39
print(platform(aliased=True))  # if the name is different to common name o cualquier valor distinto a cero
print(platform(terse=True))  # show minimum information about igual aqui
print(platform(True, True))
import platform

print(platform.machine())  # nombre generico del processador x86_64
print(platform.processor())  # nombre real del processador x86_64
print(platform.system())  # Linux
print(platform.version())  # version del sistema operativo

### la version de python que utilize
print(platform.python_implementation())  # CPython
print("tup", platform.python_version_tuple())  # ('3','12','3')
print(type(platform.python_version_tuple()[0]))
print(platform.python_version())  # 3.12.3
print(type(platform.python_version()))
print("branch", platform.python_branch())
print("compiler", platform.python_compiler())  # compiler GCC 13.3.0
print("build", platform.python_build())  # build ('main', 'Aug 14 2025 17:47:21')
print("revision", platform.python_revision())

### los modulos de python aqui https://docs.python.org/3/py-modindex.html

# modulo math tiene 50 funciones y constances
# modulo random tiene 60 entidades
# modulo platform tiene 70 funciones

# pregunta
# habra manera de saber que si es un constante o una funcion lo que devuelve el dir()
## preguntando eso puede guiarse con saber como identificar una clase, funcion, ...
