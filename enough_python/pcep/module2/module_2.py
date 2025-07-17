# module 2
## note cadena string
print("¡Hola, Mundo!")
### print es nombre de una funcion

# funcion
### causar algun efecto ejemplo enviar texto a la terminal, crear archivo, dibujar una imagen, reproducir sonido ...
### evaluar un valor (ejemplo raiz cuadrada de un valor o la longitud de un texto dado)
### devolver como el resultado de la funcion

# donde vienen
### puenden venir de python mismo (integrada)
### pueden provenir de uno o varios modulos de python llamados complementos, algunos de los modulos vienen con python, otros pueden requerir una instalacion por separado
### puedes escribirlas tu mismo
### no se puede modificar funciones que ya existen, asi que deberia eligir cuidadosamente el nombre de una funcion

# argumentos
### una funcion puede tener afecto y resultado
### pero el tercer componente es argumento
### ejemplo la funcion matematica seno(x) toma argumento x
### algunas funciones de python no necesitan argumento
### a pesar del numero de argumentos necesarios o proporcionados, las funciones de python demandan fuertemente la presencia de un par de parentesis el de apertura y de cierre
### para distinguir una funcion, colocar un par de parentesis vacios despues de sus nombres, incluso si la funcion requiere uno o mas argumentos
### la function aqui es print()
### el unico argumento entregado a la funcion print() en este ejemplo es una cadena (string)
### las comillas son parte de la cadena y podria significar asi que el texto entre nosotros no es un codigo (no es disenado para ser ejecutado)

# invocacion (semantica)
### el nombre de la funcion (print en este caso) junto con los parentesis y los argumentos, forman la invocacion de la funcion
### que sucede si python encuentra una invocacion como esta nombre_funcion(argumento)
#### comprueba si el nombre especificado es legal (explora sus datos para encontrar una funcion existente del nombre cancela si no)
#### comprueba si los requisitos de la funcion para el numero de argumentos le permiten invocal la dicha funcion
#### python deja el codigo por un momento y salta dentro de la funcin que se desea invocar, toma los argumentos y los pasa a la funcion
#### la funcion ejecuta el codigo, provoca el efecto deseado , evalua los resultados deseados y termina la tarea
#### finalmente python regresa al codigo (al lugar inmediatamente despues de la invocacion) y reanuda su ejecucion
# print(my name) sin comillas SyntaxError
# print"my name" sin parentesis SyntaxError
# print('my name') print('my name') 2 invocaciones en mismo linea SyntaxError
# print("my name') SyntaxError
# print ("my name" SyntaxError
d = ("aaa"
     "nnn"
     "ccc")
print(d)
print()
print(print("a"))  # => print None
print("a", "b", "c")  # =>  print a b c
print("a" "b"
      "c")  # => print abc

# efecto de la funcion print (3 efectos)
### toma los argumentos (puede aceptar mas de un argumento o menos de un argumento
### los convierte en un formato legible para ser humano si es necesario
### envia los datos resultantes al dispositivo de salida (generalmente la consola)

# respuesta
### cualquiera, que sear numero, caracteres, valores logicos, objetos

# que valor evalua la funcion print()
### ninguno, su efecto es suficiente, print() no evalua nada

# instrucciones
#### la invocacion de function es uno de los muchos tipos de instrucciones de Python
#### una sola instruccion por linea
#### una instruccion puede ser multi-linea
#### cada invocacion de print empieza en nueva linea (comportamiento que puede cambiar)
#### orden de ejecucion es mismo que el de codigo fuente
#### una invocacion de la funcion print() con una cadena (string) vacia genera una linea vacia

# la funcion print() los caracteres de escape y nueva linea
#### barra invertida \n (caracter de nueva linea)
#### la barra invertida \ tiene un significado como anuncio cuando de usa dentro de las cadenas (strings) llamado el caracter de escape
print("hola\n mundo")
#### si deseas colocar una barra invetida dentro de una cadena, por su naturaleza de escape, habra que duplicarla
print("hola\t mundo")
#### no todos los pares de escape (barra o diagonal invertida junto con otro caracter) significan algo
print("\i")

