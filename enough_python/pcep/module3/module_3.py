## operador de igualdad ==
# = es un operador de asignacion
# == es un operador de igualdad, a==b compara a y b (operador binario con enlazado izquierdo)
# True si es correcto and False a caso que no
var = 0
print(var == 0)  # True
var = 0  # asignando 0 a var
print(var == 0)  # True

var = 1  # asignando 1 a var
print(var == 0)  # False

# desigualdad != (no es igual a)
var = 0
print(var != 0)
print(var != .0)

# comparacion mayor que
# 10 > 5

## mayor o igual que
# 10 >= 3

# menor o igual que
# 0<=1

## que hacer despues de una comparacion
### almacenar
### tomar una decision

## condiciones y ejecucion condicional
# e.g.
# sangria = indentation

# ejecucion conditional, la sentencia  if
the_weather_is_good = True
if the_weather_is_good:
    print("good")
sheep_counter = 120
if sheep_counter >= 120:
    print("sleep_and_dream")
# go for a walk
# 'have lunch()
var = True
if var:
    print("true")
else:
    print("false")
# zero es evaluado a false
var = 0
if var:
    print("true")
else:
    print("false")
var = -1
if var:
    print("true")
else:
    print("false")

# la sentencia if-else
val = 0
if val:
    print("val")
else:
    print("no val")
print("val", val)

# la sentencia if-else anidadas (nested)
# this is known as nesting anidamiento
# if weather_is_good:
#   if nice_restaurant_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else if_tickets_are_available:
#     go_to_theater()
# else:
#     go_shopping

# la sentencia elif
# this is named cascade cascada
var = 10
if var > 5:
    print("var is greater than 5")
elif var == 5:
    print("var is equal to 5")
else:
    print("var is less than 5")
# puede escribir en una sola linea por si es una sola instruccion
if var > 5: print("var is greater than 5")
else: print("var no es greater than 5")

# pseudocodigo y introduccion a los bucles (ciclos)
# bucle : ejecucion de uuna parte de codigo varias veces
# shortcut atajo
x = "1"

if x == 1:
    print("uno")
else:
    print("else")

x = 1
if x == 1.:
    print("ehe igual")

# bucles (ciclos) en el codigo con while
# mientras hay algo que hacer
#   hazlo
# while condicion_expression :
#   instruccion
# cuerpo del bucle son las instrucciones dentro del bucle
# para salir de un bucle infinito presiona CTRL + C => KeyboardInterrupt error
# while True:
#     print("print")

# usar un counter para salir del bucle
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

### string can be with 3 quotes
x = """
hola 
carray

"""
print(x)

# bucle con for
# objetivo contar los giros o vueltas del bucle
i = 0
while i < 10:
    print(i)
    i += 1
# usando el nuevo bucle for
# usando for no se requiere el conteo, el se lo hace internamente, tampoco los condiciones
# randge empieza con zero y termina un paso (un numero entero) antes del valor de su argumento
for i in range(10):
    print("con bucle for", i)
for i in range(10, 0, -2):
    print("con bucle for a 2 incrementos ", i)
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

# break y continue
# a veces se denominan dulces sintacticos o azucar sintacticos
# estas dos instrucciones son : break y continue
# break sale del bucle inmediatamente
# continue salta el giro actual, como si fuera que el programa a llegado al ultimo instruccion sin ejecutarlos y continua con el siguiente giro
# break - ejemplo
print()
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# el bucle while y la rama else
# la rama else de un bucle while siempre va a ser ejecutada
# while tambien tiene una rama else
# este va imprimir 5 por que el estado de while es falso (False) al principio
print("totoatotoatotoatotoatotoatotoa")
totoa = 5
while totoa < 5:
    print(totoa)
    totoa += 1
else:
    print("else", totoa)
# ahora si i = 1
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else", i)

# bucle for y la rama else
# nota que i mantiene sur ultimo valor asignado
for i in range(5):
    print(i)
else:
    print("else", i)

