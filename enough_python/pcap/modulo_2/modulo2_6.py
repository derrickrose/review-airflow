# errores, fallas, y otras plagas
## ejemplo math.sqrt(-1) o usuario ingresa un valor no numerico
import math

print(math.sqrt(.1))
print(0.31622776601683794 ** 2)

## cada vez que el codigo encuentra algo erroneo, python hace dos cosas
### detiene el codigo
### genera nueva entidad que se llama excepcion
## que ocura despues ?
### python espera que alguien o algo lo note y haga algo al respecto
### si la excepcion no es resuelta, el programa sera terminado abruptamenete y veremos un mensaje de error enviado a la consola por python
### de otra manera si se atiende la excepcion y es manejada apropriadamente, el programa puede reanudarse y su ejecucion puede continuar
## python proporciona herramientas efectivas que permiten observar, identificar y manejar las excepciones eficientemente
## esto es posible debido a todas las excepciones potenciales tienen un nombre especifico, por lo que se pueden clasificar y reaccionar a elles adecuadamente

ZeroDivisionError
IndexError
KeyboardInterrupt

# como manejar excepciones
## con palabra clave try except
## pero no sera mejor verificar todo?
## => no por que podria salir muy largo el codigo
## el orden de cacheo de las excepciones no importa
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")
