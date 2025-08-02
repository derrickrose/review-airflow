# try catch does have an optional else block which is executed only if there were no exception raised
def dividir(a, b=0):
    try:
        print("-----------------------")
        print("dividir", a, b)
        print(a / b)
    except ZeroDivisionError:
        print("zero division error")
    except:
        print("error")
    else:
        print("else only if no exception raised")
    finally:
        print("finally always executed")


dividir(1)
dividir(1, 1)

# Exception <-- LookupError <-- KeyError

# BaseException <-- SystemExit
## not inherits from Exception

# AttributeError
## will be raised when you try to access an object attribute that is undefined

# ValueError
## e.g. when converting string to float
val = "1s"
## will raise a ValueError since s is not convertible
# print(float(val))
## another example when trying to unpack a tuple
## ValueError: too many values to unpack (expected 2)
tup = (1,2,3)
# a, b = (1, 2, 3)