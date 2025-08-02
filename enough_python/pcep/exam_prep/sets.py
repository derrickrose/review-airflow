# adding a value to a set
var = {1, 2, 3}
var.add(4)
print(var)

# adding an existing value to a set
## print None
print("here adding an existing value", var.add(4))
print(var)

# removing value from a set
## print None
print(var.remove(1))
print(var)

# removing a non existing value from a set
## KeyError
# print(var.remove(100))

# multiple names referring to the same set
var = {1, 2, 3}
var2 = var
print(var2)
var2.add(4)
# var and var2 are 2 names of the same set (same as on lists and dicos)
print(var)

# copying values to another set
var = {1, 2, 3}
var2 = var.copy()
print(var2)
var2.add(4)
print(var)
## here var2 is different from var
## still same memory instance for the nested objects
## for nested objects, might use deepcopy
print(var2)

# attributes in a set
print(hasattr(set, "add"))
print(hasattr(set, "remove"))
print(hasattr(set, "copy"))
print(hasattr(set, "clear"))
print(hasattr(set, "pop"))
help(set.pop)
print(hasattr(set, "update"))
help(set.update)
s = {1, 2, 3}
s.update({4, 5, 6})
print(s)
print(hasattr(set, "intersection_update"))
help(set.intersection_update)
s = {1, 2, 3}
s2 = {4, 5, 6}
print("s2", s2)
s.intersection_update(s2)
print(s)
print(hasattr(set, "difference_update"))
help(set.difference_update)
print(hasattr(set, "symmetric_difference_update"))
help(set.symmetric_difference_update)
s.symmetric_difference_update(s2)
print(s)
print(hasattr(set, "issubset"))
s = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
print("issubset", s.issubset(s2))
print(hasattr(set, "issuperset"))
print("issuperset", s2.issuperset(s))
print(hasattr(set, "isdisjoint"))
print(hasattr(set, "union"))
print(hasattr(set, "intersection"))
print(hasattr(set, "difference"))
print(hasattr(set, "symmetric_difference"))

