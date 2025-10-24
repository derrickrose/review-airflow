# herencia
## como se presenta una clase
class Classy:
    pass


c = Classy()
print(c)  # <__main__.Classy object ax 0x....>
print(c.__str__())


## no es muy util como se presenta una clase
## como pudimos ver, la funcion __str__() es lo que esta llamada por print()
## ahora cambiamoslo
class Classy:
    def __str__(self):
        return "Classy"


c = Classy()
print(c)


# herencia, por que y como  ?
## es una practica comun de pasar atributos y metodos de la superclase (definida y existente) a una clase recien creada, llamada subclase
## herencia de dos niveles
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


## Vehicle es superclase de LandVehicle y TrackedVehicle
## LandVehicle es a la vez subclase de Vehicle y superclase de TrackedVehicle
## TrackedVehicle es subclase de LandVehicle tanto como Vehicle

# funcion issubclass()
## una funcion que es capaz de identificar una relacion entre dos clases
print(issubclass(LandVehicle, Vehicle))  # True  # viene primero la clase que queremos preguntar, luego su superclase
print(issubclass(Vehicle, Vehicle))  ## cada clase se considera subclase de si misma

# funcion isinstance()
print(isinstance(c, Classy))  # True # viene primero el objeto que queremos preguntar luego su clase
v = Vehicle()
print(isinstance(v, Vehicle))
print(isinstance(v, LandVehicle))  # False
t = TrackedVehicle()
print(isinstance(t, Vehicle))  # instance tambien de sus superclases

# operador is
## se refiere si el objeto se refiere al otro objeto
c = Classy()
c1 = Classy()
print(c1 is c)  # False
c1 = c
print(c1 is c)  # True por que ya la referencia c1 apunta a c desde la asignacion superior
## de misma manera como las cadenas
print("issssssssssssssssssssssss")
a = "Maria"
b = "MariaJoseph"
print(a is b)  # False
a += "Joseph"  #
print(a is b)  # False
print(a == b)  # True


# herencia de metodo
class Super:
    def __init__(self, var):
        self.__var = var

    def __str__(self):
        return "Mi nombre es " + self.__var


class Sub(Super):
    def __init__(self, var):
        Super.__init__(self, var)


class Sub2(Super):
    def __init__(self, var):
        super().__init__(var)  # acceso con super()


s = Sub("Joseph")
s2 = Sub2("Joseph")
print(s)  ## imprime Mi nombre es Joseph es debido a la herencia con la clase Super
print(s2)


class Sup:
    counter = 1

    def __init__(self, var):
        self.sup = var


class Sub(Sup):
    counterSub = 2

    def __init__(self, var):
        super().__init__(var)

        ### sin la instanciacion de la clase super, no se puede acceder a sus variables de instancias desde un objeto de la subclase
        self.sub = var


sub = Sub("Joseph")
print(sub.counterSub)
print(sub.counter)  # siempre herede de las variables de clase
print(sub.sup)
print(type(sub).__bases__)

# definicion general
## cuando intenta acceder a una entidad de cualquier objeto, python intentara
### encontrarla dentro del objeto mismo
### encontrarla en todas las clases involucradas en la linea de herencia del objeto de abajo hacia arriba
### si ambos intentos fallan, una excepcion AttributeError sera generada

a = Sub("Joseph")
b = Sub("Joseph")
print(a == b)
print(a is b)
print(a.sub == b.sub)


class A:
    def __init__(self, var=1):
        self.a = var

    def check(self):
        print("check")


class B(A):
    def __init__(self, var):
        pass
        super().__init__(var)


d = B(2)
e = A()
print(d.a)
print(e.a)
print(issubclass(B, A))
print(issubclass(type(e), A))
print(isinstance(d, B))
print(isinstance(d, A))
print(isinstance(e, A))
print(isinstance(e, B))
print(hasattr(d, "a"))
print(hasattr(d, "check"))
print(AttributeError.__bases__)


# herencia multiple
class A:
    pass


class B:
    pass


# la clase C tiene 2 superclases, esto significa que C herida de todos los bienes ofrecidos por ambas
class C(A, B):
    pass


c = C()
print(c.__class__)


######### fooling __class__ property
class Toto:
    def __init__(self, var):
        self.toto = var


class Tati:
    def __init__(self, var):
        self.tati = var


toto = Toto(1)
print("toto", toto.toto)
print("toto.__class__", toto.__class__)
toto.__class__ = Tati
print(toto.__class__)
print(toto.toto)
# print(toto.tati)
print(Tati.__dict__)
tati = Tati(2)
print(tati.__dict__)
print(toto.__dict__)
print(isinstance(toto, Toto))
print(isinstance(toto, Tati))
print(hasattr(Tati, "tati"))
print(hasattr(tati, "tati"))
print(isinstance(toto, Tati))
print(isinstance(tati, Tati))
print(hasattr(tati, "tati"))
print(hasattr(toto, "tati"))


######### fooling __class__ property   FIN


# overriding (anulacion)
class A:
    var = 100

    def fun(self):
        return 100


class B(A):
    var = 200

    def fun(self):
        return 200


class C(B):
    val = 200
    pass


c = C()
print(c.var)
print(c.fun())
print(c.val)


class Left:
    var = "left"

    def fun(self):
        return "left"


class Right:
    var = "right"

    def fun(self):
        return "right"


class Sub(Left, Right):
    pass


