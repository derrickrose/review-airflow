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
    def __init__(self, item, value, parent=None):
        self.item = item
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return str(self.item)

    def set_left(self, left):
        self.left = left
        left.parent = self

    def set_right(self, right):
        self.right = right
        right.parent = self


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


class Path:
    def __init__(self, tail=None, head=None, tail_level=-1, head_level=-1, length=0):
        self.tail = tail
        self.head = head
        self.tail_level = tail_level
        self.head_level = head_level
        self.length = length

    def __repr__(self):
        return f"Path {self.tail} {self.tail_level} to {self.head} {self.head_level} {self.length}"


def get_max_aligned(root):
    if not root:
        return []

    def is_aligned(node, level):
        if not node:
            return False
        return node.value == level

    max_aligned = Path()

    def visit(node, level):
        if not node:
            return Path()
        left = visit(node.left, level + 1)
        right = visit(node.right, level + 1)
        current_max = left if left.length >= right.length else right

        nonlocal max_aligned
        if not is_aligned(node, level):
            max_aligned = current_max if current_max.length >= max_aligned.length else max_aligned
            return Path()
        else:
            new_max = Path()
            new_max.tail = current_max.tail if current_max.tail_level != -1 else node
            new_max.head = current_max.head if (
                    current_max.head_level != -1 and current_max.head_level < level) else node
            new_max.tail_level = current_max.tail_level if current_max.tail_level > level else level
            new_max.head_level = current_max.head_level if (
                    current_max.head_level != -1 and current_max.head_level < level) else level
            new_max.length = current_max.length + 1 if current_max.length > 0 else 1

            max_aligned = new_max if new_max.length >= max_aligned.length else max_aligned
            return new_max

    visit(root, 0)
    def rebuild_path(path):
        if not path:
            return []
        path_list = []
        current_node = path.tail
        while current_node != path.head:
            path_list.append(current_node)
            current_node = current_node.parent
        path_list.append(path.head)
        return path_list


    return rebuild_path(max_aligned)


print(get_max_aligned(a))
