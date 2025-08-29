r"""



Given the root of a binary tree, return the number of triangles
A triange is a set of three distinct nodes, a, c, and c where :
    - a is the lowest common ancestor of b and c
    - b and c have the same depth
    - the path from a to b only consits of left children
    - and the path from a to c only consists of right children

        A
      /    \
    B         C
     \       / \
      D     E    F
     / \   /     \
    G  H   I       J
          /  \     /\
        M    K    L   N
"""


class Node:
    def __init__(self, item, parent=None, left=None, right=None):
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.item)

    def set_left(self, left):
        self.left = left
        self.left.parent = self

    def set_right(self, right):
        self.right = right
        self.right.parent = self


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
k = Node("K")
l = Node("L")
m = Node("M")
n = Node("N")

a.set_left(b)
a.set_right(c)
b.set_right(d)
d.set_left(g)
d.set_right(h)
c.set_left(e)
e.set_left(i)
c.set_right(f)
c.set_right(j)
i.set_right(k)
j.set_left(l)
i.set_left(m)
j.set_right(n)


def has_left(node):
    if not node:
        return False
    return node.left is not None


def has_right(node):
    if not node:
        return False
    return node.right is not None


def get_triangles(root):
    if not root:
        return []

    triangles = []

    def visit(node):

        if not node:
            return [], []  # left_children and right_children going downward from the current node
        left_children = []
        right_children = []
        left, _ = visit(node.left)
        _, right = visit(node.right)
        if has_left(node):
            left_children.append(node.left)

        if has_right(node):
            right_children.append(node.right)
        left_children.extend(left)
        right_children.extend(right)
        if left_children and right_children:
            iteration = min(len(left_children), len(right_children))
            for index in range(iteration):
                triangles.append(f"{left_children[index]}-{node}-{right_children[index]}")
        # print(f"{left_children} - {node} - {right_children}")

        return left_children, right_children

    visit(root)
    return triangles


print(get_triangles(a))
