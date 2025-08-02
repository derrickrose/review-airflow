class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __repr__(self):
        return self.item

    def __str__(self):
        return self.item

    def has_children(self):
        return self.left is not None or self.right is not None

    def get_children(self):
        return [self.left, self.right]

    def has_grand_children(self):
        return self.left and self.left.has_children() or self.right and self.right.has_children()

    def get_size(self):
        left_size = 0
        right_size = 0
        if self.left:
            left_size = self.left.get_size()
        if self.right:
            right_size = self.right.get_size()
        return left_size + right_size + 1

    def get_depth(self):
        left_depth = 0
        right_depth = 0
        if self.left:
            left_depth = self.left.get_depth()
        if self.right:
            right_depth = self.right.get_depth()
        return max(left_depth, right_depth) + 1

    def get_grand_children(self):
        if self.has_grand_children():
            return [gc for child in self.get_children() if child for gc in child.get_children() if gc]
        return []

    def is_leaf(self):
        return self.left is None and self.right is None


a = Node("A")
b = Node("B")
a.left = b
c = Node("C")
a.right = c
u = Node("U")
b.right = u
v = Node("V")
b.left = v
w = Node("W")
v.left = w
x = Node("X")
v.right = x

print(a.get_size())
print(a.get_depth())
print(a.get_grand_children())
print(v.has_grand_children())
print(a.is_leaf())
print(v.is_leaf())