# la funcion print() utilizando variables multiples
print("hola", "mundo", "estoy", "bien")
#### nota: se borro los espacios
#### la functon print() invoca con mas de un argumento genera la salida en una sola linea
#### la funcion print() coloca un espacio entre los argumentos emitidos por iniciativa propria

# la funcion print() la manera posicional de pasar argumentos
#### deberias predecir la salida sin ejecutar el codigo en el editor
#### la forma en que pasamos los argumentos a la funcion print() es la mas comun de python y se denomina manera posicional
print("mi nombre es", "Python.", end=" ")
print("Monty Python.")

# la funcion print() la manera de pasar argumentos por palabra clave
print("Mi nombre es, ", end="")
print("Monty Python.", )
print("hola")
### vimos que print() separa los argumentos por espacio, ese tambien se puede cambiar
print("mi", "nombre", "es", "Pablo", sep="-")  # ahora es un guion en lugar de espacio
print("mi", "nombre", "es", "Pablo", sep="")
### ejemplo
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
### Mi_nombre_es*Monty*Python.*
print("    *" * 2)
print("   * *" * 2)
print("  *   *" * 2)
print(" *     *" * 2)
print("***   ***" * 2)
print("  *   *" * 2)
print("  *   *" * 2)
print("  *****" * 2)

# puntos claves
#### print() es una funcion integrada (disponible y no tiene que ser importada)
####  python viene con 69 funciones integradas, podemos verlo en [Python Standard Library](https://docs.python.org/3/library/functions.html)
#### para llamar a una funcion (invocacion), debe utilizarse el nombre seguido de un parentesis, puede pasar argumentos, una funcion print vacia imprime una linea vacia
####  las cadenas de python son delimitadas por comillas "eaaaa" o 'a,nbiii'
####  los programas de computadora son colecciones de instrucciones
####  en la cadenas, la barra diagonal inversa \ es un caracter especial que anuncia que el siguiente caracter tiene un significado diferente e.j. \n
####  los argumentos posicionales son aquellos cuyo significado viene dictado por su posicion
####  los argumentos de palabra clave son aquellos cuyo significado no esta dictado por su ubicacion, si no por una palabra especial (palabra clave)
####  los parametros end y sep se pueden usar para dar formato la salida de la funcion print()

# literales los datos en si mismos
### 123 es literal por que se puede imaginar cual es el valor
### c no se puede, requiere informacion adicional, podria ser la veloz de la luz, ...
### se utilizan literales por codificar datos y ponerlos dentro del cotigo
### dos tipos de literales :
#### una cadena
print("123")
#### un numero entero
print(123)
print(3 ** 2)  # sqrt
#### la funcion print los imprime de la misma manera sin embargo la memoria de la computadora los almanece de dos manera diferentes, la cadena existe como una serie de letras tal cual
#### el numero es convertido a una representacion maquina (una serie de bits)
#### vamos hablar de literales numericas y su vida interna

# enteros
### todos los numeros manejados por las compu modernas son de dos tipos :
#### enteros, aquellos que no tienen una parte fraccionaria
#### numeros punto-flotantes (o simplemente flotantes), los cuales contienen (o son capaz de contener) una parte fraccionaria
#### ambos tipos difieren significativamente en como son almacenados en una computadora y en el rango de valores que aceptan
#### la caracteristica del valor numerico que determina el tipo, rango y aplicacion se denomina tipo
#### si se codifica un literal y se coloca dentro del codigo python, la forma del literal determina la representacion (tipo) que Python utilizara para almacenarlo en la memoria
#### como escribirlo, en python 11111111 o 11_111_111 para ser mas facil de leer (a partir de python 3.6)
#### numero negativo, solo colocar el signo negativo adelante ,e.j. -11 -11_000
#### los signos positivos no son necesarios pero si se permite e.j. 10 o +10

# enteros numero octales y hexadecimales
### un numero precedido de 0o (zero-o) para decir que es un numero de base octal
print(0o111)
print(0b101101)
### la funcion print() realiza automaticamente la conversion
### la funcion print() acepta los valores hexadecimales tambien
print(0x111)

