import module

print(module.sum())

import module
import importlib

importlib.reload(module)
print(module.sum())
import sys

print(sys.modules)

print("importando modulo dentro de main")
import mod

mod.f()

from mod import __name__ as nom

print("package", mod.__package__)
print(nom)
print(dir(mod))


import __init__
print(__init__.__name__)


print(sys.path)