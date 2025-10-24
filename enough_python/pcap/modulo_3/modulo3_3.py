# variables de instencia
## propriedades se puede crear con el constructor
## se puede iniciar en cualquier momento del ciclo de vida del objeto
## se puede eliminar en cualquier momento
## diferentes objetos de la misma clase pueden poseer diferentes conjuntos de propriedades
## debe haber una manera de verificar con seguridad si un objeto especifico posee la propriedad que desea utilzar
## cada objeto lleva su proprio conjunto de propriedades, no interfieren entre si de ninguna manera
## tales variables (propriedades) se llaman variables de instancia
## instancia por que es conectada a la instancia del objeto, no a la clase

class Example:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


obj1 = Example()
obj2 = Example(2)
obj2.set_second(3)
obj3 = Example(4)
obj3.third = 8  # creado fuera de la clase y es posible y totalmente permisible
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
"""
{'first': 1}
{'first': 2, 'second': 3}
{'first': 4, 'third': 8}
"""


## los objetos de Python, cuando se crean estan dotados de un pequeno conjunto de propriedades y metodos predefinidos
### ejemplo __dict__ : contiene nombre y valores de todas las propriedades (variables) que contiene actualmente el objeto
## conclusion adicional aqui, modificar una variable de instencia de cualquier objeto no tiene impacto en todos los restantes

# ahora variables de instancias pero privadas

class Example:
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val):
        self.__second = val


obj1 = Example()
obj2 = Example(2)
obj2.set_second(3)
obj3 = Example(4)
obj3.__third = 8  # creado fuera de la clase y es posible y totalmente permisible
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)

"""
{'_Example__first': 1}
{'_Example__first': 2, '_Example__second': 3}
{'_Example__first': 4, '__third': 8}
"""

## cuando se intenta agregar una variable de instencia a un objeto desde cualquier metodo del objeto python maneja :
### coloca un nombre de clase antes del nombre de la variable
### coloca un guion bajo adicional al principio
### asi que first se convierte en _Example__first
### el nombre es completamente accessible fuera de la clase
print(obj1._Example__first)
### no funciona si se agrega una variable fuera del codigo de la clase, se comporta como propriedad ordinaria
print(obj3.__third)


# print(obj1.__first)## AttributeError since does not exist in the class definition

# variable de clase
## es una propriedad que existe en una sola copia y se almacena fuera de cualquier objeto
## nota :
### no existe una variable de instancia si no hay ninguno objeto de la clase
### solo existe una variable de clase en una copia, incluso si no hay objetos den la clase

class ClassVariable:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ClassVariable.counter += 1


first = ClassVariable()
print("counter")
print(first.counter)
second = ClassVariable(2)
print(ClassVariable.counter)
third = ClassVariable(3)
print(ClassVariable.counter)
print("acceder desde objeto variable de clase:")
print(ClassVariable.counter)
print(second.counter)
print(third.counter)
print(first.__dict__)


## instanciacion de la variable counter dentro de la classe pero fuera de cualquiera de sus metodos
## acceder a dicha variable tiene el mismo aspecto que acceder a cualquier atributo de instancia
## la variable de clase no se muestran en el diccionario de un objeto (__dict__)
## la variable de clase siempre presenta mismo valor en todas las instancias de clase (objetos)

class ClassVariable:
    __counter = 0
    count = 0

    def __init__(self, val=1):
        self.__first = val
        ClassVariable.__counter += 1
        self.count = val
        count = val
        print("var local count", count)


print("counter", ClassVariable._ClassVariable__counter)  # ClassVariable.__counter would raise an error
print("count", ClassVariable.count)
classVariable = ClassVariable()
print("count", classVariable.__dict__)


## conclusion
## self.count = val va crear una variable de instancia del mismo nombre
## count = val ca crear un variable local del mismo nombre
## si no variable de instancia, objeto.__dict__ estara vacio

# acceder a un atributo de objeto no existente genera una excepcion AttributeError
## los objetos de Python pueden tener atributos diferentes en comparacion de otras lenguages de programacion
## comprobando que existe el atributo
class Variable:
    def __init__(self, val=1):
        if val % 2 == 0:
            self.a = val
        else:
            self.b = val


m = Variable(1)
n = Variable(0)
a = Variable(2)
b = Variable(3)
c = Variable(4)

if hasattr(a, "a"):
    # el objeto en primer posicion y una cadena que contiene el nombre del atributo para buscar
    print("si tiena atributo a el objeto a", a.a)
else:
    print("no existe a en a")

if hasattr(n, "b"):
    print("si tienen atributo b el objeto n", n.b)
else:
    print("no existe b en n ")

print(0 % 2)


# comprobar existencia en variable de clase
class Var:
    tar = 0

    def __init__(self, val=1):
        self.var = val


obj = Var(1)
if hasattr(Var, "tar"):
    print("si existe tar en la clase Var", Var.tar)
else:
    print("no existe tar en la clase Var")
if hasattr(obj, "tar"):
    print("si existe tar en el objeto obj", obj.tar)
else:
    print("no existe tar en el objeto obj")


class Prueba:
    prueba = 0

    def __init__(self, val=1):
        self.prueba = val


prueba = Prueba(1)
print(prueba.prueba)  # instance shadows class
print(Prueba.prueba)
del prueba.prueba  # deleting it so now classe var is not shadowed
print(prueba.prueba)  # print 0 because it is the class variable

