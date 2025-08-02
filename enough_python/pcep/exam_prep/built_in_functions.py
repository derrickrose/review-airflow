# built-in function help()
## to display documentation about python objects like class, function and module
help(list)

# built-in function divmod()
## divmod() will display the division integer and the rest of the division
## e.g. this should print 3 and 1 as a tuple
print(divmod(10, 3))

# built-in function zip()
## check on arrays module

# built-in function sorted()
## check on arrays module

# built-in function hasattr()
arr = [1, 2, 3]
print(hasattr(list, "append"))
print(hasattr(list, "clear"))
print(hasattr(list, "pop"))
print(hasattr(list, "reverse"))
print(hasattr(list, "sort"))
print(hasattr(list, "copy"))
print(hasattr(list, "insert"))
print(hasattr(list, "extend"))
arr.extend([4, 5, 6])
print(arr)
print(hasattr(list, "remove"))
print(hasattr(list, "index"))
print(hasattr(list, "count"))

# what is the built-in function repr() for
# return the formal representation of an object as string
help(repr)
obj = [1, 2, 3]
print(eval(repr(obj)) == obj)

# built-in id() is to return the logical id of an object
print(id(obj))
print(id(arr))

# built-in bool() is to return the logical value of an object
print(bool(obj))

# check when to use exec() and eval()