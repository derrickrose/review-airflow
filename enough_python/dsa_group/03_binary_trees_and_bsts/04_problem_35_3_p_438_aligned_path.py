r"""

Given a binary tree, we say a node is aligned if its value is the same as its depth.
Return the length of the longest descendant chain of aligned nodes.
The chain does not need to start at the root.

Example:

depth 0             A7
                  /    \
depth 1         B1      C3
              /  \      /
depth 2     D2    E2  F2
           / \       /  \
depth 3   G4  H3    I3  J3
                \       /
depth 4         M4     K4
                 \     /
depth 5           N5   L5

Output: 5. The longest chain of aligned nodes is (6) 5 -> 4 -> 3 -> 2 -> 1 -> 2 [N,M,H,D,B,E]

"""


class Node:
    def __init__(self, item: str, value: int, left=None, right=None):
        self.item = item
        self.value = value
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


a = Node("A", 7)
b = Node("B", 1)
c = Node("C", 3)
d = Node("D", 2)
e = Node("E", 2)
f = Node("F", 2)
g = Node("G", 4)
h = Node("H", 3)
i = Node("I", 3)
j = Node("J", 3)
k = Node("K", 4)
l = Node("L", 5)
m = Node("M", 4)
n = Node("N", 5)

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
k.set_left(l)
m.set_right(n)


def get_path(root: Node):
    if not root:
        return []

    def is_aligned(node, level):
        if not node:
            return False
        return node.value == level

    max_aligned_path = []

    def visit(node, level):
        if not node:
            return []

        left_path = visit(node.left, level + 1)
        right_path = visit(node.right, level + 1)
        current_path = []
        if is_aligned(node, level):
            left_path.reverse()
            left_path.append(node)
            current_path = left_path + right_path
        else:
            current_path = list(reversed(left_path)) if len(left_path) > len(right_path) else right_path

        nonlocal max_aligned_path

        if len(current_path) > len(max_aligned_path):
            max_aligned_path = current_path

        return current_path

    visit(root, 0)

    return max_aligned_path


print(get_path(a))

# TODO next complexity (time, space) analysis and walk trough the recursions to explain why should I reverse the left path