s = Sub()
print(s.var, s.fun())


## result is fleft left, why ?  ## => orden de busqueda
## python busca las entidades de abajo hacia arriba, (si hay mas de 1 classe en una ruta de herencia, izquierda h derecha
## aqui tenemos Sub(Left, Right), ahora si cambiamos el orden en la definicion de la clase, va cambien igual la salida
class Sub2(Right, Left):
    pass


s2 = Sub2()
print(s2.var, s2.fun())  # ahora right right


# como construir una jerarquia de clases
class One:
    def do_it(self):
        print("doing it de One")

    def do(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("doing it de Two")


one = One()
two = Two()
one.do()  # doing it de One
two.do()  # doing it de Two ????? si por causa de poliformismo (viene de griego polys muchos y morphe forma)  ## la manera de que una misma clase puede tomar varias formas dependiendo de las redefiniciones realizadas por cualquiera de sus subclases
# ## el método, redefinido en cualquiera de las superclases, que cambia el comportamiento de la superclase se llama virtual

# jerarquia de clases

import time


class TrackedVehicle:
    def control_track(self, left, stop):
        pass

    def turn(self, left):
        self.control_track(left, True)
        time.sleep(0.25)
        self.control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(self, left, on):
        pass

    def turn(self, left):
        self.turn_front_wheels(left, True)
        time.sleep(0.25)
        self.turn_front_wheels(left, False)


## cambiar para mejor jerarquia

class Vehicle:

    # aqui es un metodo abstracto ya que no hace casi nada, solo lo tenemos para redefinir despues,
    # abstracto : posibilidad que sera instanciada mas tarde
    def change_direction(self, left, val):
        pass

    def turn(self, left, val):
        self.change_direction(left, val)
        time.sleep(0.25)
        self.change_direction(left, val)


class TrackedVehicle(Vehicle):

    def control_track(self, left, val):
        pass

    def change_direction(self, left, val):
        self.control_track(left, val)


class WheeledVehicle(Vehicle):

    def turn_front_wheels(self, left, val):
        pass

    def change_direction(self, left, val):
        self.turn_front_wheels(left, val)


## ventaja es que se anadir otra forma de giro simplemente modificando el metodo turn()
## asi es como el poliformismo ayuda al desarrollador a mantener el codigo limpio y consistente

# jerarquia de clases, continuacion
## la herencia no es la unica forma de construir clases adaptables. Se puede logral los mismos objetivos (no siempre)
## utilizando una tecnica llamada composicion
## la composicion es el proceso de componer un objeto usando objetos diferentes

## la herencia extiende las capacidades de una clase agregando nuevos componentes y modificando los existentes
### en otras palabaras la recete completa esta contenida dentro de la clase misma y todos sus ancestros, el objeto toma
### todas las partenencias de la clase y las usa
## la composicion proyecta una clase como contenedor capaz de almacenar y usar otros objetos (derivados de otras clases)
### donde cada uno de los objetos implementa una parte del comportamiento de una clase
class Track:
    def control_track(self, left, val):
        print("pistas", left, val)

    def change_direction(self, left, val):
        self.control_track(left, val)


class Wheels:

    def turn_front_wheels(self, left, val):
        print("ruedas", left, val)

    def change_direction(self, left, val):
        self.turn_front_wheels(left, val)


class Vehicle:
    def __init__(self, controler):
        self.controler = controler

    def turn(self, left):
        self.controler.change_direction(left, True)
        time.sleep(0.25)
        self.controler.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Track())
wheeled.turn(True)
tracked.turn(False)


## de este manera, la capacidad de giro del vehiculo se compone de un objeto externo, no implementado dentro de la clase
## vehiculo
## en otras palabras tenemos un vehiculo universal y podemos instalar pistas o ruedas en el

# herencia multiple frente a simple
## herencia multipa dificil de mantener (puede ser ambiguoso)
## viola le principio de responsabilidad unica (ya que forma una clase de dos o mas claes que no se saben nada una de otra)
## enlace de responsabilidad unica
## https://en.wikipedia.org/wiki/Single_responsibility_principle

# orden de resolucion de metodos (MRO)
## es una regla que debes obedecer
class A:
    pass


class B(A):
    pass


# class C(A, B): ## crea un error TypeError
#     pass


## TypeError cannot create a consistent method resolution order por que en la jerarquia,
## se esta salstando el B y pues es que B tambien es super de C
## como cambiar esto, con solo se invierte el orden de los superclases de C(B, A) asi funciona bien
## ya que es de abajo hacia arriba y cuando es herencia multiples, Python lee de izquierda hacia derecha
"""
A <- B <----C
  |_________|
"""


# el problema del diamante
class A:
    pass


class B(A):
    def fun(self):
        print("B")


class C(A):
    def fun(self):
        print("C")


class D(B, C):
    pass


a = D()
a.fun()  ## imprime b aun que ambas clases B y C tienen funcion fun  ## ORM es la respuesta


# usa de super
class A:
    def __str__(self):
        return "A"


class B(A):
    def __str__(self):
        return super().__str__() + "B"  ## utilizar super () para recuperar la superclase mas cercana


c = B()
print(c)


class Dog:
    kennel = 0

    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1

    def __str__(self):
        return self.breed + " dice: ¡Guau!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, corderito!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, intruso!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
print(rocky)

class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + " ¡No me gustan las montañas"


a = LowlandDog("Collie")
print(a)
