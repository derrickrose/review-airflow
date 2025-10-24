# excepciones utiles
# excepciones integradas

## ArithmeticError
### BaseException <- Exception <- ArithmeticError
### excepcion abstracta que incluye todas las excepciones causadas por operaciones aritmeticas como division cero o dominio invalido

## AssertionError
### BaseException <- Exception <- AssertionError
### una excepcion concreta causada por la instrucion assert cuando su expression se evalua False, None, cero, o cadena vacia

## BaseExcepcion
### BaseExcepcion
### la mas abstracta de todas las excepciones de Python
### except: y except BaseException: son equivalentes

## IndexError
### BaseException <- Exception <- LookupError <- IndexError
### una excepcion concreta se genera cuando se intenta acceder al elemento de una secuencia inexistente (cadena como arreglo)

## KeyboardInterrupt
### BaseException <- KeyboardInterrupt
### una excepcion concreta que se genera cuando el usuario usa un atajo para terminar el programa con CTRL+C

## LookupError
### BaseException <- Exception <- LookupError
### excepcion concreta que contiene las excepciones que se genera cuando intenta acceder a un elemento de una colleccion inexistente

## MemoryError
### BaseException <- Exception <- MemoryError
### excepcion concreta surge cuando la memoria esta saturada

## OverflowError
### BaseException <- Exception <- ArithmeticError <- OverflowError
### excepcion concreta que surge cuando una operacion produce un numero demasiado grande para ser almacenado

## ImportError
### BaseException <- Exception <- StandardError <- ImportError
### excepcion concreta que surge cuando falla una operacion de importacion (paquete no visible, modulo no existente, ...)

## KeyError
### BaseException <- Exception <- LookupError <- KeyError
### excepcion concreta que surge cuando intenta de acceder a un elemento no existente (dict)

## biblioteca estandar de python para las excepciones
## https://docs.python.org/3.6/library/exceptions.html

## mnemonic
## B     baseexception
## KES   keyboardInterrupt, exception, systemexit
## MALAS memoryerror, arithmeticerror, lookuperror, assertionerror, standarderror
## ZOKI zeodivizionerror, overflowerror, keyerror, importerror

