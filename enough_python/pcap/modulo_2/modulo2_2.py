# cadenas
## secuencias inmutables (no se puede cambiar, para cambiar habra que crear una nueva)
## el caracter de escape no esta contado como caracter
word = "by"
print(len(word))
word = ""
print(len(word))
word = "b\'"
print(len(word))
word = "b\""
print(len(word))
for i in word:
    print(i)

# cadenas multilineas
b = """
a 
"""
print(b)
print(len(b))
## hay caracteres invisibles \n y es identificado a un caracter (caracter especial de control)
c = '''


a
'''
print(c)
print(len(c))

# operaciones con cadenas
## pueden ser concatenadas "aaa"+"bbb"
## replicadas 2 * "cccc"
str1 = "aaa"
str2 = "bbb"
str3 = str1 + str2
print(str3)
str4 = 2 * str3
print(str4)  # print(str1 * str2) TypeError cant multiply sequence by non-int of type str
## los atajos tambien pueden ser aplicadas += and *= (augmented assignment)

# para saber el valor del punto de codigo de un caracter, ord() => ordinal
## TypeError si no cumple con uno y un solo caracter
print(ord("a"))

# si conoces el punto de codigo, la funcion ch() regresa el caracter
## ingresar un valor invalido para el regresa un error TypeError or ValueError
print(chr(97))
# => a  # print(chr(-1)) # ValueError
# print(chr(256.)) # TypeError

# indexacion
stra = "abcde"
print(stra[0])
### no se debe intentar pasar el limite, va salir IndexError
for i in range(len(stra)):
    print(stra[i])
### los indices negativos tambien si funcionan
for i in range(len(stra) - 1, -1, -1):
    print(stra[i])

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
# del str2[0]
del str2
# print(str2) #NameError not defined
str2 = "a"

# str2.append("e") # AttributeError

# min()
## se refiere en su punto de codigo
str2 = "abc"
print(min(str2))
str2 = "Abc"
print(min(str2))

# max()
print(max(str2))
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
print(str2)
str2.append("d")
str2 = "".join(str2)
print(str2)

a = ""
a = list(a)
print(a)  # no error

# count()
a = "abc"
print(a.count("a"))
print(a.count("x"))  # no regresa error si no existe
## las listas de metodos de cadenas en python https://docs.python.org/3.4/library/stdtypes.html#string-methods
