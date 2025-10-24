# metodo de clase
## metodo funcion dentro de una clase
## un metodo debe al menos tener un parametro, puede ser que se llama sin argumento pero al menos un parametro (self)
## la razon de self es identificar el objeto para cual el metodo se invoca
## no debes invocal el parametro self al invocar el método
class Classy:
    def method(self):  # un parametro self
        print("Hola, soy un metodo de Classy")


cla = Classy()
cla.method()  # invocarlo sin argumento


## ahora si quieremos que el método se invoca con parametros, debemos colocarlos despues de self
class Classy:
    def method(self, name=""):
        print("Hola", name, ",soy un metodo de Classy")


cla = Classy()
print(cla.method("Baba"))


# metodos de clase existen para acceder a los variables de instancias y de clases
## el parametro self es usado para obtener acceso a la instancia del objeto (las entidades tambien) y las variables de clases
class Classy:
    counter = 0

    def __init__(self, val):
        self.val = val
        Classy.counter += 1

    def get_values(self):
        return self.val, self.counter


cla = Classy(1)
print(cla.get_values())
cla = Classy(1)
print(cla.get_values())


class Classy:
    varia = 2

    def method(self):
        return Classy.varia, self.toto


c = Classy()
c.toto = 3  ## taking this off will raise an AttributeError
print(c.method())


def papita(obj):
    print("popolo is a function outside ")
    return obj.toto


c.papita = papita
print(c.papita(c))
print(c.__dict__)


## tambien se usa el parametro self para invocar otros metodos dentro de la clase
class Classy:
    def method(self):
        print("Hola, soy un metodo de Classy")

    def other_method(self):
        self.method()
        print("Hola, soy otro metodo de Classy")


a = Classy()
a.other_method()


# si se llama __init__ el método, no sera un método regula, sera un constructor
## cuando una clase tiene un constructor, este se invoca automaticamente y implicitamente cuando se instancia el objeto de la clase
## esta obligado a tener el paramétro self
## pudiera (pero no necesariamente) tener mas parametros que solo self
## se puede utilizar para configurar el objeto:
### inicializa adecuadamente su estado interno, crea variables de instancia, crea instancias de cualquier otro objeto si es necesario
## el constructor no puede retornar un valor
## no se puede invocar directamente desde el objeto o desde dentro de la clase
class Classy:
    def __init__(self, val=1):
        self.val = val

    def __hidden(self):  # método parcialmente oculto
        print("hidden")


c = Classy()
# c.__hidden() # AttributeError
c._Classy__hidden()  # imprime hidden


# la vida interna de clases y objetos
## usar __dict__ podremos ver las entidades dentro de una clase un método
## otra entidad __name__, esta ausente dentro del objeto, existe solamente en la clase , es una cadena
## si desea encontrar la clase de un objeto en particular, se puede usar una funcion llamada type(), regresa la clase
## si desear encotrar entonces el nombre de la clase del objeto sera type(obj).__name__
class Classy:
    counter = 0

    def __init__(self, val=1):
        self.val = val
        Classy.counter += 1


c = Classy()
print(c.__dict__)
print(Classy.__dict__)
print(Classy.__name__)
print(type(c))  # <class '__main__.Classy'> (clase)
print(type(c).__name__)  # Classy (cadena)
print(type(type(c).__name__))
# print(c.__name__) AttributeError

# la entidad __module__
## tambien dentro de la clase tenemos una entidad __module__
print(Classy.__module__)  ## __main__
print(c.__module__)  # __main__

## como sabemos el __main__ no es un modulo en si, solamente es donde se ejecuto el proceso
## eso es decir si creamos a lado un archivo que se llama classy.py, creamos dentro la classe Classy, luego importamos aca
## va salir modulo classy ??? pruebamoslo
import classy

c = classy.Classy()
print(type(c))  # debe ver <class 'classy.Classy'> ???
print(type(c).__name__)
print(type(c).__module__)
print(type(c).__dict__)


# entidad __bases__ es una tupla que contiene clases (no nombres) que son superclases directas de la clase
## solo muestra la superclase directa
## solo las clases tienen este atributo, los objetos no
class Classy:
    pass


class Classi(Classy):
    pass


class Classii(Classi):
    pass


class Classiii(Classii, Classy):
    pass


print(Classiii.__bases__)
c = Classiii()  # print(c.__bases__) # AttributeError por que no contenga la entidad
print(Classy.__bases__)  # una clase sin superclases apunta a object, una clase predefinida como su ancestor directo


class Classy:
    counter = 0

    def __init__(self, val=1):
        self.__val = val
        Classy.counter += 1


def get_counter(cls):
    return cls.counter


print("hasattr", hasattr(Classy, "counter"))

c = Classy()
c = Classy()
print("hasattr", hasattr(c, "_Classy__val"))
print(get_counter(type(c)))
print(get_counter(c))


# introspeccion y reflexion
## todo esto permite que el programador de Python realice dos actividades importantes especificas para muchos lenguajes objetivos
### introspeccion : que es la capacidad de un programa para examinar el tipo o las propriedades de un objeto en tiempo de ejecucion
### reflexion : que va un paso mas alla, capacidad de un programa para manipular los valores, propriedades y o funciones de un objeto en tiempo de ejecucion
## en otras palabras no se necesita conocer la definicion completa de la clase/objeto para manipular el objeto, ya que
## el objeto y o su clase contiene los metadatos que permiten reconocer sus caracteristicas durante la ejecucion del programa

# investigando clases
class MyClass:
    def __init__(self, val=1):
        self.val = val
        self.integer = val


def incInt(obj):
    for name in obj.__dict__:
        if name.startswith("i"):
            value = getattr(obj, name)
            print("valor", value)
            setattr(obj, name, value + 1)
            print("valor", getattr(obj, name))


print("-------------------")
incInt(MyClass(0))


# continuar con puntos claves
class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1


class Snake:
    def __init__(self, victims=0):
        self.victims = victims

    def increment(self):
        self.victims += 1


days = ['Lun', 'Mar', 'Mie', "Jue", "Vie", "Sab", "Dom"]
days_map = {i: days[i] for i in range(len(days))}
print(days_map)
days = ['Lun', 'Mar', 'Mie', "Jue", "Vie", "Sab", "Dom"]
week_day_map = {i: days[i] for i in range(len(days))}
days_number_map = {y: x for x, y in week_day_map.items()}
print(days_number_map)
print("here")
print(Classy.counter)
class Classy:
    counter = 0
    counter1 = 1 + Classy.counter

    def __init__(self, val=1):
        self.val = val
        Classy.counter += 1
        Classy.counter1 += 1



c = Classy()
print(c.counter)
print(c.counter1)

# continuar aqui

import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt((x - self.__x) ** 2 + (y - self.__y) ** 2)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getX(), self.getY())
    #

class A:
    pass
a = A()
print(a.__dict__)
print(a.__module__)
# print(a.__bases__)
# print(a.__name__)