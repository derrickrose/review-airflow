var = 1
print(var != 0)
print(var != 1.)

# reiniciar el bit a la posicion 3 del fin consiste a
val = 7  # 00000111
mask = 4  # 00000100 since my bit is in the third position from end , indice 2 from end
print("checkar mi bit", val & mask)

val = val & ~mask
print("reiniciar mi bit", val)
val = val & -5
print("reiniciar mi bit", val)

# poner 1 a nuestro bit
# restabilicer mi bit
val = 3
val = val | mask
print("poner 1 a mi bit", val)

# negar mi bit
val = 7
mask = 4
# negar mi bit consiste a val ^ mask
val = val ^ mask
print("negar mi bit", val)

# entonces si val es 3 (por que el valor de mi bit es zero), negarlo se vuelve a 7
val = 3
mask = 4
val = val ^ mask
print("negar mi bit", val)

# desplacamiento hacia la izquierda es como multiplicar por 2
val = 7
val <<= 1
print("val << 1", val)

# desplacamiento hacia la derecha es como dividir entero por 2
val = 7
val >>= 1
print("val >> 1", val)
