# modulo os
import os, platform

## os.uname() informacion sobre el sistema operativo unix
## platform.uname() algo parecido en windows
print(
    os.uname())  ## posix.uname_result(sysname='Linux', nodename='dev-workstation-01', release='6.8.0-84-generic', version='#84-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  5 22:36:38 UTC 2025', machine='x86_64')
print(
    platform.uname())  ## uname_result(system='Linux', node='dev-workstation-01', release='6.8.0-84-generic', version='#84-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  5 22:36:38 UTC 2025', machine='x86_64')
## os.name
print(os.name)  # posix (unix), nt (windows), java si el codigo esta escrito en Jython
print(platform.system())  # Linux

# creando directorio en Python
## requiere una ruta que puede ser absoluto o relativo
ruta = "/home/usuario/directorio_nuevo"  # una ruta absoluto
ruta = "directorio_nuevo"  # en el espacio de trabajo actual
ruta = "../directorio_nuevo"  # esto es una ruta en el directorio superior del espacio de trabajo actual
ruta = "./directorio_nuevo"  # igual que el precedente relativo tambien

import os

## ejecutarlo dos veces genera un FileExistsError
## BaseException <- Exception <- OSError <- FileExistError
# os.mkdir(ruta)  ## se ha creado el directorio
## pueda tener argumento pero en algunos sistemas operativos se ignora el argumento que cambia los permisos al directorio
## entonces mejor modificarlo con el comando chmod
print(FileExistsError.__bases__)

print("current working dir", os.getcwd())
## os.listdir() regresa un arreglo que contiene los directorios y archivos dentro del
## puede igual tener argumento, la ruta que quiere imprimir su contenido
## si no se pasa un argumento, va imprimir el espacio de trabajo actual en el que esta corriendo el codigo
print("parent list_dir", os.listdir("../"))

# creacion recursiva de directorios os.makedirs()
ruta = "./directorio_nuevo/directorio_nuevo2"
# os.makedirs(ruta)
print("current_list_dir", os.listdir("./"))
# os.chdir("./directorio_nuevo")

print("current working dir", os.getcwd())
print(os.listdir("./"))

## equivalente de esto en linux mkdir -p [ruta]
## su equivalencia en windows es mkdir [ruta]

# getcwd() su equivalente en linux ex pwd

# eliminando directorios en Python os.rmdir()
os.chdir("../")
# os.rmdir("./directorio_nuevo")
# os.rmdir(ruta)  ## FileNotFoundEror cuando no existe el directorio
## aqui son 2 niveles de directorios, va solamente borrar el ultimo nivel
## OSError cuando el directorio no es vacio
## tendramos que primero borrar los contenidos
## os.rmdir("./directorio_nuevo")
print(FileNotFoundError.__bases__)

## BaseException <- Exception <- OSError <- FileNotFoundError

# os.removedirs()
print(os.makedirs("./directorio_nuevo/directorio_nuevo3"))
os.removedirs("./directorio_nuevo/directorio_nuevo3")

## en linux, rm -r [ruta] (recursivo) o rmdir -p [ruta]
## con rm solo borra el ultimo directorio al contrario de rmdir -p bora todo la ruta dada en argumento

# la funcion os.system()
## en windows devuelve el valor devuelto por el shell despues de ejecutar el comando dado
## en linux devuelve el estado de la salida del proceso
import os

returned = os.system("ls -l")
print(returned)
print("--------------------------")
r = os.system("mkdir directorio_nuevo")
print(r)
r = os.system("rmdir directorio_nuevo")
print(r)

try:
    os.makedirs("tree/c/other_courses/cpp")
    os.makedirs("tree/c/other_courses/python")
    os.makedirs("tree/cpp/other_courses/c")
    os.makedirs("tree/cpp/other_courses/python")
    os.makedirs("tree/python/other_courses/c")
    os.makedirs("tree/python/other_courses/cpp")
except FileExistsError as e:
    print(e)


def build_directory(path, directory):
    if not path.endswith("/"):
        return path + "/" + directory
    return path + directory


def find_matched(start_path, directory_name):
    found = []

    def find(path):
        for directory in os.listdir(path):
            new_path = build_directory(path, directory)
            if directory == directory_name:
                found.append(new_path)
            find(new_path)

    find(start_path)

    return found


for i in find_matched("tree", "cpp"):
    print(i)

# resumen
# os.uname()
## devuelve informacion sobre el systema operativo
### systemname nombre del sistema operativo
### nodename nombre de la maquina en la red
### release actualizacion del sistema
### version la version del sistema operativo
### almacena el identificador de hardware por ejemplo x86_64
print(os.uname())

# atributo name os.name
## regresa el sistema operativo
print(os.name)
## posix, nt o java
print(os.listdir(
    "."))  ## os.listdir() omite current and parent not the same as for ls -a que si imprime current y parent and then the other directories
