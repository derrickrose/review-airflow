# 4 programas simples
# cifrado de cesar
# cambiar el caracter por el que sigue (convertir en punto de codigo, agnadir uno y reconvertir en caracter)
# decifrado (convertir en punto de codigo, quitar uno y reconvertir en caracter
# procesador de numero
# sumar muchos numeros successivos (usa split)
# el iban
# Validador IBAN.

iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")

# algo de busqueda (o comparacion de cadena) hamming and levenshtein
# https://en.wikipedia.org/wiki/Hamming_distance
# https://en.wikipedia.org/wiki/Levenshtein_distance