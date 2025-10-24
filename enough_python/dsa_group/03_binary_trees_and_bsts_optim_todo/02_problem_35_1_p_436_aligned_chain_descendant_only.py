r"""

Given a binary tree, we say a node is aligned if its value is the same as its depth.
Return the length of the longest descendant chain of aligned nodes.
The chain does not need to start at the root.

Example:

depth 0             A7
                  /    \
depth 1         B1      C3
              /  \      /
depth 2     D2    E8  F2
           / \       /  \
depth 3   G4  H3    I3  J3
                \       /
depth 4         M4     K4
                /     /
depth 5       N5     L5

Output: 5. The longest chain of aligned descendant only nodes is 1 -> 2 -> 3 -> 4 -> 5 [B,D,H,M,N]

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


a = Node(7)
b = Node(1)
c = Node(3)
d = Node(2)
e = Node(8)
f = Node(2)
g = Node(4)
h = Node(3)
i = Node(3)
j = Node(3)
k = Node(4)
l = Node(5)
m = Node(4)
n = Node(5)

a.set_left(b)
a.set_right(c)
b.set_left(d)
b.set_right(e)
d.set_left(g)
d.set_right(h)
h.set_right(m)
m.set_left(n)
c.set_left(f)
f.set_left(i)
f.set_right(j)
j.set_left(k)
k.set_left(l)


def get_max_aligned_chain(root):
    if not root:
        return 0

    def is_aligned(node, level):
        return node and node.value == level

    max_aligned = 0

    def visit(node, level):
        if not node:
            return 0
        nonlocal max_aligned
        left = visit(node.left, level + 1)
        right = visit(node.right, level + 1)
        best = max(left, right)

        if not is_aligned(node, level):
            max_aligned = max(best, max_aligned)
            return 0
        else:
            best += 1
            max_aligned = max(best, max_aligned)
            return best

    visit(root, 0)
    return max_aligned


print(get_max_aligned_chain(a))