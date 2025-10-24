# los conceptos basicos del enfoque orientado a objetos
## el desarrollo procedimental es mas viejo que orientado a objeto
## orientado a objeto es util para proyecto grande donde trabajan muchos desarrolladores y facilita dividir en partes
## python es a la ves procedimental y orientado a objeto

# enfoque procedimental frente al enfoque orientado a objetos
## en el enfoque procedimental, los datos y los codigos son 2 mundos a parte y datos no usan funciones pero funciones usan datos
## en el enfoque objeto, los datos pueden usar metodos
## en el enfoque orientado a objetos, los datos y el codigo estan encapsulados juntos en el mismo mundo, divididos en clases
## cada clase es como una receta que se puede usar cuando quieres crear un objeto util. ilimitados de objetos
## cada objeto tiene un conjunto de rasgos (se denominan propriedades o atributos, usaremos ambas palabras como sinonimos)
## y es capaz de realizar un conjunto de actividades (que se denominan métodos)
## las recetas pueden modificarse si son inadecuadas para fines especificos y en efecto pueden crearse nuevas clases
## estas nuevas clases heredan propriedades y metodos de los originales, y generalmente agregan nuevos, creando nuevas herramientas mas especificas
## UpperClass
## MiddleClass
## LowerClass

# jerarquias de clase
## intentaremos senalar algunas clases que son buenos ejemplos de este concepto

r"""
            vehiculos
               |_____________________________________________________________
               |                      |                  |                   |
    vehiculos terrestres   vehiculos acuaticos   vehiculos aereos   vehiculos espaciales
                |
         ______|____________________________________
        |                    |                    |
    con ruedas       vehiculos oruga       aerodeslizadores
"""

## todos los vehiculos estan relacionados por una sola caracteristica importante: la capacidad de moverse
## clase vehiculos es una superclase
## las de mas son subclases (descendientes)
## toman en cuenta la direccion de las flechas, siempre apuntan a la superclase

# otro ejemplo de jerarquias: el reino taxonomico de los animales

r"""
            animales
     __________|____________________________
     |              |        |       |      |
    mamiferos   reptiles    aves   peces   anfibios 
        |_________________________
        |                        |
    mamiferos salvajes   mamiferos domesticados

"""


# que es un objeto?
## una encarnacion de los requisitos, rasgos y cualidades asignados a una clase especifica pero toman en cuenta le jerarquia
## esto significa que un objeto que partenece a una clase especifica partenece a todas las superclases al mismo tiempo
## tambien un objeto perteneciente a una superclasse puede no pertenecer a ninguna de sus subclases
## ten en cuenta que hemos supuesto que una clase solo puede tener una superclase, esto no siempre es cierto, pero discutiremos al respeto

# herencia
# cualquier objeto hereda todos los rasgos definidos dentro de cualquiera de sus superclases

# que contiene un objeto
## tres grupos de atributos
### nombre que lo identifica de forma exclusiva dentro de su namespace (aun que hay objetos anonimos)
### conjunto de propriedades individuales (aun que algunos objetos no tengan propriedades)
### conjunto de habilidades para realizar actividades especificas (capaz de cambiar el objeto en si, o algunos de los otros objetos)
## existe una pista (aunque esto no siempre funciona) que ayuda a identificar cualquiera de las tres esferas anteriores :
### un sustantivo : el nombre del objeto
### un adjetivo : probalemenente se esta definiendo una propriedad del objeto
### un verbo : probablemente se esta definiendo una actividad del objeto

# ejemplos
## un cadillac rosa paso rapidamente
### nombre del objeto cadillac
### clase vehiculos con ruedas
### propriedad color rosa
### actividad pasar rapidamente

# mas ejemplos
## Max es un gato grande que duerme todo el dia
### nombre max
### clase gato
### propriedad tamano grande
### actividad dormir (todo el dia)

# primer clase
class TheSimplestClass:
    pass


# primer objeto
## el nombre de la clase intenta fingir que es una funcion
## la clase recien definida se convierte en herramienta pa crear objetos
## el objeto definido contiene todo lo que trae la clase, como esta vacia, el objeto tambien
## el acto de crear un objeto de la clase seleccionada tambien se llama instanciacion (ya que el objeto se convierte en una instencia de la clase)
my_first_object = TheSimplestClass()


####################################### VARIABLE DE CLASE y DE INSTANCIA


# variable de classe y variable de instancia
class A:
    counter = 0

    def __init__(self, name):
        self.name = name
        A.counter += 1  # sin mencionar A. al crear la clase va surgir un error UnboundLocalError


