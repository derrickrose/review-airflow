# excepcion una vez mas

## el bloque else solo se ejecuta cuando no hubo ninguno excepcion y siempre
try:
    1 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
else:
    print("No hubo ninguna excepcion")

try:
    1 / 1
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
else:
    print("No hubo ninguna excepcion")

# el bloque finally debe de estar en final siempre
try:
    1 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
else:
    print("No hubo ninguna excepcion")
finally:
    print("Esto siempre se ejecuta")

# las excepciones son clases
## a demas cuando se genera una excepcion, se crea una instancia de un objeto de la clase
## y pasa por todos los niveles de ejecucion del programa buscando el bloque except que
## esta preparado para tratar con la excepcion
## tiene un operador as como identificador y disegnado para capturar la excepcion con el fin de analizar su naturaleza
### nota el alcance del identificador solo es dentro del except y no mas alla
try:
    int("Hola Mundo")
except Exception as e:
    print(e)
    print(e.__str__())


# todas las excepciones integradas de Python forman una jerarquia de clases
## si deseas puedes extenderlo sin problema
## como un arbol, es un ejemplo perfecto de una estructura de datos recursiva
## imprimir la jerarquia de las excepciones
def print_excepciones(excepcion, indent=0):
    print("| " * indent, excepcion.__name__, sep="")
    val = 0
    for sub in excepcion.__subclasses__():
        val += print_excepciones(sub, indent + 1)
    return val + 1


print(print_excepciones(BaseException))


# anatomia detallada de las excepciones
## el BaseException tiene un argumento args (tuple) que contenga argumentos pasados al constructor de la clase
### vacia si no ha estado pasado ningun argumento
def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    # imprime "" : "" : "" por que llamado sin argumentos
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("mi excepción")
except Exception as e:
    # imprime "mi excepción" : "mi excepción" : "mi excepción" por que llamado sin argumentos
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("mi", "excepción")
except Exception as e:
    # imprime ('mi','excepcion') : ('mi','excepcion') : ('mi','excepcion')
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)


# crear su propria excepcion
## puede ser util si trabajas en un modulo complejo que detecta errores y genera excepciones
## y deseas que las excepciones se distingan facilmente de cualquier otra de Python
## hacer que las excepciones son derivadas a las predefinidas
## veas que la clase extende ZeroDivisionError
## y no olvidas que el orden de los bloques except es muy importante
## y tambien la exepcion mas abstracta puede cachear su subclase
class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("peores noticias")
    else:
        raise ZeroDivisionError("malas noticias")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('División entre cero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('Mi división entre cero')
    except ZeroDivisionError:
        print('División entre cero original')


class A:
    def __str__(self):
        return "A"


class B:
    def __str__(self):
        return "B"


class C(A, B):
    pass


o = C()
print(o)


class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')


class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)


try:
    raise Ex("ex")
except Ex as e:
    print(e)


class A:
    def a(self):
        print("a")


class B:
    def a(self):
        print("b")


class C(B, C):
    def c(self):
        self.a()


## para revisar herencia y metodos
## herencia y entidades

o = C()
o.c()


# crear excepciones en dominio de pizza
## crear la base
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese_count, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese_count = cheese_count


def make_pizza(pizza, cheese_count=0):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no hay tal pizza en el menú")
    if cheese_count > 100:
        raise TooMuchCheeseError(pizza, cheese_count, "demasiado queso")
    print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese_count)
        print(tmce.args)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
        print(pe.args)
