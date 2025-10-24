# capitalize()
## convierte en majuscula el primer caracter y los de mas en minuscula
## crea una nueva cadena => return
## no se cambia el original
str1 = "hello world"
print("capitalize", str1.capitalize())  # Hello world
print("original", str1)
str1 = "HELLO WORLD"
print("capitalize HELLO WORLD", str1.capitalize())  # Hello world
str1 = "  ALPHA"
print("capitalize space ALPHA", str1.capitalize())  # alpha

# center()
# siempre con argumento entero
# el argumento 10 por ejemplo en este caso va ser el len() del string
# ya que viene 3 caracteres , 10 -3 = 7
# se divide ese 7 en 3, 3 adelante, 4 atras
# se crea nueva cadena, no cambia el original
str1 = "abc"
print("abc center 10", list(str1.center(10)))  # 3 frente, 4 atras
print("abc center 13", list(str1.center(13)))  # 5 frente, 5 atras
print("abc center 14", list(str1.center(14)))  # 5 frente, 6 atras
print("original", str1)

# siguemos con center, pero cuando el espacio proporcionado es menor que el nombre de caracteres actual de la cadena
str1 = "abc"
print("espacio inferior cadena", list(str1.center(2)))  # no hay cambios, regresa la cadena tal cual
print(list(str1.center(10, "*")))  # podemos reemplazar el espacio por otro caracter

# endswith()
str1 = "hello world"
print("endswith()", str1.endswith("world"))
print("endswith()", str1.endswith(" "))

# find()
# no regresa error si no se encuentra, regresa -1
va = "hello world"
print("find r in hello world", va.find("r"))  # 8
print("find empty in hello world", va.find(""))  # 0
print("find h in hello world", va.find("h"))  # 0
va = ""
print("finding space on empty", va.find(" "))  # -1
va = " "
print(va.find(""))  # 0 regresa siempre zero si busca una cadena vacia dentro de una cadena
va = "   "
print("aki", va.find("", 1, 2))  # 1
## find() vs in
stra = "hello world, hello universe"
if "hello" in stra:
    print("hello is in str")
else:
    print("hello is not in str")
if stra.find("hello") != -1:
    print("hello is in str")
# con find puedes buscar la secunda y mas instancias
print("find a word", stra.find("hello", 1))  # 13

## existe tambien una variante de find() que espera 3 parametros
### limite de la busqueda (inclusivo en __start y exclusivo en __end)
## debe todo los caracteres de la cadena acabar en el limite
valor = "tout va bien pour tout le monde dans ce monde de tommy fotuto"
print("find to", valor.find("to", 50, ))  # regresa 59
# con el limite exclusivo de [50, 58[ ya no se encuentra
print(valor)
print("find to 222222222", valor.find("tommy", 49, 54))  # -1

# isalnum() alphanumeric alfabetico o digito
print("abc123 is alnum", "abc123".isalnum())  # True
print("é is alnum", "é".isalnum())  # True
print("abc1 23 is alnum", "abc1 23".isalnum())  # False
print("empty string is alnum", "".isalnum())  # False
print("space is alnum", " ".isalnum())  # False
print("ΑβΓδ is alnum", "ΑβΓδ".isalnum())  # True
print("12334 is alnum", "12334".isalnum())  # True

# isalpha()
print("abc is alpha", "abc".isalpha())  # True
print("empty string isalpha", "".isalpha())  # false pour vide

# isdigit()
print("123 is digit", "123".isdigit())
print("empty string is digit", "".isdigit())
print("12345 isdigit", "12345".isdigit())

print("=============================================")
# islower()
print("abc is lower", "abc".islower())  # True
print("ABC is lower", "ABC".islower())  # True
print("abc1 is lower", "abc1".islower())  # True
print("a1 is lower", "a1 .%ù".islower())  # True
print("empty string is lower", "".islower())  # False
print("space is lower", " ".islower())  # False
print("a space is lower", "a ".islower())  # True

# isspace()
print("---------------------------------spaces")
print(" ".isspace())
print("  ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
print("abc".isspace())
print("".isspace())  # False
print("---------------------------------end spaces")

# isupper()
print("---------------------------------upper")
print(" ".isupper())  # False
print("".isupper())  # False
print("A %*U".isupper())  # True

# join()
# print("".join([1, 2, 3]))  # TypeError expected str instance, found in
print("_______________________________________________join")
print("".join(["1", "2", "3"]) == "123")
print("aki", "".join([]))
print("aki", "".join(["1"]))
print("aki", "a".join(["", "", ""]))
a = "".join(["", "", ""])
print("|" + a + "|")
print(len(a))

# lower
# no cambia el original
# crea una nueva cadena
print("----------------------------------lower")
a = "ABC"
print(a.lower())
print("original", a)
print("abc".lower())
print("ABC1".lower())

# lstrip(), tambien crea una nueva cadena
## n'importe quel caractere qui match un des caracter dans la liste si il se trouve a gauche
print("----------------------------------lstrip")
a = " abc"
print("[" + a.lstrip())  # se quito el espacio a la izquireda, todos los espacios izquierda
a = "abc "
print("[" + a.lstrip())  # no regresa error
a = "www.sfr.fr"
print("w.|" + a.lstrip("w."))  # this is not the exact string, ust errase the w and/or . from the left
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
print(stra.replace("is", "it", 3))  # thit it it is

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
print(a.rstrip("db") + "]")

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
print("-------------------------------startswith")
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
print("-----------------------title")
str1 = "hello world"
print(str1.title())  # "Hello World"
str1 = """ hello, 
        world
        
        dinamo db
        dynastie    tara.loatra1toto
        """
print(str1.title())

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
