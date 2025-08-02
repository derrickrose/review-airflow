# in python, a function is evaluated only once
## it does mean an argument object declared once will always remain in the memory
## e.g.
def addup(val, array=[]):
    array.append(val)
    return array


## the first call will add 1
print(addup(1))
## the second call will add 2 aside 1 (from first call)
print(addup(2))
## same for the third one, so this will print [1,2,3]
print(addup(3))


## same thing for set
def addup_set(val, unique=set()):
    unique.add(val)
    return unique


print(addup_set(1))
print(addup_set(2))
print(addup_set(3))


## same thing for dico
def addup_dico(val, dico={}):
    dico.update({val: val})
    return dico


print(addup_dico(1))
print(addup_dico(2))
print(addup_dico(3))
