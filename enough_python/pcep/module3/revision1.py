var = 0
if var:
    print("true")
else:
    print("false")

#
var = 0
if var:
    print("true")
else:
    print("false")

val = 2
while val < 5:
    print(val)
    val += 1
    if val == 5:
        break
else:
    print("else", val)  # not shown since salto del bucle por la instruccion azucarada break

for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("elseelse", i)

for j in range(17, 3):
    print(i)
    if j == 4:
        break
else:
    print("elseelseelse", j)
