# herencia
## manera de compartir los metodos y atributos de un clase hacia sus subclases

class A:

    def __init__(self, name):
        self.name = name

    def imprimir(self):
        print(self.name)


# aun que no definimos nada en B, la clase por herencia tiene acceso a los atributos y metodos de A
class B(A):
    pass


b = B("B")
b.imprimir()
print(b.name)


# pero ojo, si definimos un constructor en el subclase, tenemos que llamar el constructor de la superclase
## por que no se invoca sola el constructor en este caso (sin el constructor en la subclase, python se encarga
## de llamar el constructor del superclase

class C(A):
    def __init__(self, name):
        pass


c = C("C")


# c.imprimir() AttributeError


# genera un error ya que no definimos nada AttributeError
# print(c.name)

# para arreglar esto, tenemos que llamar el constructor de la superclase, y asignar los valores
class C(A):

    def __init__(self, name):
        super().__init__(name)


c = C("C")
c.imprimir()

########################################################### FUNCIONES

print("isinstance", isinstance(c, C))  # True
print("issubclass", issubclass(C, A))  # True
a = A("")
print("isinstance", isinstance(a, C))  # True
print("issuperclass", isinstance(a, C))  # False ==> una instancia de una superclase no es una instancia de la subclase


######################################################### HERENCIA MULTIPLE

class A:

    def imprimir(self):
        print("A")


class Left(A):

    def imprimir(self):
        print("Left")


class Right(A):
    def imprimir(self):
        print("Right")


class C(Left, Right):
    pass


c = C()
c.imprimir()


# Imprime right por que aun class C no redefine el metodo imprimir ,
# su valor lo tiene de Left (su super clase directa)
# es por el MRO (method resolution order) quien dice que es de izquierda a derecha por mismo nivel, de bajo arriba

########################################################"

# un problema de python el salto
# Tata <- Tete  <- Titi
#                    |
#      <--------------


class Tata:
    def imprimir(self):
        print("Toto")


class Tete(Tata):
    def imprimir(self):
        print("Tete")


# class Titi(Tata, Tete):
#     def imprimir(self):
#         print("Titi")


# titi = Titi()
# titi.imprimir()

# error TypeError
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Tata, Tete

# to fix the promblem, we have to just revert the subclases of Titi
# put that Tete come first

class Titi(Tete, Tata):
    pass


## now it is working
titi = Titi()
titi.imprimir()


# diamond problem


#       Beta
# Alpha         Delta
#       Gamma

class Alpha:
    def imprimir(self):
        print("Alpha")


class Beta(Alpha):
    def imprimir(self):
        print("Beta")


class Gamma(Alpha):
    def imprimir(self):
        print("Gamma")


class Delta(Gamma, Beta):
    pass


delta = Delta()
delta.imprimir()

# so MRO for this case is Delta -> then Gama -> then Beta -> then Alpha ...