## nota si el bucle no se ejecuta, la varibale mantene su ultimo valor
# aqui el bucle no se ejecuta por que el valor del empezamiento es mas que el valor de terminacion
# entonces error NameError por que no esta definido
ll = 45
for ll in range(2, 1):
    print(ll)
else:
    print("else:", ll)
# VERY IMPORTANT only brake make the else not run
# checando altura de piramide
blocks = 15
height = 0
current_level_used_blocks = 0
used_blocks = 0
while used_blocks < blocks:
    if (used_blocks + current_level_used_blocks) >= blocks:
        break
    height += 1
    current_level_used_blocks += 1
    used_blocks += current_level_used_blocks
print("La altura de la pirámide:", height)
# notas : ser muy pendientes en las preguntas

# logica de computadora operadores logicos
# conjuncion and
# or disyuncion
# es un operador binaro con una prioridad inferior a la expresada por los operadores de comparacion
# and : A False and B True , A and B => False (logica)
# or : un operador de disyuncion con un prioridad mas baja que and
# or : A False or B True , A or B => True
# not operador unario que realiza una negacion logica, convierte la verdad en falso y lo falso en verdad, de prioridad muy alta
print(var > 0)
print(not (var <= 0))
print(var != 0)
print(not (var == 0))

# leyes de Morgan dicen que
# la negacion de una conjuncion es la separacion de las negaciones
# la negacion de una disyuncion es la conjuncion de las negaciones
# not(p and q) == (not p) or (not q)
# not(p or q)  == (not p) and (not q)

# valores logicos frente a bits individuales
# no toman por bits si no que todo de una vez
# el resultado es False o True
# cero cuando todos los bits se restablecen False
# no cero cuando se establece al menos un bit True
i = 1
print("i=1")
print("not i", not i)  # false
j = not not i
print("not not i", j)  # True

# operadores bit a bit
# hay cuatros operadores bit a bit
# & and ampersand conjucion a nivel de bit
# | or barra vertical disyucion a nivel de bit
# ^ xor signo de intercalacion o exclusiva a nivel de bit, al menos uno es correcto y solamente uno
# ~ not tilde negacion a nivel de bits
# A 0  , B 0  a nivel de bit  A & B = 0  ; A | B  = 0 ; A ^ B = 0
# A 0 , B 1 a nivel de bit A & B = 0; A | B = 1 ; A ^ B = 1
# todo debe ser entero no podemos usar flotantes
a = 0b1
b = ~a
print("negation de 0b1 uno baso binario es ~a", b)  # -2 TODO check why it is weird
a = 0b1 ^ 0b0
print(a)  # 1

# operaciones logicas frenta a operciones de bit continuacion
i = 15  # 0b00000000000000000000000000001111
j = 22  # 0b00000000000000000000000000010110
# 0b00000000000000000000000000001111
# 0b00000000000000000000000000010110
# dernier bits por i 0 ~ 1 por j = 0
# avant dernier bits por i 1 ~ 1 tambien por j = 1 , y asi sucesivamente
# asi el resultado es
# 0b00000000000000000000000000000110
# para traducirle en decimal :
# ultimo bits : 0 *2**0
# penultimo : 1 * 2**1 == 1*2 == 2
# antepenultimo : 1 * 2 ** 2 = 1 * 4 =4
# asumir todos 1+2+4 = 6
print("i and j", i and j)  # True
print("i & j ", "binario", i & j)  # va operar uno por uno a los bits # valor 6 como el calculo arriba

# para calcular la inversion binario de un numero binario firmado
# invertir los bits
# si el numero empieza con 1 asi es negativo, entonces proceder al calculo de complemento 2
# primer paso invertir todos los digitos otravez, luego asumarle 1

