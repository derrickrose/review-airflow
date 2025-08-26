r"""

you are given the root of a non-empty binary tree.
We lay out the tree on a grid as follows:
1. we put the root at (r,c) = (0,0)
2. we recursively lay out the subtree one unit below the root (increasing r by one)
3. we recursively lay out the right subtree one unit to the root's right (increasing c by one)
for instance, the left child of the root goes on (1,0) and the right child of the root goes on (0,1)

two nodes are stacked if they are laid on the same (r,c) coordinates.
return the maximum number of stacked nodes on the same coordinate.


         1
      /     \
    2         3
   /  \        /
  4    5      6
  \    /    /  \
  7   10   8    9





"""
from collections import defaultdict


# brute force

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_left(self, left):
        self.left = left
        left.parent = self

    def set_right(self, right):
        self.right = right
        right.parent = self

    def __repr__(self):
        return str(self.value)


uno = Node(1)
dos = Node(2)
tres = Node(3)
cuatro = Node(4)
cinco = Node(5)
seis = Node(6)
siete = Node(7)
ocho = Node(8)
nueve = Node(9)
diez = Node(10)

uno.set_left(dos)
uno.set_right(tres)
dos.set_left(cuatro)
dos.set_right(cinco)
tres.set_left(seis)
cuatro.set_right(siete)
cinco.set_left(diez)
seis.set_left(ocho)
seis.set_right(nueve)


def get_max_stacked(root):
    if not root:
        return 0, (), []

    storage = defaultdict(list)
    maximum_stacked = 0
    coordinate = ()

    def visit(node, r, c):
        if not node:
            return (), []

        visit(node.left, r + 1, c)
        visit(node.right, r, c + 1)
        storage[(r, c)].append(node)
        nonlocal maximum_stacked, coordinate
        if len(storage[(r, c)]) > maximum_stacked:
            maximum_stacked = len(storage[(r, c)])
            coordinate = (r, c)
        return (r, c), storage[(r, c)]

    visit(root, 0, 0)
    return maximum_stacked, coordinate, storage[coordinate]


print(get_max_stacked(uno))
