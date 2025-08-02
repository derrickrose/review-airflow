# tester égalité entre deux float
var = 0.3
x = 0.1
y = 0.2
## false car 0.1+0.2 donne 0.30000000000000004 en python
print(0.1 + 0.2)
## False
print(var == x + y)
## pour tester égalité entre ces 2 valeurs float, on utilise
## cette fois va donner True
print(abs(var - x - y) < 1e-15)

# déclarer des variables sur une seule ligne
## utilisation de mode tuple
a, b, c = 1, 2, 3
print(a, b, c)
## utilisation de semi-colon
a = 10;b = 10;c = 10
print(a, b, c)
## utilisation de égalité
a = b = c = 100
print(a, b, c)

# converting float from string
## built-in function float() can convert any leading or trailing space without error
var = float(" 3.14 ")
print(var)