# por los numeros negativos
# checar el numero positivo primero (representacion en binario del numero positivo)
# luego aplicar la calcula en complemento 2 para verificar su representacion negativo
## eso es en 2 paso
## paso 1 es invertir los digitos
## segundo paso es anadir 1 a la mas derecha
## ya teniendo este numero negativo
## el ultimo paso es aplicar el operador de invertimiento de bits
# TODO ojo aqui, cada vez que se encuentra un numero negativo, para saber su valor es seguir esos 2 pasos de calculo complemento 2
print(~-18)  # 17
# TODO relire https://edube.org/learn/python-essentials-1-esp-edube/operaciones-l-oacute-gicas-y-de-bits-en-python-2
x = True
y = 2
x = x or y
print(x)
## podemos abreviar los operadores de bits
x = 0
y = 1
x = x & y
print(x)
x = 0
y = 1
# forma abreviada , in english augmented operator
x &= y
print(x)

# tratar los bits individuales
# given a 32 bits variable
# I just have the third one (it counts from zero at the most right )
# use it to compare the value of the bit in position x for example
# we cannot compare with the all bits because the other value are unpredictable
# what I do instead is compare the bit with zero and 1
# then the value at third position is 2**3 = 8
flag_register = 0x1234
# 0000000000000000000000000000x000
# so the mask here is 8
# 00000000000000000000000000001000
# because its compare bit for bit
# so we can do the following condition
the_mask = 8
if flag_register & the_mask:
    print("value of my bit es uno")
else:
    print("value of my bit es zero")
# reiniciar my bit
# usaremos misma condicion
# ~the mask will make all bits to 1 except my bit
# with & it will always be zero
# usamos la misma conjucion
# reiniciar mi bit (put it to zero)
flag_register = flag_register & ~the_mask
print(flag_register)
flag_register &= ~the_mask
print(flag_register)
# restablecer mi bit
flag_register = flag_register | the_mask
print(flag_register)
flag_register |= the_mask
print(flag_register)
# negar mi bit
# reemplazar un zero con uno y uno con zero
flag_register = flag_register ^ the_mask
print(flag_register)
flag_register ^= the_mask
print(flag_register)
#
# dezplazamento izquierdo y desplazamiento derecho
# otra operacion relacionada con los bits inidividuales : shifting
# se aplica solo a los valores enteros
# 12345 * 10 = 123450 => desplazamiento a la izquierda y llenar el vazio con zero
# 123450 / 10 = 12345 => desplazamiento a la derecha
# igual en binario, desplazarlos a la izquierda es igual a multiplicar con 2
# los operadores de cambio en python son un par de digrafos << y >>
# value << bits y value >> bits
# este tipo de operacion no es conmutativa <=> el orden si influje
print(17 >> 1)  # 8 <=> 17//2
print(4 << 2)  # 4*4 <=> 16   dezplazar a la izquierda 2 bits es como multiplicar por 4

# tabla de prioridades de los operaciones actualizada
# 1	~, +, -	unario
# 2	**
# 3	*, /, //, %
# 4	+, -	binario
# 5	<<, >>
# 6	<, <=, >, >=
# 7	==, !=
# 8	&
# 9	|
# 10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

# listas
# ordenamiento es el proceso de ordenar los numeros
# escalar solo puede contener un valor (no mas de uno)
# declarar una lista con corchetes, corchete abierto [ corchete cerrado ]
numbers = [1, 2, 3, 4, 5]  # longitud igual a cinco
# pueden contener valores de diferentes tipos
numbers2 = [1, "2", 3, 4, 5]  # es un colleccion de elementos pero cada elementos es un escalar
print(numbers2)  # empieza con cero y termina con cuatro por lo que si hay cincos elementos

# indexando listas
# cambiar el valor del primer elemento de la lista
numbers[0] = 11
print(numbers)
# copiar el valor del qui=nto elemento al segundo
numbers[1] = numbers[4]  # indice es el valor dentro de los corchetes
# indexacion es el proceso de recuperar el valor de un elemento de una lista
val = numbers[1]
print(val)

# la longitud de la lista con la funcion len()
# la logitud puede variar (agnadir valores o quitar) por eso se dice que la lista es muy dinamica
print(len(numbers))

