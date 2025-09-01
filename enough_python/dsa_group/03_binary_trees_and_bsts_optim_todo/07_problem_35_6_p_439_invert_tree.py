r"""
Given a binary tree, invert it by modifying the left and right pointers (do not modify the values in the nodes or create new nodes).
The left subtree of the root should become the right subtree inverted, and the right subtree of the root should become the left
subtree inverted. Return the root of the the tree after modifying it.

             1                              1
          /    \                         /     \
        6       7                       7       6
      /  \     /                         \     /  \
    4    11   2                           2   11    4
     \         \                         /         /
     5          9                       9        5

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


uno = Node(1)
dos = Node(2)
cuatro = Node(4)
cinco = Node(5)
seis = Node(6)
siete = Node(7)
nueve = Node(9)
diez = Node(10)
once = Node(11)

uno.set_left(seis)
uno.set_right(siete)
seis.set_left(cuatro)
seis.set_right(once)
cuatro.set_right(cinco)
siete.set_left(dos)
dos.set_right(nueve)


def preorder(node):
    if not node:
        return []
    return [node.item] + preorder(node.left) + preorder(node.right)


def invert_tree(root):
    if not root:
        return None

    def visit(node):
        if not node:
            return None
        left = visit(node.left)
        right = visit(node.right)
        node.set_left(right)
        node.set_right(left)
        return node

    return visit(root)


print(preorder(uno))
print(preorder(invert_tree(uno)))
