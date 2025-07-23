arr = [1, 2, 3, 4, 5]
arr.insert(2, 10)
print(arr)

b = arr
print(b)
b[2] = 100
print(arr)

c = arr[:]
print(c)
c[2] = 1000
print(c)
print(arr)

bi_dim = []
for i in range(3):
    arr = []
    for j in range(3):
        arr.append(j)
    bi_dim.append(arr)

print(bi_dim)

tri_dim = []
for i in range(3):
    arr = []
    for j in range(3):
        arr2 = []
        for k in range(3):
            arr2.append(f"{i}{j}{k}")
        arr.append(arr2)
    tri_dim.append(arr)
print(tri_dim)
print(tri_dim[0][0][0])

print("i", i)
print("j", j)
print("k", k)

val = 5
while val > 0:
    print(val)
    val -= 1
    if val == 3:
        break
else:
    print("else", val)

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("elseelse", i)

print(i)

for i in range(5, 0):
    print(i)

print(i)

print("------------------------------")
lista = [0, 1, 2]
lista2 = lista
del lista2[0]
print(lista)
print(lista2)
lista = [0, 1, 2, 1, 3]
print(lista.count(1))
lista2 = lista[:]
print(lista2)
del lista2[0]
print(lista)
print(lista2)

print("while ---------------")
i = 5
while i > 3:
    print(i)
    i -= 1
    if i == 2:
        break
else:
    print("else", i)
print("for ---------------")
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("elseelse", i)
print(i)# last i value 2

for i in range(5, 0):
    print(i)
    if i == 2:
        break
else:
    print("elseelseforelse", i)
