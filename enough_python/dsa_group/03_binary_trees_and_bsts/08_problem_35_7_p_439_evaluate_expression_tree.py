r"""

We are given a root of a tree representing an arithmetic expression


class Node:
    def __init__(self, kind, num, children):
        self.kind = kind # One of "sum", "product", "max", "min" or "num"
        self.num = num # Only valid when kind is "num"
        self.children = children #Only valid when kind is not "num"

There are two types of nodes, depending on the value of kind :
    -   Number nodes have "num" as the kind and have no children.
    -   Operation nodes do not have "num" as the kind and have one or more children. There are no null children

This is not a binary tree, as nodes have more than two children. We call this an N-ary tree.

Implement an evaluate() function which evaluates the tree according to the following rules :
    -   The value of a numeric node is its num field, which is an integer
    -   The value of an operation node depends on its kind: it is a sum, product, max or min of the children's values
        (the product of a single value is itself)


                       min 12
                   /       \
                max 12      + 48
              /  |  \          \
           4 4  6 6  + 12        * 48
                     /  \        /   \
                   5 5    77     66     88

"""


class Node:
    def __init__(self, kind, num, children):
        self.kind = kind  # One of "sum", "product", "max", "min" or "num"
        self.num = num  # Only valid when kind is "num"
        self.children = children  # Only valid when kind is not "num"


five = Node("num", 5, None)
seven = Node("num", 7, None)
sum1 = Node("sum", None, [five, seven])
four = Node("num", 4, None)
six1 = Node("num", 6, None)
max1 = Node("max", None, [four, six1, sum1])
six2 = Node("num", 6, None)
eight = Node("num", 8, None)
product = Node("product", None, [six2, eight])
sum2 = Node("sum", None, [product])
min1 = Node("min", None, [max1, sum2])


def evaluate(node):
    if node.kind == "num":
        return node.num
    evaluated = list(map( lambda x : evaluate(x), node.children))
    if node.kind == "max":
        return max(evaluated)
    if node.kind == "min":
        return min(evaluated)
    if node.kind == "sum":
        return sum(evaluated)
    if node.kind == "product":
        value = 1
        for val in evaluated:
            value *= val
        return value
    return 0


print(evaluate(min1))
