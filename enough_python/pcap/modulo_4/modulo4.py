# generadores, donde encontrarlos
## un generador en Python es un fragmento de codigo capaz de producir una serie de valores y controlar el proceso de iteracion
## es la razon por lo cual los generadores a menudo se llaman iteradores aun que hay quienes que pueden encontrar una diferencia entre estos dos
for i in range(5):
    print(
        i)  ## la funcion range() es un generador y tambien es un iterador  ## un funcion devuelve un valor una vez, y solo una vez


## un generador devuelve una serie de valores y en general se invoca (implicitamente) mas de una vez
## en el ejemplo, range(5) se invoca 6 veces (implicitamente), proporcionando 5 valores de cero a cuatro

# protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las reglas impuestas por el contexto
## de las sentencias for e in
## un objeto conforme al protocolo de iterador se llama iterador
## un iterador debe proporcionar dos métodos: __iter__() y __next__()
## exo : redefine the function range


class MyIterator:  # iterator implements __next__
    def __init__(self, minimum, maximum, step=1):
        self.__i = minimum
        self.__maximum = maximum
        self.__step = step

    def __next__(self):
        if self.__i >= self.__maximum:
            raise StopIteration  # parent of StopIteration is Exception
        else:
            val = self.__i
            self.__i += self.__step
            return val


class MyRange:  # Iterable (implements __iterator__ )

    def __init__(self, min_or_max, maximum=None, step=1):
        if maximum is None:
            self.__minimum, self.__maximum = 0, min_or_max
        else:
            self.__minimum, self.__maximum = min_or_max, maximum
        self.__step = step

    def __iter__(self):
        return MyIterator(self.__minimum, self.__maximum, self.__step)


print("_start_")
for i in MyRange(5):
    print(i)


## iterable implement init
## iterator implement next
## iterable(iterator)

# version compact
class IterableIterator:
    def __init__(self, min_or_max, maximum=None, step=1):
        if maximum is None:
            self.__i, self.__maximum = 0, min_or_max
        else:
            self.__i, self.__maximum = min_or_max, maximum
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i >= self.__maximum:
            raise StopIteration
        res = self.__i
        self.__i += self.__step
        return res


print("__version_3_")
for i in IterableIterator(2):
    print(i)

## fibonacci
print("Fubonacci")


class Fibonacci:

    def __init__(self, val):
        self.__val = val
        self.__val1 = 1
        self.__val2 = 1
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):

        self.__i += 1
        if self.__i > self.__val:
            raise StopIteration
        if self.__i in [1, 2]:
            return self.__i, self.__val1
        else:
            res = self.__val1 + self.__val2
            self.__val1, self.__val2 = self.__val2, res
            return self.__i, res


for i in Fibonacci(3):
    print(i)


# la sentencia yield  ## se necesita guardar el estado de la iteracion en las invocaciones subsecuentes de __iter__  ## por ejemplo por Fubonacci, habra que guardar los valores evaluados en las iteraciones anteriores  ## que por eso Python ha creado una manera mas simple de iterar


def fun(i):
    for i in range(i):
        return i


# for i in fun(5):
#     print( i)


## imprime solo cero ya que el for no tiene manera de terminar su iteracion por que se detuvo por la instrucion return

## con yield eso cambia
## igual que return pero no pierde el estado de la funcion
## todos los valres de las variables estan congelados y esperan la proxima invocacion
## cuando se reanuda la ejecucion (no desde cero como usando return)
## dicha funcion no se debe invocarse explicitamente ya que no es una funcion, es un objeto generador
## la invocacion devolvera el identificador del objeto, no la seria que esperamos del generador
## por lo tanto que la funcion anterior se invoca explicitamente (con return )

# como construir un generador
def fun2(i):
    for i in range(i):
        yield i


a = fun2(5)
print(a)  # <generator object fun2 at 0x7004134c9300>

for i in fun2(5):
    print(i)


## que pasa si quiere producir las primeras n potencias de 2
def fun(n):
    val = 1
    for i in range(n):
        yield val
        val *= 2


print("powers of 2")
for i in fun(8):
    print(i)

## se puede tambien usar con lista con comprension
print([i for i in fun(8)])

## se puede igual usar la function list()
print(list(fun(8)))

## se puede usar in tambien
print(2 in [i for i in fun(8)])
print(2 in list(fun(8)))
print(2 in fun(8))


