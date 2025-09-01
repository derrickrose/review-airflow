# class Node:
#     def __init__(self, item, left=None, right=None):
#         self.item = item
#         self.left = left
#         self.right = right
#
#     def __repr__(self):
#         return str(self.item)
#
#
# def is_leaf(node):
#     if not node:
#         return False
#     return node.left is None and node.right is None
#
#
# def has_children(node):
#     if not node:
#         return False
#     return node.left is not None or node.right is not None
#
#
# def get_children(node):
#     if not node:
#         return []
#     return [node.left, node.right]
#
#
# def get_size(node):
#     if not node:
#         return 0
#     size = 1
#     if node.left:
#         size += get_size(node.left)
#     if node.right:
#         size += get_size(node.right)
#     return size
#
#
# def get_level(node):
#     if not node:
#         return 0
#     left_level = 0
#     right_level = 0
#     if node.left:
#         left_level += get_level(node.left)
#     if node.right:
#         right_level += get_level(node.right)
#     return max(left_level, right_level) + 1
#
#
# def get_grand_children(node):
#     if not node:
#         return []
#     return [gc for child in get_children(node) if child for gc in get_children(child) if gc]
#
#
# a = Node("A")
# b = Node("B")
# a.left = b
# c = Node("C")
# a.right = c
# u = Node("U")
# v = Node("V")
# b.left = v
# b.right = u
# w = Node("W")
# x = Node("X")
# v.left = w
# v.right = x
#
# print("a is leaf", is_leaf(a))
# print("a has children", has_children(a))
# print("a children", get_children(a))
# print("a size", get_size(a))
# print("a level", get_level(a))
# print("a grand children", get_grand_children(a))
#
# print("w is leaf", is_leaf(w))
# print("w has children", has_children(w))
# print("w children", get_children(w))
# print("w grand children", get_grand_children(w))
# print("a size", get_size(a))