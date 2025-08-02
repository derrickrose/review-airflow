# LEGB rules
## the order python search for variables are
## LOCAL, ENCLOSING, GLOBAL, BUILT-IN
## note: enclosing is outside of current boucle for example

# UnboundLocalError
## x is reachable inside the function
## but it cannot be used in any assignment
## putting x in any assignment python will search for x in local scope
## resulting as an error since the x variable scope is enclosing not local to the function
## x will not be found
x = 1
#

def add():
    print(x)
    # x =2
    return x


print(add())