# flotantes
# para almanecer numero que tiene parte decimal (fraccionaria) no vacia
# e.j. dos y medio o menos cero punto cuatro se consideran numero punto-flotante o solamente flotante se dice
2.5
-0.4
# ojo si el indioma usa coma para parte flotante, python puede no entender o mal interpretar
print(1.5)
print(1, 5)  # va imprimir 1espacio5 asi la parte decimal de un flotante tiene que ser con punto
print(.4)  # si cero es el unico digito antes del punto se puede omitir
print(4.)  # igual por 4.0
# el punto decimal es esencialmente importante para reconocer numeros punto-flotantes en Python
# 4 y 4.0 son complentamente distintos, 4 es un numero entero mientras que 4.0 es punto-flotante

# se puede utilizar la letra e para decir que es un numero flotante no solamente el punto decimal
print(1e1)  # para decir 1*10^1
print(2e2)  # deberia ser 200.0

# ejemplo la velocidad de la luz 300000000 la abreviacion 3 * 10^8
# 3 por diez a la octava potencia
print(3E8)
print(1e10)  # no se puede con solo e10
# el exponente (valor despues de e debe ser un valor entero)
# la base (el valor antes de la e) puede o no ser un valor entero
print(3E8)
print(3.00E8)

# codificando flotantes
# almanecer numero que son muy pequenos (en el sentido que son muy cerca de cero)
# la constante de planck denotada como h
# 6.62607 x 10^-34
# python no necesariamente codifica los numeros igual aquel que los has codificado
print(6.62607e-34)
# python siempre va imprimir la manera mas corto de escribir un numero
print(0.000000000000000000000000000000000000000000001)  # python imprime 1e-45

# cadenas
# las cadenas se escribe dentro de unas comillas
# querer imprimir Me gusta "Monty Python"
print("Me gusta \"Monty Python\"")  # con diagonal invertida para escapar
print('Me gusta "Monty Python"')  # utilizando apostrofe para no utilizar escape

# codificando cadenas
# con comillas ""
# con apostrofe ''
# una cadena vacia sigue siendo una cadena

# booleanos
# para representar la veracidad
# el nombre proviene de George Boole (1815-1864) autor de las leyes del pensamiento
# las cuales definen el Algebra booleana, una parte del algebra que hace uso de dos valores:
# verdadero y falso, denotados como 1 y 0
# afortunadamente las computadoras solo conocen dos tipos de respuestas :
# SI
# NO
# nunca habra respuesta como probablemente si, pero no estoy seguro
# esos valores son denotados True y False
print(True > False)
print(False > True)

# ejercicio
# en una linea para representar
# "Estoy"
# ""aprendiendo""
# """Python"""
print('"Estoy"', '""aprendiendo""', '"""Python"""', sep="\n")

# otro literal es el None un objeto de NonType y puede ser utilizado para representar
# la ausencia de un valor
print(None)
print(1)
print("a")
print(2 + 2)

