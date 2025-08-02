# multiplying a string with an int will result a repetition of the string
## "aaa"
print("a" * 3)

# multiplying with a bool
## True is evaluated as 1
print("a" * True)
print("a" * 1)
## False is evaluated as 0
## this will result an empty string
print("|", "python" * False, "|", sep="")
print("|", "python" * 0, "|", sep="")
