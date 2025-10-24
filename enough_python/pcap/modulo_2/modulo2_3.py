# capitalize
## convierte en majuscula el primer caracter y los de mas en minuscula
## crea una nueva cadena => return
## no se cambia el original
str1 = "hello world"
print(str1.capitalize())
print(str1)
str1 = "HELLO WORLD"
print(str1.capitalize())
str1 = " ALPHA"
print(str1.capitalize())

# center
str1 = "abc"
str1 = str1.center(10)  # 10-3 = 7 , il a mis 3 avant e 4 apres espace => il priorise toujours derriere
print("[" + str1 + "]")
print(len(str1))
print(str1.index("a"))
str1 = "abc"
print("[" + str1.center(2) + "]")  # cuando el espacio dedicado es mas pequena que la cadena regresa la cadena
str1 = "abc".center(10)
print(len(str1))
print(str1.index("a"))
str1 = "abc".center(12)
print("[" + str1 + "]")
print(len(str1))
print(str1.index("a"))
print(str1.center(105, "*"))  # podemos reemplazar el espacio por otro caracter

# endswith()
str1 = "hello world"
print(str1.endswith("world"))
print(str1.endswith("k"))

# find()
va = "hello world"  # no regresa error si no se encuentra, regresa -1
print(va.find("r"))
print(va.find(""))
print(va.find("h"))
va = ""
print(va.find(" "))
va = " "
print(va.find(""))  # regresa siempre zero si busca una cadena vacia dentro de una cadena
va = "   "
print("aki", va.find("", 1))
## find() vs in
stra = "hello world, hello universe"
if "hello" in stra:
    print("hello is in str")
else:
    print("hello is not in str")
if stra.find("hello") != -1:
    print("hello is in str")
# con find puedes buscar la ssecunda y mas instancias
print(stra.find("hello", 1))

## existe tambien una variante de find() que espera 3 parametros
### limite de la busqueda
str = "tout va bien pour tout le monde dans ce monde de tofu fotuto"
print(str.find("to", 50, ))  # regresa 58
# con el limite exclusivo de [50, 58[ ya no se encuentra
print(str.find("to", 50, 58))

# isalnum() alphanumeric alfabetico o digito
print("abc123".isalnum())
print("é".isalnum())
print("abc1 23".isalnum())
print("".isalnum())
print(" ".isalnum())
print("ΑβΓδ".isalnum())
print("isalnum", "12334".isalnum())

# isalpha()
print("abc".isalpha())
print("".isalpha())  # false pour vide
print("isalpha", "abc".isalpha())

# isdigit()
print("123".isdigit())
print("".isdigit())
print("isdigit", "12345".isdigit())

# islower()
print("abc".islower())
print("ABC".islower())
print("abc1".islower())
print("islower", "a1 .%ù".islower())  # if there is only a digit it is false but if whith one cchar lower it True
print("".islower())  # False
print("aki", " ".islower())
print("a ".islower())

# isspace()
print(" ".isspace())
print("  ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
print("abc".isspace())
print("".isspace())  # False

# isupper()
print(" ".isupper())
print("".isupper())
print("A ".isupper())

# join()
# print("".join([1, 2, 3]))  # TypeError expected str instance, found in
print("".join(["1", "2", "3"]))
print("aki", "".join([]))
print("aki", "".join(["1"]))
print("aki", "a".join(["", "", ""]))
a = "".join(["", "", ""])
print(a)
print(len(a))

# lower
print("ABC".lower())
print("abc".lower())
print("ABC1".lower())
print("ABC1".lower())

# lstrip(), tambien crea una nueva cadena
## n'importe quel caractere qui match un des caracter dans la liste si il se trouve a gauche
a = " abc"
print("[" + a.lstrip())  # se quito el espacio a la izquireda, todos los espacios izquierda
a = "abc "
print("[" + a.lstrip())  # no regresa error
a = "www.sfr.fr"
print("w.|" + a.lstrip("w."))
a = "heloo world"
print("y" + a.lstrip("oo "))
a = "heloo world"
print("yy" + a.lstrip("eh"))

# replace()
## al ilgual regresa nueva cadena
str1 = "hello world"
print(str1.replace("world", "universe"))
print(str1)
#### otra variante de replace()
stra = "this is it is"
print(stra.replace("is", "it", 1))  # pero reemplaza una sola vez => thit is it
print(stra.replace("is", "it", 2))  # thit it it

# rfind()
# parejo que find de la derecha, pero no cuenta regresivo, el index siempre viene de la izquierda
stra = "hello world, hello"
print(stra.rfind("hello"))
print(stra.rfind("hello", 0, 5))
print(stra.rfind("hello", 5, 0))
print(stra.find("hello"))
stra = "aaaaaaaaaaaaaaaaaaaaaaaaa"
print(stra.rfind("a", 6, 0))

# rstrip()
# igual que lstrip()
a = " abc "
print(a.rstrip() + "]")
a = "abc"
print(a.rstrip("c") + "]")
a = "abcd"
print(a.rstrip("ab") + "]")

# split()
a = "hello world"
print("split sin parametro", a.split())  # ['hello', 'world']  # la operacion inversa se realiza con join()
a = " hello, world "

# strip()
print(a)
print(a.strip())
a = "hello, world "
print(a.strip(" h") + "!")

# startswith()
str1 = "hello world"
print(str1.startswith("hello"))
print(str1.startswith("hello "))

# el metodo swapcase()
str1 = "HELLO WORLD"
print(str1.swapcase())
str1 = "abcDEFan"
print(str1.swapcase())
print("swapcase", "ijéçà$£là@çoầ^ôâêîôûïëüïö".swapcase())

# title()
str1 = "hello world"
print(str1.title())  # "Hello World"

# upper()
str1 = "hello world"
print(str1.upper())
str1 = "ABC"
print(str1.upper())  # todos en mayusculas


## building own split method
def mysplit(strng):
    strng = strng.strip()
    if not strng:
        return []
    array = []
    current = ""
    for c in strng:
        if c == " ":
            if current:
                array.append(current)
            current = ""
        else:
            current += c
    array.append(current)
    return array

    #  # coloca tu código aquí  #


print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# seguir con laboratorio de 2.3
# https: // edube.org / learn / python - essentials - 2 - esp / tu - propio - split - 1
