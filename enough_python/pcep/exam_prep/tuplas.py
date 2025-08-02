# las tuplas son inmutables

# caso de list dentro de una tupla
tupla = (1, 2, [3, 4])
print(tupla)
## la lista dentro de la tupla si se puede modificar
tupla[2].append(100)
print(tupla)

var = 1,
print(var)
var = (1,)
print(var)

var = 1, 2, 3
var2 = var[3:]
for i in var2:
    var*=2
print(var)

