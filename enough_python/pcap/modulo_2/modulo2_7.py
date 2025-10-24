# anatomia de las excepciones
## cuanto mas cerca de la raiz se encuentra la exception mas es abstrata
## al contrario si la excepcion se encuentra en su extremo (digamos la hoja) es concreta

r""""
                         base exception
  ___________________________|_____________________________
  |                          |                           |
SystemExit                 Exception              KeyboardInterrupt
                        /    |        \
            ValueError  LookupError  ArithmeticError
                     ______|_______            |
                     |           |             |
                IndexError  KeyError   ZeroDivisionError

"""

## las flechas siempre apuntan a la entidad mas general
## nota si cambiamos la exception con su clase mas abstrata, sigue funcionando el codigo
try:
    print(1 / 0)
except ArithmeticError:
    print("division por cero arith")
except Exception:
    print("division por cero except")
except BaseException:
    print("division por cero base")
except ZeroDivisionError:
    print("division por cero zerodiv")

## nota que el cacheo se para en la primera coincidencia, no es necesaria que la coincidencia sea exacta
## significa esto que si BaseException viene primero va funcionar y los de mas abajo no va servir
## no poner una excepcion mas general antes de otras mas concretas
try:
    print(1 / 0)
except (BaseException, ArithmeticError) as e:
    if isinstance(e, ArithmeticError):
        print("div por cero arith")
    if isinstance(e, BaseException):
        print("div por cero base")


def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema Aritmético!")
    return None


bad_fun(0)

print("FIN.")


## una excepcion puede ser resuelto dentro de una funcion
## al igual que fuera de una funcion
## en el lugar del problema o si no python va buscar la linea donde llamo la funcion
## si no hay parte del codigo que lo resuelva va actuar como la manera estandar
## terminando el codigo y emitiendo error mensaje de diagnostico

# raise
## la palabra raise genera exepcion como si fuera de manera natural
## raise es una palabra clave reservada
### simular excepciones reales
### parcialmente manejar una excepcion y hacer que otra parte del codigo sea responsable de completar el manejo
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")


## raise tambien se puede escribir sin el nombre de la excepcion pero solo dentro de un block except
def bad_fun(n):
    try:
        return 1 / n
    except:
        print("lo he hecho")
        raise  # aqui va volver a enerar la misma excepcion


try:
    bad_fun(0)
except ZeroDivisionError:
    print("exepcion cacheada")

# assert (afirmar) tambien es una palabra clave
## syntaxis assert expression
## si la expression se evalua verdadera:
### True o diferente a zero, cadena no vacia, arreglo no vacio o cualquiera expression no hace nada
## si la expression se evalua falsa, va generar una excepcion AssertionError

## se utiliza en parte de codigo donde quieres estar absolutamente a salvo de datos incorrectos
## y donde no estas absolutamente seguro de que los datos hayan sido examinados cuidadosamente
## el generar una excepcion AssertionError asegura que tu codigo no produzca resultados no validos
### y muestra claramente la naturaleza de la falla
## las aserciones no reemplazan las excepciones ni validan los datos, son suplementos
import math

x = "-1"
x = float(x)

# assert x >= 0.0 # asi es como usarlo
# x = math.sqrt(x)
# print(x)
