a = [0, 1, 2]


def fun(a):
    a = [1, 2]
    print(a)


fun(a)
print(a)


def fun2(a):
    del a[0]
    print(a)


fun2(a)
print(a)


def fun(firstname, lastname):
    print("hola", firstname, lastname)


fun("Pierre", "Marceau")
# fun("Pierre", firstname="Marceau") #TypeError
fun(firstname="Marceau", lastname="Pierre")

var = [1, 2]


def fun(var):
    var[0] = 100
    print(var)
    del var


print(var)
fun(var)
del var


# print(var)# NameError
# print(int("a")) #ValueError

def imprimir(a, b=0):
    print(a, b)


a = 1
b = 0
imprimir(a, b)
imprimir(b=1, a=1)
imprimir(a)
# imprimir(b=1)  # TypeError missing 1 required positional argument: 'a'

var = 1


def imprimir(var):
    print(var)
    var = 100
    print(var)
    del var


def imprimir2():
    global var
    var = 10000
    print(var)


print(var)
imprimir(var)
print(var)
imprimir2()
print(var)

var = 1


def imprimir3(a):
    global var
    print(var)
    var = 10_000_000
    print(var)
    var = a
    print(var)
    del var


imprimir3(var)  # print(var) # NameError since deleted on func and also made global inside the function
