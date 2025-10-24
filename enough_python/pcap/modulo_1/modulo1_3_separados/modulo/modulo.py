#! /usr/bin python3
## la primera linea es un shabang
## que es necesario para los servidores
import sys

for p in sys.path:
    print(p)



""" modulo.py - Un ejemplo de un modulo en Python """  # doc-string
print("me gusta ser un modulo")
print(__name__)
_counter = 0


def suml(the_list):
    global _counter
    _counter += 1
    the_sum = 0
    for i in the_list:
        the_sum += i
    return the_sum


if __name__ == "__main__":
    print("esto es un modulo")
    print("pero puedo hacer unas pruebas")
    a = [i + 1 for i in range(4)]
    print(suml(a) == 10)
