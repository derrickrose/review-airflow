r"""
You are given the root of a non-empty binary tree.
We lay out the tree on a drid as follows :
    - we put the root at (r,c) = (0,0)
    - we recursively lay out the left subtree one unit below the root (increasing r by one)
    - we recursively lay out the right subtree one unit to the root's right (increasing c by one)
For instance, the left child of the root goes on (1,0) and the right child goes on (0,1)

Two nodes are stacked if they are lai on the same (r,c) coordinates.
Return the maximum number of stacked nodes on the same coordinate.

          1
       /   \
    2        3
  /  \      /
 4    5    6
  \       / \
  7      8   9


"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

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

uno.set_left(dos)
uno.set_right(tres)
dos.set_left(cuatro)
dos.set_right(cinco)
cuatro.set_right(siete)
tres.set_left(seis)
seis.set_left(ocho)
seis.set_right(nueve)

from collections import defaultdict


def get_max_stacked(root):
    if not root:
        return 0

    storage = defaultdict(list)  # { (r,c) : [] }
    maximum = 0

    def visit(node, r, c) -> None:
        if not node:
            return
        storage[(r, c)].append(node)
        nonlocal maximum
        if len(storage[(r, c)]) >= maximum:
            maximum = len(storage[(r, c)])
        visit(node.left, r+1, c)
        visit(node.right, r, c+1)

    visit(root, 0, 0)

    return maximum
print(get_max_stacked(uno))

