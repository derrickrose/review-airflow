class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.item}"

    def __str__(self):
        return f"{self.item} -> {self.left} , {self.right}"

    def has_children(self):
        return self.left or self.right

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_leaf(self):
        return not self.left and not self.right

    def get_children(self):
        return [self.left, self.right]

    #
    # def get_grand_children_flat(self):
    #     return [gc for child in self.get_children() if child for gc in child.get_children()]
    # def get_grand_children(self):
    #     grand_children = []
    #     for child in self.get_children():
    #         if child:
    #             grand_children.extend(child.get_children())
    #     return grand_children

    def get_grand_children(self):
        return [gc if child else None for child in self.get_children() for gc in child.get_children()]

    def get_level(self):
        size = 1
        left_size = 0
        right_size = 0
        if self.left:
            left_size = self.left.get_size()
        if self.right:
            right_size = self.right.get_size()
        return size + max(left_size, right_size)

    def get_size(self):
        size = 1
        if self.left:
            size += self.left.get_size()
        if self.right:
            size += self.right.get_size()
        return size


a = Node("A")
b = Node("B")
c = Node("C")
u = Node("U")
v = Node("V")
w = Node("W")
x = Node("X")

a.left = b
a.right = c
b.left = v
b.right = u
v.left = w
v.right = x

print(a.get_level())
print(a.get_size())
print(a.is_leaf())
print(b.get_children())
print("   __ ")
print(b.get_grand_children())
