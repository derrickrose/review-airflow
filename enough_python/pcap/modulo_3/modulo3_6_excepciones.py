
# todas las excepciones integradas de Python forman una jerarquia de claes
## si deseas puedes extenderlo sin problema
## como un arbol, es un ejemplo perfecto de una estructura de datos recursiva
## imprimir la jerarquia de las excepciones
def print_excepciones(excepcion, indent=0):
    print("| " * indent, excepcion.__name__, sep="")
    val = 0
    for sub in excepcion.__subclasses__():
        val += print_excepciones(sub, indent + 1)
    return val + 1


# print(print_excepciones(BaseException))
from io import UnsupportedOperation

print(UnsupportedOperation.__bases__)