# operadores basicos
print(1 + 1)
print(0 - 1)
print(2 * 3)
print(4 ** 2)  # 4 puissance 2
print(4 % 2)  # entier reste de la division de 4 par 2, operador residuio o modulo
print(4 / 2)
print(9 // 2)  # division entera de 9 par 2 (2*4=8 donc 4) (floor division)
# cuando los datos y operadores se unen, forman juntos expresones
# la expresion mas sencilla es el literal
print(0.1 ** 2)  # cuando almenos uno de los argumentos son flotantes, el resultado es flotante
# exception a la regla, por un division, siempre el resultado es flotante
print(9 / 2)
print(9.0 // 2)  # le resultat sera 4.0 siempre redondeo hacia abajo valor entero
print(-6 // 4)  # resultat -2
print(6. // -4)  # resultat -2.0
# operador modulo
print(12 % 4.5)  # resultado 3.0
# zero division not working
# operador de suma
print(-4 + 4)  # 0
print(-4. + 8)  # 4.0
# operador de resta (signo de menos)
# izquierdo minuendo y sustraendo es en la derecha
print(-4 - 4)  # -8 operador unario si espera un solo valor , binario si espera 2
print(4. - 8)  # -4.0
print(-1.1)  # -1.1
# operadores y sus prioridades
# las multiplicaciones preceden a las sumas
# la jerarquia de prioridades
# operadores y sus enlaces, el operador tiene un enlanzado del lado derecho,
# significa que va primero 9%6 = 3 % 2 = 1
print(9 % 6 % 2)
# pero hay una excepcion por el operador de exponenciacion utiliza enlazado del lado derecho a izquierdo
print(3 ** 2 ** 1)  # 9
print(2 ** 2 ** 3)  # 256
# prioridad mas alta hacia mas baja
# +,- unario
# **
# *, /, //, %
# +,- binario
# operadores y parentesis
# se puede usar y tambien los calculos dentro de un parentesis siempre pasan primeros
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print(5.0 % 2)
# modulo suit toujours le signe du diviseur
print(-2. % 4)

# variables
# compopentes de un variable nombre y valor
# case sensitive
# caracteres latinos
# tambien caracteres de otros indiomas
tenté = 10
print(tenté)
# no pueden empezar con numero
# 1dol = 10  error
# tasa blanco = "blanco"  # error por que trae un espacio
dol1 = 10

# nombre correcto de variables
my_variable = 10
# palabras clave o mejor dicho reservadas no se deben utilizar
valores = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
           'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
           'pass',
           'raise', 'return', 'try', 'while', 'with', 'yield']
# for i in valores:
#     print(i)

# creando variables
# en python no es necesario declarar, se crea cuando se asigna un valor
var = 1
print(var)

# utilizando variables
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

# combinar
print("hola " + "mundo")

# asignar un valor nuevo
var = 1
print(var)
var += 1
print(var)

# resolviendo problemas matematicos simples
# El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los dos catetos.
# la raiz cuadrada es igual a potencia mitad (0.5)
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
# no se puede sumar cadena con entero
# print("total de manzana" + 3) ==> error TypeError can only concatenate str (not "int") to str
print("total de manzana", 3)

# operatores abreviados
x = 2
x = x * 2
print(x)
x = 2
x *= 2
print(x)
# i = i + 2 * j ⇒ i += 2 * j
# var = var / 2 ⇒ var /= 2
# rem = rem % 10 ⇒ rem %= 10
# j = j - (i + var + rem) ⇒ j -= (i + var + rem)
# x = x ** 2 ⇒ x **= 2

# puntos clave
# una variable es una ubucacion nombrada reservada para almacenar valores en la memoria
# cada variable debe de tener un numbro unico, comienza con letra on guillon bajo y no ser reservada de python
# tambien se puede usar operadores de asignacion compuesta (operadores abreviados)
a = 6
b = 3
a /= 2 * b
print(a)

# poner comentarios
# Un texto insertado en el programa el cual es, omitido en la ejecución, es denominado un comentario.

# funcion input()
# print(input("ingresa una cadena"))
# # el resultado de input es una cadena
# anything = input("Inserta un número: ")
# something = anything ** 2.06
# print(anything, "al cuadrado es", something) # error TypeError

# conversion de datos
# int()
# float()

# operadores de cadenas
# concatenacion
a = "hola"
b = "mundo"
print(a, b)
# replication
a = "bestie"
b = a * 2
c = 2 * a
print(b)
print(c)
print(2 * "ll")
print(0 * "l")
print("valor es |", (0 * "l"), "| ")  # with 2 separator so 0*var = empty var
print("valor es |", (-1 * "l"), "| ")  # with 2 separator so -1 *var = empty var
# para crear un rectangulo
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# conversion de tipos de datos
# leg_a = float(input("Inserta la longitud del primer cateto: "))
# leg_b = float(input("Inserta la longitud del segundo cateto: "))
leg_a = 10.5
leg_b = 2.5
print("La longitud de la hipotenusa es " + str((leg_a ** 2 + leg_b ** 2) ** .5))

# review
# % modulo reste de la division
# // el divizion entera
