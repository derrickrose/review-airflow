def route(a, b):
    print("a", a, "b", b)


route("a", "b")

route(b="a", a="b")


def to(a, b):
    print(a, b)
    return


to("a", "b")


def wishing(wish=True, birth=True):
    print("-------------------")
    if wish:
        print("happy birthday")
    if birth:
        print("birth")


arr = [1, 2, 3]


def imprimir(n):
    o = n
    print("inside", n)
    o[0] = 100
    print(n)  # print("inside", arr)


print(arr)
imprimir(arr)
print("outside", arr)


# to avoid the modification, use rebanadas slicing

def vara(n):
    n += 100
    print(n)


n = 10
print(n)
vara(n)
print(n)

# isinstance
val = .7
print(isinstance(val, float))

print(type(val) is float)


ton = "ton"
print(ton)


def toto():
    global ton  # esto hace que python no crea una nueva varible, usa la que esta afuera
    ton = "tontont2"
    print("ton en local", ton)


toto()
print(ton)

arr = [1, 2, 3]
def po(arr):
    print(arr)
    arr=[1,1,1]
    print(arr)
print(arr)
po(arr)
print(arr)


var = [1, 2, 3]


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    my_list_1.append(0)
    print("Print #2:", my_list_1)
    print("Print #3:", var)


my_function(var)
print(var)

var = [1, 2, 3]


varvarvar = [1, 2, 3]


def my_function(my_list_1):
    print("toto Print #1: mylist", my_list_1)
    global varvarvar
    del varvarvar
    my_list_1.append(0)
    print("toto Print #2: mylist", my_list_1)  # print("Print #3: varvarvar", varvarvar)


my_function(varvarvar)
# print(varvarvar) # NameError


variable = [1, 2, 3]
def check(variable):
    variable.append(4)
    print(variable)
print(variable)
check(variable[:])
print(variable)

var1 = 1
var2 = 2
var3 = 3

var1,var2,var3 = var3,var2,var1
print(var1,var2,var3)


dico = {"a": 1, "b": 2}
print(len(dico))

words = ["a", "b", "c"]
print(len(words))

for word in words:
    if word in dico:
        print(word, dico[word])
    else:
        print(word, 0)


dico = {"a": 1, "b": 2}
print(dico)
dico.update({"c": 100})
print(dico)
print(dico.popitem())
print(dico)


dic = dico.copy()
print(dic)
dic.clear()
print(dic)
print(dico)


tupla = 1,2,1,3,4,1,5
print(tupla.count(1))

lista = [1,2,1,3,4,1,5]
print(lista.count(1))

dico = {}
dico.update({"a": 1, "b": 2})
print(dico)

dic = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}
dic3 = {}
# for item in dic, dic2:
#     for key, value in item.items():
#         dic3[key] = value
# print(dic3)
dic3 = {**dic, **dic2}
print(dic3)

tup = tuple(dic3.items())
print(tup)

diccc = dict(tup)
print(diccc)


dic = {"chien": "perro", "chat": "gato"}
tup = tuple(dic.values())
print(tup)
print(diccc)


dic = {"chien": "perro", "chat": "gato"}
tup = tuple(dic.values())
print(tup)

dico = {"a":1, "b":2}
ic = dico.copy()
print(ic)
dico = {"a":1, "b":2}
ic = dico.copy()
print(ic)