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
depth 4         M6     K4
                /     /
depth 5       N5     L5

Output: 5. The longest chain of aligned nodes is 1 -> 2 -> 3 -> 4 -> 5 [B,D,H,M,N]

"""


class Node:
    def __init__(self, item, value):
        self.item = item
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.item)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


a = Node("A", 7)
b = Node("B", 1)
c = Node("C", 3)
d = Node("D", 2)
e = Node("E", 8)
f = Node("F", 2)
g = Node("G", 4)
h = Node("H", 3)
i = Node("I", 3)
j = Node("J", 3)
m = Node("M", 6)
k = Node("K", 4)
n = Node("N", 5)
l = Node("L", 5)

a.set_left(b)
a.set_right(c)
b.set_left(d)
b.set_right(e)
c.set_left(f)
d.set_left(g)
d.set_right(h)
f.set_left(i)
f.set_right(j)
h.set_right(m)
j.set_left(k)
m.set_left(n)
k.set_left(l)

