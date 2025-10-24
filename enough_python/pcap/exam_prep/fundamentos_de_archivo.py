# los archivos

# nombres
## en windows C:\directory\file
## en linux /directory/files
## windows almacenan minusculas y majusculas pero no distinguen entre ellas
## en linux si distinguen entre ellas
## en Python para windows, los nombres de archivos deben escribirse con doble diagonal invertida ya que es un caracter de escape
name = "\\dir\\file"
## python lo invierta si es necesario enconces tambien funcionara estos para windows
name = "/dir/file"
name = "c:/dir/file"

## no se comunica directamente con los archivos, sino usamos un tipo de manejadores (puntero inteligente) o
## streams o flujos (una especie de canal)
## el programador que tiene un conjunto de funciones y métodos puede realizar ciertas operaciones en el flujo o stream
## que afectan los archivos reales utilizando mecanismos contenidos en el nucleo (noyau) del sistema operativo
## de esta forma, puedes implementar el proceso de acceso a cualquier archivo, incluso cuando el nombre del archivo es
## desconocido al momento de escribir el programa

# Flujos de archivos (streams)
## open mode (modo de apertura)
## si la apertura es exitosa, el programa solo podra realizar las operaciones que sean consistentes con el modo abierto declarado
## hay dos operaciones basicas a realizar con el stream :
### lectura del stream => de archivo hacia memoria
### escritura del stream => de memoria hacia archivo
## existen 3 modos basicos utilizados para abrir un stream:
### modo lectura : permite solo operaciones de lectura, intentar escribir en la transmision provocara una excepcion
#### UnsupportedOperation, la cual proviene del modulo io y hereda de OSError y de ValueError
### modo escritura : solo permite de escribir, intentar leer provocara la excepcion UnsupportedOperation
### modo actualizar : permite tanto lectura y escritura
## cuando lees algo de un stream, un cabezal virtual se mueve sobre la transmision de acuerdo con el numero de bytes transferidos desde el stream
## al igual cuando escribes algo en el stream, el mismo cabezal se mueve a lo largo del stream registrando los datos de memoria
## los libros de programacion se refieren a este mecanismo como la posicion actual del archivo

# manejo de archivos
## Python supone que cada archivo esta oculto detras de un objeto de una clase adecuada
## los archivos se pueden procesar de muchas maneras diferentes :
### algunos dependen del contenido del archivo
### otros de las intenciones del programador
## en cualquier caso, diferentes archivos pueden requerir diferentes conjuntos de operaciones y comportarse de diferentes maneras

## un objeto de una clase adecuada es creado cuando abres el archivo y lo aniquilas (destroy) al momento de cerrarlo
## entre estos dos eventos (abrir y cerrar), puedes usar el objeto para especificar que operaciones se deben realizar en un stream
## las operaciones que puedes usar estan impuestas (determined by) por la forma en que abriste el archivo
## en general, el objeto proviene de una de las clases IOBase, RawIOBase, BufferedIOBase, TextIOBase
## nota: nunca se utiliza el constructor para dar vida a estos objetos, la unica forma de obtenerlos es invocar la funcion open()
## la funcion open() analiza los argumentos y crea automaticamente el objeto requerido
## si deseas deshacerte del objeto, invoca el metodo denominado close(), cortara la conexion con el objeto y el archivo y eliminara el objeto
## solo nos ocuparemos de los streams representados por los objetos BufferedIOBase y TextIOBase

## debido al tipo de contenido de los flujos o streams, se dividen en tipo texto y binario
### los flujos de texto estan estructurados en lineas, es decir contiene caracteres tipograficos (letras, digitos, signo de puntuacion, ...
#### dispuestos en filas (lineas), como se ve a simple vista cuando se mira el contenido del archivo en el editor
#### este tipo de archivo es escrito (o leido) principalmente caracter por caracter, o linea por linea
### los flujos binarios no contienen texto, sino una secuencia de bytes de cualquier valor. esta secuencia puede ser
#### por ejemplo un programa ejecutable, una imagen, un audio o un videoclip, un archivo de base de datos, ...
#### debido a que estos archivos no contienen lineas, las lecturas y escrituras se relacionan con porciones de datos de cualquier tamano
#### por lo tanto, los datos se leen y escriben byte a byte, bloque a bloque, donde el tamano del bloque generalmente varia de uno
#### a un valor elegido arbitrariamente

## ahora viene un problema, en unix/linux, los extremos de la linea estan marcados por un solo caracter llamado LF (ascii 10)
### designado en los programas de Python como \n
## en los sistemas operativos derivado del prehistorico CP/M (tambien aplica para windows), el final dos caracteres
### CRyLF (ascii 14 y 10) los cuales se pueden codificar como \r\n
## esta ambiguedad puede causar varias  consecuencias desagradables

## si escribas un programa responsable de procesar un archivo de texto para windows, puedes encontrar CRLF pero
## si el mismo programa se ejecuta en un entorno linux, sera completamente inutil, y viceversa
## estas caracteristicas indeseables del programa que impiden o dificultan el uso del programa en diferentes entorno es la falta de portabilidad
## de mismo modo, el programa que permite la ejecucion en diferentes entornos se llama portabilidad
## un programa dotado de tal rasgo se llaman programa portable

