# en python string (cadena) es str

# secuencias inmutables (no se puede cambiar, para cambiar habra que crear una nueva)
s = 'abc'
# s[0] = 'd' # TypeError: str object does not support item assignment

# conteo de caracteres
s = ""
print(len(s))  # 0
s = "by"
print(len(s))  # 2
s = "by\""
print(len(s))  # 3 por que el caracter de escape no esta contado

# cadenas multilineas
b = """
a 
"""
print("b", b)
print("len b", len(b))  # 4 => 1 salto de linea, el caracter a, el caracter espacio, el caracter salto de linea

# operaciones con cadenas
## pueden ser concatenadas "aaa"+"bbb"
## replicadas 2 * "cccc"
str1 = "aaa"
str2 = "bbb"
str3 = str1 + str2
print("str3", str3)  # 'aaabbb'
str4 = 2 * str3
print("str4", str4)

## print(str1 * str2) # TypeError cant multiply sequence by non-int of type str

# los atajos tambien pueden ser aplicadas += and *= (augmented assignment)

# para saber el valor del punto de codigo de un caracter, ord() => ordinal
## TypeError si no cumple con uno y un solo caracter
print("ord", ord("a"))

# si conoces el punto de codigo, la funcion ch() regresa el caracter
## ingresar un valor invalido para el regresa un error TypeError or ValueError
print("ch", chr(97))
# => a  # print(chr(-1)) # ValueError
# print(chr(256.)) # TypeError

# indexacion
stra = "abcde"
print(stra[0])
### no se debe intentar pasar el limite, va salir IndexError
print("---------------------------------------")
for i in range(len(stra)):
    print(stra[i])
print("________________-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
### los indices negativos tambien si funcionan
for i in range(len(stra) - 1, -1, -1):
    print(stra[i])
for i in range(-1, -(len(stra) + 1), -1):
    print(i, stra[i])
print("-----------------fin------------------------------")

# rebanadas
stri = "abcdef"
print(stri[1:3])
print("valor erroneo", stri[1:-100])

# operadores in y not in
str2 = "abc"
print("d" in str2)
if "a" in str2:
    print("a is in str2")
else:
    print("a is not in str2")

# las cadenas son inmutables
str2 = str2 + "d"
print(str2)
## habra error de TypeError si intentas modificar un valor de la cadena con su index
# str2[0] = "e"
## igual por del
# del str2[0] TypeError: 'str' object doesn't support item deletion
del str2
# print(str2) #NameError not defined
str2 = "a"

# str2.append("e") # AttributeError

# min()
## se refiere en su punto de codigo
str2 = "abc"
print("min", min(str2))
str2 = "Abc"
print("min", min(str2))

# max()
print("max", max(str2))
str2 = ""

# print("[" + max(str2) + "]") # ValueError max() iterable argument is empty


# index()
str2 = "abcefehjfkdsfds"

# print(str2.index("x")) => ValueError substring not found
print(str2.index("e"))

# list
str2 = "abc"
print(str2)
str2 = list(str2)
print("list(str)", str2)
str2.append("d")
str2 = "".join(str2)
print("after join", str2)

a = ""
a = list(a)
print(a)  # no error

# count()
print("count")
a = "abc"
print(a.count("a"))
print(a.count(
    "x"))  # no regresa error si no existe  ## las listas de metodos de cadenas en python https://docs.python.org/3.4/library/stdtypes.html#string-methods

###############################################################################

# cadenas en action
# comparacion con los mismos operadores == != > < <= ...
print("alpha" == "alpha")  # True
print("alpha" != "Alpha")  # True
print("alpha" < "alphabet")  # True
print(
    "alpha" > "ALPHA")  # True => majuscula es inferior a minuscula, punto flotante a partir de 65 para mjuscula y 97 or minuscula

print("ALPHA > Alpha", "ALPHA" > "Alpha")  # False

# los digitos no se considera numero
print(
    "100" < "99")  # True por que 1 < 9 pero no se considera 99 y 100  ## en resumen se compara caracter por caracter y el primero que tiene mayor gana
print("199999" < "2")  # True
## asi que comparar cadena con numero siempre devuelve falso
print("'1' ==1 ", "1" == 1)
print("'1'!=1", "1" != 1)

# print("10" > 10)  # TypeError

# ordenamiento
greek = ["omega", "alpha", "pi", "gamma"]
## la primera sorted() , acepta una lista y regresa nueva lista
print(greek)
print(sorted(greek))
print(greek)  # permanece intacta
print(greek.sort())  # cambia directamente la lista, regresa None
print(greek)

# cadenas frente a numeros
## como convertir en numoro entero, flotante, ... de cadenas en entero ? ...
entero = 12
flotante = 12.3
sEntero = str(entero)
sFlotante = str(flotante)
print(sEntero)
print(sFlotante)
## la conversion inversa
### la conversion inversa solo es posible cuando los numeros son digitos validos usando int() y float()
### si el numero no es valido, regresa un error ValueError
print(float(sFlotante))
print(int(sEntero))  ###
