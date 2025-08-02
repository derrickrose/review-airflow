dico = {"a": 1, "b": 2}
print(dico)
dico.update({"c": 100})
print(dico)
dico.clear()
print(dico)
del dico
# print(dico) # NameError
dico = {"a": 1, "b": 2}
print(dico)
del dico["a"]
print("----------------")
print(dico)
dico["a"] = 100
print(dico)
a = dico.copy()
print(a)
print("pop item", a.popitem())
print(a)

###
print("-------------------------")
tupla = 1, 2, 1, 3, 4, 1, 5
print(tupla.count(1))
# tupla[0]=1 # TypeError
print(len(tupla))
print(tupla)
tupla2 = tupla[:2]
print(tupla2)

lista = [1, 2, 3]
print(lista)
lista[0], lista[2] = lista[2], lista[0]
print(lista)

# tuple travail ensemble avec dico car dico.popitem return a tuple last added item
print(len(dico))

li = [("a", 1), ("b", 2), ("c", 3)]
di = dict(li)
print(di)

print(di.popitem())
print(di)
t = list(tuple(di.items()))
print(t)

print("--------------------------------------------")
dicc = {"a": "1", "b": "2"}
dicc2 = dicc
print(dicc)
print(dicc2)
dicc2["c"] = "3"
print("dicc2 after", dicc2)
print("dicc after", dicc)

def modif(array):
    array[0] = 100
    print(array)

array = [1, 2, 3]
print(array)
modif(array)
print(array)

def modif2(dic):
    dic = {"a": 1, "b": 2}
    dic["a"] = 100
    print(dic)

dic = {"a": 1, "b": 2}
print(dic)
modif2(dic)
print("dic after", dic)

