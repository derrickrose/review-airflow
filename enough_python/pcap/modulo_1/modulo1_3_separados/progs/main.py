import sys

sys.path.append("../modulo") # funciona si ejecutamos desde la carpeta de inicio
## si no pues habra que usar la ruta completa

import modulo

print("counter", modulo._counter)

print(modulo.suml([1, 2, 3]))
print(modulo.suml([1, 2, 3, 4]))
print("counter", modulo._counter)