## dado que los problemas de portabilidad eran (y siguen siendo) muy graves, se tomo la decision de resolver definitivamente
## el problema de una manera que no atraiga la atencion del desarrollador
## se realizo a nivel de clases, que son responsables de leer y escribir caracteres hacia y desde el stream
### cuando el stream esta abierto y se recomienda que los datos en el archivo asociado se procesen como texto (o no existe tal aviso)
#### se cambia el modo texto
### durante la lectura y escritura de lineas desde y hacia el archivo asociado, no occure nada especial en el entorno unix,
### pero cuando se realizan las mismas operaciones en el entorno windows, un proceso llamado traducioccion de caracteres de nueva linea occure :
#### cuando lees una linea del archivo, cada par de caracteres \r\n se reemplaza con un solo caracter \n y viceversa
#### durante la operacion de escritura, cada caracter \n se reemplaza con un par de caracteres \r\n
### el mecanismo es completamente transparente para el programa,
### cuando el stream esta abierto, su contenido se toma tal cual es, sin ninguna conversion, no se agregan ni se omiten bytes

# abriendo los flujos o streams
# name = "modulo4.py"
# stream = open(file=name, mode="r", encoding=None)  # FileNotFoundError si el archivo no existe
# stream.close()
## se pueden omitir el argumento mode y encoding, por defecto mode es read 'r' y encoding depende de la plataforma
## modos de apertura :
### "r" lecutra, el archivo debe existir
### "w" escritura (se borra)
### "a" adjuntar (append)
### "r+" lectura y actualizacion, el archivo debe existir
### "w+" escritura y actualizacion

# seleccion de los modos de texto y binario
## si hay una letra b al final de la cadena del modo significa que el stream se debe abrir en el modo binario
## si la cadena del modo termina ocn la letra t, el stream es abierto en modo texto
## el modo texto es el comportamiento predeterminado que se utiliza cuando no es especifica ya sea modo binario o texto
## la apertura del archivo establecera la posicion actual del archivo (cabezal virtual de lectura/escritura)
### antes del primer byte del archivo si el modo no es a, y despues del ultimo byte del archivo si el modo es a
### "rt" , "rb"
### "wt", "wb"
### "at", "ab"
### "r+t", "r+b"
### "w+t", "w+b"
### tambien puedes abrir un archivo para su creacion exclusiva, modo de apertura "x", si existe genera una excepcion

# abriendo flujos
try:
    stream = open(file=name, mode="rt")
    stream.close()
except Exception as e:
    print("No se pudo abrir el archivo", e)

# flujos o streams pre-abiertos
## dijimos que antes de cualquier operacion del stream, se debe de abirlo con la funcion open()
## hay 3 exepciones a esta regla,
## cuando comienza nuestro programa, los tres streams ya estan abiertos y no requieren ninguna preparacion adicional
## ademas, tu programa puede usar estos streams explicitamente si tienes cuidado de importar el modulo sys
## los 3 streams son sys.stdin, sys.stdout, sys.stderr
### sys.stdin normalmente se asocia con el teclado, input() lee los datos de stdin por default
### sys.stdout normalmente asociada con la pantalla, print() envia los datos al stream stdout por default
### sys.stderr pantalla, preabierta para escribir errores (pero separado de stdout)
import sys

# sys.stdout.write("Hola mundo\n")
# sys.stderr.write("Hola baba\n")

# cerandos los flujos
## con la funcion close(), sin argumento, IOError en caso de un error y no regresa nada si exitoso
## close() puede fallar ya que no es en tiempo real, pasa por cache o buffer, luego al cerrar, obliga a descargar el contenido
## por lo tanto puede fallar el close()

# diagnosticando problemas con los flujos
## el objeto IOError esta equipado con una propriedad llamada errno (error number)
try:
    stream = open(file="name", mode="rt")
    stream.close()
except IOError as e:
    print("Error al abrir el archivo", e)
    print("Error number", e.errno)

## las constantes simbolicas en modulo errno
## errno.EACCES permiso denegado : cuando se intenta escribir a un archivo abierto con lectura
## errno.EBADF numero de archivo incorrecto : operar un stream sin abrirlo
## errno.EEXIST archivo existente : cambiar nombre de un archivo con su nombre anterior
## errno.EFBIG archivo demasiado grande : crear archivo mas grande que el maximo permitido por el sistema operativo
## errno.EISDIR es un directorio : intenta tratar un nombre de un directorio como si fuera un archivo ordinario
## errno.EMFILE demasiados archivos abiertos : mas streams de los aceptables para el sistema operativo
## errno.ENOENT el archivo o directorio no existe : intenta acceder a un archivo o directorio no existente
## errno.ENOSPC : no queda espacion en el dispositivo : no hay espacion libre en el dispositivo
## la lista completa es mucho mas larga, incluye tambien algunos codigos de error no relacionados con el procesamiento de los streams
import errno

try:
    stream = open(file="name", mode="rt")
    stream.close()
except Exception as e:
    if e.errno == errno.ENOENT:
        print("El archivo no existe")
    elif e.errno == errno.EACCES:
        print("No tienes permiso para acceder al archivo")
    elif e.errno == errno.EISDIR:
        print("El archivo es un directorio")  ####" y sigue
    else:
        print("Error desconocido", e)

## afortunadamente, existe una funcion que puede simplificar el codigo de manejo de errores strerror() proviene del modulo os
## y espera solo un argumento nomero de error
## la funcion genera un ValueError si pasas un numero que no esta vinculado a ningun error real
try:
    stream = open(file="name", mode="rt")
    stream.close()
except Exception as e:
    print("Error al abrir el archivo", e, "Error:", errno.errorcode[e.errno])
    print("Error number", e.errno)
    import os

    print("Error:", os.strerror(e.errno))

# resumen
# import errno para tener el errorcode
# errno.errorcode[e.errno]    # e es la excepcion cacheada
## mas detalles con strerror
## from os import strerror
## strerror(e.errno)

