# class Node:
#     def __init__(self, item, parent=None, left=None, right=None):
#         self.item = item
#         self.parent = parent
#         self.left = left
#         self.right = right
#
#     def __repr__(self):
#         return str(self.item)
#
#
# def set_left(node, left):
#     if node and left:
#         node.left = left
#         left.parent = node
#
#
# def set_right(node, right):
#     if node and right:
#         node.right = right
#         right.parent = node
#
#
# def set_parent(node, parent):
#     if node and parent:
#         node.parent = parent
#
#
# def has_children(node):
#     if not node:
#         return False
#     return node.left is not None or node.right is not None
#
#
# def is_leaf(node):
#     return not has_children(node)
#
#
# def get_children(node):
#     if not node:
#         return []
#     return [child for child in [node.left, node.right] if child]
#
#
# def get_grand_children(node):
#     if not node:
#         return []
#
#     return [gc for child in get_children(node) for gc in get_children(child)]
#
#
# def has_parent(node):
#     if not node:
#         return False
#     return node.parent is not None
#
#
# def get_parent(node):
#     if not has_parent(node):
#         return None
#     return node.parent
#
#
# def get_grand_parent(node):
#     if not node or not node.parent:
#         return None
#     return node.parent.parent
#
#
# def get_ancestors(node):
#     if not node:
#         return []
#     ancestors = []
#     node = node.parent
#     while node:
#         ancestors.append(node)
#         node = node.parent
#     return ancestors
#
#
# def is_root(node):
#     return not has_parent(node)
#
#
# def has_left(node):
#     if not node:
#         return False
#     return node.left is not None
#
#
# def has_right(node):
#     if not node:
#         return False
#     return node.right is not None
#
#
# def get_size(node):
#     if not node:
#         return 0
#     return 1 + get_size(node.left) + get_size(node.right)
#
#
# def get_tree_depth(node):
#     if not node:
#         return 0
#     return 1 + max(get_tree_depth(node.left), get_tree_depth(node.right))
#
#
# def get_level(node):
#     if not node:
#         return 0
#     level = 0
#     while node.parent:
#         node = node.parent
#         level += 1
#     return level
#
#
# def get_lca(node1, node2):
#     if not node1 or not node2:
#         return None
#     level1 = get_level(node1)
#     level2 = get_level(node2)
#     while level1 > level2:
#         node1 = node1.parent
#         level1 -= 1
#     while level2 > level1:
#         node2 = node2.parent
#         level2 -= 1
#     while node1.item != node2.item:
#         node1 = node1.parent
#         node2 = node2.parent
#     return node1
#
#
# def get_distance(node1, node2):
#     if not node1 or not node2:
#         return 0
#     node_lca = get_lca(node1, node2)
#     distance_1 = 0
#     distance_2 = 0
#     while node1.item != node_lca.item:
#         node1 = node1.parent
#         distance_1 += 1
#     while node2.item != node_lca.item:
#         node2 = node2.parent
#         distance_2 += 1
#     return distance_1 + distance_2
#
#
# def preorder(node, visited=None):
#     if not node:
#         return None
#     print(node)
#     if node.left:
#         preorder(node.left, visited)
#     if node.right:
#         preorder(node.right, visited)
#     return None
#
#
# def dfs_preorder(node):
#     if not node:
#         return None
#     print("dfs using preorder")
#     print(node)
#     if node.left:
#         preorder(node.left)
#     if node.right:
#         preorder(node.right)
#     return None
#
#
# # Example tree:
# #        A
# #      /   \
# #     B     C
# #    / \    /
# #   D   E  F
# #  / \      \
# # H   I      G
#
# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")
# f = Node("F")
# g = Node("G")
# h = Node("H")
# i = Node("I")
#
# set_left(a, b)
# set_right(a, c)
# set_left(b, d)
# set_right(b, e)
# set_left(c, f)
# set_left(d, h)
# set_right(d, i)
# set_right(f, g)
#
# print(get_level(a))
# print(get_level(i))
# print(get_lca(h, e))
# print(get_distance(i, g))
# dfs_preorder(a)
#