# eliminando elemento de una lista
print(numbers2)
del numbers2[0]
print("after del numbers[0]", numbers2)
del numbers2[-1]
print("after del 2 numbers[-1]", numbers2)
print(len(numbers))
print(numbers)  # notar que se quito el 11 en el primero
# ya que no existe el quinto, no puedes sacar su valor, tampoco agnadir un valor
# print(numbers[4]) # causara error IndexError
# numbers[4]=1 # causara error IndexError

# los indices negativos son validos
# indice -1 es el ultimo
print(numbers[-1])
print(numbers[3])

# funciones frente a metodos
# invocacion de una funcion
# res = funcion(argumento)
# invocacion de un metodo parece a este
# res = data.method(arg)

# agregando elementos a una lista
numbers.append(6)  # se anadido al final de la lista existente
# el metodo insert es un poco inteligente, puede agregar un nuevo elemento en cualquier lugar de la lista
print(numbers)
numbers.insert(-1, 10)  # the shift is to the right so the value is put at the before last element
print(numbers)
print(numbers[1])

# continuacion de agregamiento de elementos en una lista
my_list = []  # Creando una lista vacía.
for i in range(5):
    my_list.insert(0, i + 1)  # insert es inversado
print(my_list)

# haciendo useo de las listas
# sumar los valores
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print("total", total)
# ocultar la indexacion
total = 0
i = 0
for i in my_list:
    total += i
print("total", total)

# listas en accion
# intercambiar los valores de 2 variables si requiere un tercero variable dicho auxiliar
var = 1
var_2 = 2
print(var, var_2)
auxiliar = var
var = var_2
var_2 = auxiliar
print(var, var_2)
# python ofrece una forma mas conveniente de hacer el intercambio
var, var_2 = var_2, var
print(var, var_2)
# revertir un orden
lo = [1, 2, 3, 4, 5]
print(lo)
lo[0], lo[4] = lo[4], lo[0]
lo[1], lo[3] = lo[3], lo[1]
print(lo)
# pero si la lista contiene 100 elementos
# lo harias con una lista que contenga 100 elementos ?
# solucion => usar el bucle for
print("lo", lo)
for i in range(len(lo) // 2):
    lo[i], lo[-(i + 1)] = lo[-(i + 1)], lo[i]
print(lo)

# lista tipo de dato en python para almacenar multiples objetos, es una coleccion ordenada y mutable de elementos
# separados por coma entre corchetes
# las listas pueden ser anidadas, veremos mas sobre anidamiento mas tarde
ta = [1, "2", 3, [4, 5, 6], "7"]
for i in ta:
    print(i)
my = [1, 2, 3]
del my[0]
print(my)
# del my
# print(my) this will create a NameError it is not defined

# ordenamiento burbuja
# comparar los elementos adyacentes y al intercambiar algunos de ellos logramos nuestro objetivo
# poco eficiente
# ordenar de tipo ascendente o descendente
lista = [8, 10, 6, 2, 4]  # ascendente
print(lista)
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)  # now its correct we needed 3 times

# bueno vamos a mejorlo con introducion de un variable swap (intercambio)
swap = True
conteo = 0
lista = [8, 10, 6, 2, 4]
print("lista", lista)
while swap:
    swap = False
    conteo += 1
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            swap = True
    print("lista intermediaro", lista)
print("lista", lista)
print("conteo", conteo)

# python tiene un metodo para ordenar lista .sort()
lista = [8, 10, 6, 2, 4]
print("antes de sort", lista)
lista.sort()  # y este est mucho mas rapido
print("ya clasificada", lista)

# tambien hay un metodo llamado .reverse() para invertir los elementos de una lista
# no es ordenamiento por valor si no que es reversar los indices de cada elementos
lista = [1, 7, 5, 2]
# con reverse() esto cambiara en [2,5,7,1]
print("lista", lista)
lista.reverse()
print("lista.reverse()", lista)

a = "A"
b = "B"
c = "C"
d = " "
lst = [a, b, c, d]
lst.reverse()
print(lst)

