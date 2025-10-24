# cadenas en action
# comparacion con los mismos operadores == != > < <= ...
print("alpha" == "alpha")  # True
print("alpha" != "Alpha")  # True
print("alpha" < "alphabet")  # True
print(
    "alpha" > "ALPHA")  # True => majuscula es inferior a minuscula, punto flotante a partir de 65 para mjuscula y 97 or minuscula

print("ALPHA" > "Alpha")

# los digitos no se considera numero
print(
    "100" < "99")  # True por que 1 < 9 pero no se considera 99 y 100  ## en resumen se compara caracter por caracter y el primero que tiene mayor gana
print("199999" < "2")  # True
## asi que comparar cadena con numero siempre devuelve falso
print("1" == 1)
print("1" != 10)

#### print("10" > 10) #TypeError

# ordenamiento
greek = ["omega", "alpha", "pi", "gamma"]
## la primera sorted() , acepta una lista y regresa nueva lista
print(greek)
print(sorted(greek))
print(greek)  # permanece intacta
print(greek.sort())  # cambia directamente la lista, regresa None
print(greek)

# cadenas frente a numeros
## como convertir en numoro entero, flotante, ... de cadenas en entero ? ...
entero = 12
flotante = 12.3
sEntero = str(entero)
sFlotante = str(flotante)
print(sEntero)
print(sFlotante)
## la conversion inversa
### la conversion inversa solo es posible cuando los numeros son digitos validos usando int() y float()
### si el numero no es valido, regresa un error ValueError
print(float(sFlotante))
print(int(sEntero))
###