## el generador de numeros Fibonacci
def fibonacci(n):
    res = 1
    prev = 1
    for i in range(1, n):
        if i in [1, 2]:
            yield 1
        else:
            yield prev + res
            prev, res = res, prev + res


print(list(fibonacci(8)))

# mas acerca de lista por comprension
## filtrar cuando se crea una lista
the_list = [i for i in range(10) if i % 2 == 0]
print(the_list)  # los corchetes hacen una lista

## filtrar cuando se crea un generator
## con parentesis es un generator (no tupla) en este caso
the_generator = (i for i in range(10) if i % 2 == 0)
print(the_generator)


# print(len(the_generator)) # TypeError object of type generator has no len
def fun(i):
    a = []
    for i in range(i):
        a.append(i)
    return a


def fun2(i):
    for i in range(i):
        print("inside generator ")
        yield i


print("here")
a = fun(5)  ## ya esta directamente creada la lista y pues se guarda en memoria
print(a)
print("here2")
b = fun2(5)
print(b)
for i in b:
    print(i)  ## generator is lazy evaluation, se evalua solo cuando se esta iterando sobre el

# la funcion lambda
## funcion sin nombre o funcion anonima, para facilitar el entendimiento del programa
## syntaxis lambda parameters : expression
two = lambda: 2
print("lambda", two())
sqr = lambda x: x ** 2
print("lambda", sqr(2))
cal = lambda x, y: x + y
print("lambda", cal(2, 3))

# como usar lambdas y para que
arr = [1, 2, 3, 4, 5]
arr2 = map(lambda x: x ** 2, arr)
print(arr2)
for i in arr2:
    print(i)  ## es map() regresa un generador ????


## la mejor manera de usar lambda es en su forma anonimo
def print_fun(args, fun):
    for arg in args:
        print("arg", arg, "fun", fun(arg))


def power(x):
    return x ** 2


print_fun([1, 2, 3, 4, 5], power)

## ahora con lambda
print("usando lambda")
## la funcion print_fun sique igual, solo ya no se necesita la funcion power

print_fun([1, 2, 3, 4, 5], lambda x: x ** 2)

# lambda y la funcion map()
# map(funcion, list) syntaxis
list1 = [i for i in range(10)]
list2 = map(lambda x: x ** 2, list1)
print(list1)
print(list2)
print("primero")
for i in list2:
    print(i)
print("segundo")
for i in list2:
    print(i)
print("tercero")

for i, j in map(lambda x: (x, x + 1), list1):
    print(i, j)

# lambda y la funcion filter()
arr = [1, 2, 3, 4, 5]
arr2 = [i for i in arr if i % 2 == 0]
## usando lambda
arr2 = filter(lambda x: x % 2 == 0,
              arr)  ## es el filter tambien regresa un generador, no es un generador es un iterador pezero
print(arr2)
print("first")
for i in arr2:
    print(i)
print("second")
for i in arr2:
    print(i)


# cierres
## cierre es una tecnica que permite almacenar valores a pesar de que el contexto en el que se crearon ya no existe
def outer(par):
    loc = par


var = 1
outer(var)  ## obviamente erroneo NameError por ambas


# print(par)
# print(loc)

def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var = 1
fun = outer(var)
# se imprimo el valor de loc aun que ya no existe en el contexto  ## se congela entonces la funcion inner() y tambien con los valores que los estan accesibles (loc por supuesto)  ## inner() solo se puede invocar desde dentro de outer()

print(fun())


## resulta que al invocar outer, aun que ya no existe la funcion, por inner se regresa el valor
## la funcion devuelta durante la invocacion de outer() es un cierre ==> inner

## otro ejemplo
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc

    return power


fsqr = make_closure(2)
fcub = make_closure(3)
print(fsqr(2), fcub(2))


## el cierre no solo utiliza el ambiente congelado, sino que tambien puede modificar su comportamiento utilizando valores
## tomados del exterior
## yield solo se puede utilizar dentro una funcion
## ejemplo decorar un valor

def decorador(tag):
    def inner(texto):
        return tag + texto + tag[0] + "/" + tag[1:]

    return inner


deco = decorador("<div>")
print(deco("hola"))

##
any = [1, 2, 3, 4]
even_list = list(map(lambda x: x%2, any))
print(even_list)

# seguir aca
# 4.2.1 Accediendo archivos desde código en Python