# la vida al interior de las listas
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)  # imprime 2 pero deberia ser 1 no ?
# eso es debido a que las listas y muchas otras entidades en python
# se almacenan de diferentes maneras que las variables escalares
# el nombre de una variable ordinaria es el nombre de su contenido
# el nombre de una lista es el nombre de una ubicacion de memoria donde se almacena la lista
# entonces la asignacion list_2=list_1 copia el nombre del arreglo no su contenido
# en efecto las dos listas identifican la misma ubicacion en la memoria de la computadora
# asi que modificar uno afecta el otro

# rebanadas poderosas, rebanada = slice
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)  # va imprimir 1 por que la rebanada copia los contenidos, no el nombre
lisa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lisa2 = lisa[:]
print("lisa2", lisa2)
lisa3 = lisa[0:len(lisa)]
print("lisa3", lisa3)
print(lisa[1:5])

# rebanadas indices negativo
lisa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lisa[1:-1])
# si la position de l'indice de end est plus devant que celle de start, le retour sera vide
print(lisa[-1:1])  # va imprimir vacia

# rebanadas continuacion
# si te estabas pasando por alta el start, el valor del indice start por defecto es 0
# de igual manera si omites el end, sera igual a decir len(lisa)
lisa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lisa[4:])

# rebanadas continuacion
# la instruccion del tambien puede eliminar rebanadas
lisa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del lisa[4:]  # nota que en este caso la rebanada no va producir una nueva lista
print(lisa)
# al igual puedes eliminar todos los contenidos de la lista
del lisa[:]  # la lista queda vacia
# del lisa # la lista ya no va existir
print(lisa)  # nota que es diferente a del lisa que luego al imprimir produce un error NameError

# los operadores in y not in
lisa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if 10 in lisa:
    print("10 is in lisa")
else:
    print("10 is not in lisa")
if 10 not in lisa:
    print("10 is not in lisa")

# listas algunas programas simples
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print(largest)

# listas algunas programas simples
# buscar si el numero esta en una lista
# buscar cuantos numeros de la oloteria has atinado

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_elements = []
for i in my_list:
    if i not in unique_elements:
        unique_elements.append(i)
my_list = unique_elements
print("La lista con elementos únicos:")
print(my_list)

# puntos claves
listi = [1, 2, 3, 4, 5]
listj = listi
del listi[0]
print(listj)
del listj
# meme s'il partage la meme valeur en memoire, supprimer la liste revient à supprimer seulement la referecne
print(listi)

# listas en aplicaciones avanzadas
# listas dentro de listas
# las listas puenden constar (contenir) de escalares y elementos mucho mas complejos
# en vida real, el mejor ejemplo es un tablero de ajedrez: compuesto de filas y columnas
# una comprension de lista es una lista pero se cree de manera dinamica mientras que corre el programa
# opcion una
row = []
for i in range(8):
    row.append("WHITEPAWN")
print(row)
# se puede hacerlo tambien con comprension de lista
row = ["WHITEPAWN" for i in range(8)]
print(row)
odds = [x for x in range(10) if x % 2 != 0]
print(odds)

# arreglos bidimensionales
board = []  # board ahora es un tablero bidimensional o se le llama matriz
for i in range(8):
    row = ["EMPTY" for j in range(8)]
    board.append(row)
# podremos tambien utilizar la forma de compreson
board = [["EMPTY" for i in range(8)] for j in range(8)]
print(board)

# continuacion
# para encontrar cualquier elemento de una lista bidimensional, debes usar dos coordenadas
# una vertical (numero de fila)
# una horizontal (numero de campo de columna)

# arrgeglos tridimensionales
# verifica si hay disponibilidad en el piso 15 del tercer edificio
hotel = [[[False for i in range(20)] for j in range(15)] for k in range(3)]
for i in range(20):
    if not hotel[2][14][i]:
        print("Disponible el piso 15 del tercer edificio en la habitacion", i)