a = A("a")
b = A("B")
## counter variable de clase por que no cambia en ninguna instancia hasta la classe
print(A.counter)
print(a.counter)
## no es visible en las instancias
print(a.__dict__)  # {'name': 'a'}
print(A.__dict__)  # {'__module__': '__main__', 'counter': 2, ....
print(A.counter)


# public, protected, private attributes
class B:
    public = 0
    _protected = 0
    __private = 0

    def __init__(self, public="b", protected="b", private="b"):
        self.public = public
        self._protected = protected
        self.__private = private
        B.public += 1
        B._protected += 1
        B.__private += 1


def protected(self):
    return self._protected


b = B()
b1 = B("b1", "b1", "b1")
b2 = B("b2", "b2", "b2")
print(b.__dict__)  # {'public': 'b', '_protected': 'b', '_B__private': 'b'}
# tambien se puede anadir atributos
b.toto = "toto"
print(b.__dict__)  # {'public': 'b', '_protected': 'b', '_B__private': 'b', 'toto': 'toto'}
print(b1.__dict__)  # {'public': 'b1', '_protected': 'b1', '_B__private': 'b1'} no afecta las de mas instencia
## asi que para acceder a un variable de instancia public le damos b.public, parecido a protected, b.protected,
## pero algo especial para privado b._B__privado (objeto._Classe__variableprivado)
print(b1.public)
print(b1._protected)
print(b1._B__private)  # b1.__private # AttributeError
print(B.public)  # 3 con la clase si tenemos el valor correcto de variable de clase
print(b.public)  # b la variable de instancia gana
print(
    B.__dict__)  # {'__module__': '__main__', 'public': 3, '_protected': 3, '_B__private': 3, '__init__': <function B.__init__ at 0x74250521d260>, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None}

###################################################### funciones y attributos predeterminados

# hasattr()
print(hasattr(b, "toto"))  # True
print(hasattr(B, "public"))  # True
print(hasattr(B, "toto"))  # False


class C:
    counter = 0


my_c = C()
print(hasattr(my_c, "counter"))  # True
print(C.__dict__)
print(hasattr(C, "counter"))  # True
print(my_c.__dict__)

# getattr()
if hasattr(my_c, "counter"):
    print("si existe counter en el objeto")
    print(getattr(my_c, "counter"))
# getattr(C, "countera") AttributeError when no existe
if hasattr(C, "countera"):
    print("si existe countera en la clase")
else:
    print("no existe countera en la clase")

# isinstance()
print(isinstance(my_c, C))  # True

print("counter", my_c.counter)  # accessible when reading 0
# del my_c.counter AttributeError
print(my_c.__dict__)

del C.counter
# print(my_c.counter)  # AttributeError since deleted from class


print(C.__class__)  # type
print(C.__bases__)  # (<class 'object'>, ) # recuperar los super clase
# print(my_c.__bases__) AttributeError
print(C.__name__)  # C
print(C.__module__)  # __main__
print(my_c.__class__)  # <class '__main__.C'>
print(my_c.__class__.__name__)  # C
print(my_c.__module__)  # __main__


# print(my_c.__name__)  # AttributeError


############################################################ metodo de clase

## acceder a un metodo dentro de la clase se usa igual self como los atributos
## self.name, self.__str___
class D:
    def __init__(self, name="desconocido"):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"D('{self.__str__}')"

    def imprimir(self):
        print(self.name)

    def __imprimir_oculta(self):
        print("soy oculto")


d = D()
print(d)

print(d.__str__())
print(d.__repr__())
print(d.imprimir())

## acceder a un metodo oculto
## misma manera que los atributos cuando empieza con 2 guiones bajo se comporta como si fuera oculta
## entonces la manera de acceder en aquella entidad es igual con _Clase__metodo()
print(d._D__imprimir_oculta())

################################################################### introspection et reflexion


# introspeccion y reflexion
## todo esto permite que el programador de Python realice dos actividades importantes especificas para muchos lenguajes objetivos
### introspeccion : que es la capacidad de un programa para examinar el tipo o las propriedades de un objeto en tiempo de ejecucion
### reflexion : que va un paso mas alla, capacidad de un programa para manipular los valores, propriedades y o funciones de un objeto en tiempo de ejecucion
## en otras palabras no se necesita conocer la definicion completa de la clase/objeto para manipular el objeto, ya que
## el objeto y o su clase contiene los metadatos que permiten reconocer sus caracteristicas durante la ejecucion del programa
