# Un lenguaje es un medio (y una herramienta) para expresar y registrar pensamientos.
# Que compone un lenguaje
### alfabeto cojunto de simbolos utilizados para formar palabra e.g. alfabeto latino para el inglés
### léxico también conocido como diccionario
### sintaxis reglas utilizadas para precisar si una determinada cadena de palabras forma una orácion valida
####### soy una persona (valida)
####### yo siempre soy uno (no)
### semántica cojunto de reglas que determinan si una frase tiene sentido
####### me comí una dona (valida)
####### una dona me comió (no tiene sentidào)
# código fuente different from   código máquina (executed by computers)
# archivo fuente => file contening the source code
def print_language_definition():
    print("A language is a medium (and a tool) for expressing and recording thoughts.")
    print("What makes up a language:")
    print("Alphabet: a set of symbols used to form words (e.g. Latin alphabet for English)")
    print("Lexicon: also known as a dictionary")
    print("Syntax: rules used to determine if a certain string of words forms a valid sentence")
    print("   - I am a person (valid)")
    print("   - I always am one (invalid)")
    print("Semantics: set of rules that determine if a sentence makes sense")
    print("   - I ate a donut (valid)")
    print("   - A donut ate me (does not make sense)")


# El lenguaje debe ser interpretado o compilado.
### Intérprete
### Compilador => Compila un programa de alto nivel en código de máquina.


# python es un languaje de programacion interpretado, orientado objetos y con semantica dinamica
# su origino  proviene de la vieja serie de comedia de la BBC Monty Python's Flying Circus

# Guido Van Rossum el que creo python
# Diciembre 1989 semana de navidad, objetivo interprete descendiente de ABC para atraer los hackers de Unix/C
# en 1999 Guido Van Rossum definiciendo los objetivos de python
#### facil e intuitivo
#### codigo abierto (cualquiera pueda conctribuir a su desarrollo)
#### comprensible (como el ingles)
#### adecuado para tareas cotidianas
# python es uno de los tops segun [PYPL](https://pypl.github.io/DB.html#google_vignette) and [TIOBE](https://www.tiobe.com/tiobe-index/)

# PROS
#### facil de aprender y de enseñar
#### facil de utilizar y de entender
#### facil de obtener, instalar y desplegar
# CONS
#### no es el mejor en termino de rendimiento
#### la depuracion del codigo de python puede ser mas dificil, pero afortunadamente cometer errores es dificil

# rivales de python
#### Perl scripting escrito por Larry Wall
#### Ruby scripting escritoo  por Yukihiro Matsumoto

# utilizacion
#### motores de busqueda, almacenamiento en la nube y herramientas, redes sociales,
#### muchos cienficos han abandonado las costosas herramientas patentadas y se han cambiado a python
#### muchos testers tambien comienzan a usar python para llevar a cabo procedimientos de prueba repetibles

# todavia existen algunos nichos en los que python esta ausente o rara vez se ve :
#### programacion de bajo nivel
#### aplicaciones para dispositivos moviles

# tipos de python non compatibles entre ellos
#### python2
#### python3

# el curso sobre python3

# python alias CPython mantenido por PSF (Python Software Foundation)
#### todos los pythons que provienen del PSF estan escritos en el languaje C

# Cython
#### se usa para traducir un codigo funcional de python a c (python lento pero facil, c dificil pero rapido)

# Jython
#### python con java, para que sea efectiva la integration de python en un ambiente java
#### jython sigue los estandares de python2

# Pypy y RPython
#### un entorno de python escrito en un languaje similar a python llamado rpython (restricted python)
#### un subconjunto de python
#### es mas facil de verificar un nueva caracteristica que puede o no ser introducida en la implementacion de python
#### es mas utilizado por los desarolladores de python
#### compatible con python3

# obtener y utilizar python
#### ya esta instalado en linux debido a que muchos componentes del sistema operativo linux usan python
#### solo escribir python en el terminal
#### sale la version utilizada de python
#### [non linux user can download from here](https://www.python.org/downloads/.)
#### mac user (posiblemente ya tienen a python2, se debe decargar el archivo .pkg para usar el python3
#### windows user pueden directamente descargar el archivo .exe

# getting started
#### editor IDLE (integrated development and learning environment) (desarrollo integrado y entorno de aprendizaje)
#### consola pra poder ejecutar el codigo
#### depurador capaz de ejecutar el codigo paso a paso

# hola mundo
#### en idle, new file, save as, not required the extension on the name, it is made automatically
print("hola")

# anatomia de un error
#### rastreo (ruta que el codigo atraviesa a traves de diferentes partes del programa)
#### ubicacion del error (nombre del archivo, numero de linea con error, nombre del modulo) puede ser enganoso por que python muestra el lugar donde se percata por primera vez de los efectos del error
#### contenido de la linea erronea
#### nombre del error y una breve explicacion

