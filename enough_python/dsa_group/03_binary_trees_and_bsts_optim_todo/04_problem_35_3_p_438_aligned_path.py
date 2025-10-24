r"""

Given a binary tree, we say a node is aligned if its value is the same as its depth.
Return the longest chain of aligned nodes (downward and upward).
The chain does not need to start at the root.

Example:

depth 0             A10
                  /    \
depth 1         B1      C3
              /  \      / \
depth 2     D2    E2  F2   G4
                   \
depth 3             H3
                  /   \
depth 4        I4      L4
              /
depth 5     J5
              \
depth 6        K6
              /
depth 7     M7

Output: 8. The longest chain of aligned nodes is (8) 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 2 [M,K,J,I,H,E,B,D]

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


a = Node(10)
b = Node(1)
c = Node(3)
d = Node(2)
e = Node(2)
f = Node(2)
g = Node(4)
h = Node(3)
i = Node(4)
j = Node(5)
k = Node(6)
l = Node(4)
m = Node(7)

a.set_left(b)
a.set_right(c)
b.set_left(d)
b.set_right(e)
e.set_right(h)
h.set_left(i)
h.set_right(l)
i.set_left(j)
j.set_right(k)
k.set_left(m)
c.set_left(f)
c.set_right(g)


def max_aligned_path(root):
    if not root:
        return 0

    def is_aligned(node, level):
        return node and node.value == level

    max_aligned = 0

    def visit(node, level):
        if not node:
            return 0
        nonlocal max_aligned
        left_arm = visit(node.left, level + 1)  # integer
        right_arm = visit(node.right, level + 1)
        best = max(left_arm, right_arm)
        if not is_aligned(node, level):
            max_aligned = max(best, max_aligned)
            return 0
        else:
            merged = left_arm + 1 + right_arm
            max_aligned = max(merged, max_aligned)
            return best + 1

    visit(root, 0)

    return max_aligned


print(max_aligned_path(a))










