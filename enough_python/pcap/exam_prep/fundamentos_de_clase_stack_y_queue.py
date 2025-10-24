# viaje desde el enfoque procedimental hacia al prientado a objetos
# pila
## colocar monedas
## no puedes poner moneda en ningun otro lugar sino en la parte superior de la pila
## no puedes sacar moneda desde ninguna lugar que no sea la parte superior de la pila
## si deseas obtener la moneda que se encuentra en la parte inferior, debes eliminar todas las monedas de los niveles superiores
## UEPS (LIFO last in first out) ultimo en entrar primera en salir
## una pila es un objeto con dos operaciones elementales,
### push (una moneda es colocada en la parte superior)
### pop (una moneda se retira de la parte superior )

# pila enfoque procedimental
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(5)
push(10)
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)


# pila enfoque procedimental frente al enfoque orientado a objetos
## la pila procedimental ya esta lista pero presente vulnerabilidades
## la variable stack se puede modificar por cualquiera
## si quieres mas que una pila, tambien vas a necesitar crear una varibale stack mas y mas funciones
## tambien puede ocurir que no solo necesitas funciones push() y pop()
## pero intenta imagina que si necitas una dozena (duplicacion de codigo)
## ==> el enfoque orientado a objeto soluciona cada uno de los problemas mencionados anterior

# enfoque orientado objetos
## ocultar (proteger) los valores contra el acceso no autorizado (encapsulamiento)
### no se puede acceder tampoco modificar los valores encapsulados
## cuando se necesita mas que una pila (teniendo la clase que implemento todos los aspectos deseados, pudes duplicar)
## cuando se necesita mas funcionamientos que push() y pop()

class Stack:  # definiendo la clase de la pila
    def __init__(self):  # definiendo la funcion de constructor
        # se puede agregar tantas propriedades que quiere y se va reflejar en cada instancion
        self.__items = []  # el doble guiones bajos para decir que es oculto

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        val = self.__items[-1]
        del self.__items[-1]
        return val


stack = Stack()  # instanciando objeto
## va provocar AttributeError por que con esos 2 guiones bajos, el atributo es oculto del mundo exterior
# print(stack.__items)  # acceder a un entidad del objeto con punto
stack.push(3)  # print(len(stack.__items))
stack1 = Stack()
stack1.push(5)


# subclase
## otra pila para sumir los elementos
## push no solo agnade el valor pero tambien sum los valores
## pop tambien reste el valor de la variable sum
## self es solo invocar un metodo dentro de la clase, afuera con solo un punto, y self tiene que ser primer argumento
class AddingStack(Stack):  # herede de stack
    def __init__(self):
        Stack.__init__(self)  # iniciacion de la superclase y obligatorio hacerlo, recomendada viene primero
        self.__sum = 0

    def push(self,
             item):  # la funcion push() ha sido anulado, el mismo nombre en la superclase ahora representa una funcionalidad diferente
        print("adding", item)
        self.__sum += item
        Stack.push(self, item)  ## para evitar que se confunde con cualquier otra funcion que tiene mismo nombre

    def pop(self):
        val = Stack.pop(self)
        print("removing last", val)
        self.__sum -= val
        return val

    def sum(self):
        print("valor actual", self.__sum)
        return self.__sum


add_stack = AddingStack()
add_stack.push(3)
add_stack.push(5)
add_stack.push(10)
print(add_stack.sum())
print(add_stack.pop())
print(add_stack.sum())


# resumen
## metodo de clase es una funcion dentro de la clase capaz de acceder a cualquiera propriedad de la clase

# una cola queue
class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    def __init__(self):
        IndexError.__init__(self, "Error de Cola")


class Queue:
    def __init__(self):
        self.__items = []  # # Escribe código aquí.  #

    def put(self, elem):
        self.__items.insert(0, elem)  # # Escribe código aquí.  #

    def get(self):
        try:
            val = self.__items[-1]
            del self.__items[-1]
            return val
        except QueueError as e:
            print(e.__cause__)


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")

