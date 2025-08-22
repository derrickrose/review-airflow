r"""

Given a binary tree, we say a node is aligned if its value is the same as its depth.
Return the longest chain of aligned nodes (downward and upward).
The chain does not need to start at the root.

Example:

depth 0             A0
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

Output: 7. The longest chain of aligned nodes is (7) 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 2 [K,J,I,H,E,B,D]

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


a = Node("A", 0)
b = Node("B", 1)
c = Node("C", 3)
d = Node("D", 2)
e = Node("E", 2)
f = Node("F", 2)
g = Node("G", 4)
h = Node("H", 3)
i = Node("I", 4)
j = Node("J", 5)
# j = Node("J", 8)
k = Node("K", 6)
l = Node("L", 4)
m = Node("M", 7)

a.set_left(b)
a.set_right(c)
b.set_left(d)
b.set_right(e)
c.set_left(f)
c.set_right(g)
e.set_right(h)
h.set_left(i)
i.set_left(j)
j.set_right(k)
h.set_right(l)
k.set_left(m)


# TODO next check order and try to understand why we have to inverse
# TODO next complexity (time, space) analysis and walk trough the recursions to explain why should I reverse the left path


def get_max_aligned_path(root) -> list:
    if not root:
        return []

    def is_aligned(node, level) -> bool:
        if not node:
            return False
        return node.value == level

    max_path = []

    def visit(node, level) -> tuple[list, list]:
        if not node:
            return [], []  # first list is max_aligned (no consideration of direction) and second list is the arm (max aligned downward only nodes)

        left_max_aligned, left_arm = visit(node.left, level + 1)
        right_max_aligned, right_arm = visit(node.right, level + 1)
        current_max_aligned = left_max_aligned if len(left_max_aligned) >= len(right_max_aligned) else right_max_aligned
        current_arm = left_arm if len(left_arm) >= len(right_arm) else right_arm
        nonlocal max_path
        max_path = current_max_aligned if len(current_max_aligned) >= len(max_path) else max_path

        if not is_aligned(node, level):
            return [], []
        else:
            merged_arm = list(reversed(left_arm)) + [node] + right_arm
            current_arm = [node] + current_arm
            current_max_aligned = merged_arm if len(merged_arm) >= len(current_max_aligned) else merged_arm
            max_path = current_max_aligned if len(current_max_aligned) >= len(max_path) else max_path
            return current_max_aligned, current_arm

    visit(root, 0)
    return max_path


print(get_max_aligned_path(a))
