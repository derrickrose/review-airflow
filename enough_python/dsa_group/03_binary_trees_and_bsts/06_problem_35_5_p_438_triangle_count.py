r"""


         A
      /     \
    B         C
     \        /\
      D      G   H
    /  \    /     \
  E     F  I       J

Given the root of a binary tree, return the number of triangles
A triange is a set of three distinct nodes, a, c, and c where :
    - a is the lowest common ancestor of b and c
    - b and c have the same depth
    - the path from a to b only consits of left children
    - and the path from a to c only consists of right children

"""


class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.item)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def has_left(node):
    if not node:
        return False
    return node.left is not None


def has_right(node):
    if not node:
        return False
    return node.right is not None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")

a.set_left(b)
a.set_right(c)
b.set_right(d)
d.set_left(e)
d.set_right(f)
c.set_left(g)
c.set_right(h)
g.set_left(i)
h.set_right(j)


def get_triangles(root):
    if not root:
        return []

    storage = {}  # key node, value (left_children, right_children)

    def visit(node):
        if not node:
            return [], []

        left_children = []
        right_children = []
        if has_left(node):
            left_children.append(node.left)
            left = visit(node.left)
            left_children.extend(left[0])
        if has_right(node):
            right_children.append(node.right)
            right = visit(node.right)
            right_children.extend(right[1])
        storage[node] = left_children, right_children
        return left_children, right_children

    visit(root)
    triangles = []
    for key, value in storage.items():  # key a node , value tuple(left_children which is an array, right_children)
        maximum_iteration = min(len(value[0]), len(value[1]))
        for index in range(maximum_iteration):
            triangles.append(f"{value[0][index]}-{key}-{value[1][index]}")
    return triangles


print(get_triangles(a))
