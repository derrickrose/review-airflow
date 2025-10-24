# modulo 2 cadenas, listas errores y excepciones

codigos de caracteres mas utiles
space 32
A 65
a 97
97-65 = 32

resumen

## compu almacenan caracteres como numero

## no hay estandares por eso se implemento el codigo ascii (american standard code for information interchange)

## el ascii almacena los caracteres en ocho bits (256 caracteres)

## al principio usaron los 128 restantes para almacenar otros caracteres

## asi que no es suficiente

## tambien un punto de codigo en ISO/IEC 8859-2 con el mismo numero va ser diferente en ISO/IEC 8859-5

## se implemento unicode para lidiar con esto y contiene millones de caracteres

## pero los primeros 128 siguen siendo los de ascii

## pero unicode no dice como almacenar los caracteres en compu ni en archivo

## por eso viene UCS (universal character set)

## el mas usado es UCS-4

## algoritmo de busqueda

- hamming : https://en.wikipedia.org/wiki/Hamming_distance
- levenshtein : https://en.wikipedia.org/wiki/Hamming_distance
- similitud acustica, ejemplo echo y hecho, este tipo de algo se ha inventado en 1918 soundex : https://en.wikipedia.org/wiki/Soundex
- a veces es mejor almacenar los valores en cadena debido a que la preicision de los datos enteros y flotantes son limitada