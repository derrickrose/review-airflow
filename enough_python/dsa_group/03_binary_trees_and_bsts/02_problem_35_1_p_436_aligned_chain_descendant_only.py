#
#
# class Node:
#     def __init__(self, item, value, left=None, right=None, parent=None):
#         self.item = item
#         self.value = value
#         self.left = left
#         self.right = right
#         self.parent = parent
#
#     def __repr__(self):
#         return str(self.item)
#
#     def set_parent(self, parent):
#         self.parent = parent
#
#     def set_left(self, left):
#         self.left = left
#         left.set_parent(self)
#
#     def set_right(self, right):
#         self.right = right
#         right.set_parent(self)
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
# def has_children(node):
#     if not node:
#         return False
#     return has_left(node) or has_right(node)
#
#
# def has_parent(node):
#     if not node:
#         return False
#     return node.parent is not None
#
#
# def get_children(node):
#     if not node:
#         return None
#     children = []
#     if has_left(node):
#         children.append(node.left)
#     if has_right(node):
#         children.append(node.right)
#     return children
#
#
# def has_grand_children(node):
#     if not node:
#         return False
#     children = get_children(node)
#     if not children:
#         return False
#     for child in children:
#         if has_children(child):
#             return True
#     return False
#
#
# def get_grand_children(node):
#     if not node:
#         return False
#     return [gc for child in get_children(node) for gc in get_children(child)]
#
#
# def get_ancestors(node):
#     if not node:
#         return False
#     if not has_parent(node):
#         return []
#     ancestors = []
#     node = node.parent
#     while node is not None:
#         ancestors.append(node)
#         node = node.parent
#     return ancestors
#
#
# def get_size(node):
#     if not node:
#         return 0
#     return 1 + get_size(node.left) + get_size(node.right)
#
#
# def get_tree_level(node):
#     if not node:
#         return 0
#     left = 1 + get_tree_level(node.left)
#     right = 1 + get_tree_level(node.right)
#     return max(left, right)
#
#
# def get_height(node):
#     if not node:
#         return 0
#     node = node.parent
#     level = 0
#     while node:
#         level += 1
#         node = node.parent
#     return level
#
#
# def get_lca(node1, node2):
#     if not node1 or not node2:
#         return None
#     level1 = get_height(node1)
#     level2 = get_height(node2)
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
# def get_path(node1, node2):
#     if not node1 or not node2:
#         return []
#     lca = get_lca(node1, node2)
#     if not lca:
#         return None
#     path1 = []
#     node1 = node1.parent
#     while node1 and node1 != lca:
#         path1.append(node1)
#         node1 = node1.parent
#     path2 = []
#     node2 = node2.parent
#     while node2 and node2 != lca:
#         path2.append(node2)
#         node2 = node2.parent
#     path1.append(lca)
#     path2.reverse()
#     return path1 + path2
#
#
# def dfs_inorder(node):
#     if not node:
#         return None
#     if node.left:
#         dfs_inorder(node.left)
#     print(node)
#     if node.right:
#         dfs_inorder(node.right)
#     return None
#
#
# def dfs_postorder(node):
#     if not node:
#         return None
#     if node.left:
#         dfs_postorder(node.left)
#     if node.right:
#         dfs_postorder(node.right)
#     print(node)
#     return None
#
#
# def dfs_preorder(node):
#     if not node:
#         return None
#     print(node.item)
#     if has_left(node):
#         dfs_preorder(node.left)
#     if has_right(node):
#         dfs_preorder(node.right)
#     return None
#
#
# def is_aligned(node):
#     if not node:
#         return False
#     return node.value == get_height(node)
#
#
# r"""
#
# Given a binary tree, we say a node is aligned if its value is the same as its depth.
# Return the length of the longest descendant chain of aligned nodes.
# The chain does not need to start at the root.
#
# Example:
#
# depth 0             A7
#                   /    \
# depth 1         B1      C3
#               /  \      /
# depth 2     D2    E8  F2
#            / \       /  \
# depth 3   G4  H3    I3  J3
#                 \       /
# depth 4         M4     K4
#                 /     /
# depth 5       N5     L5
#
# Output: 5. The longest chain of aligned nodes is 1 -> 2 -> 3 -> 4 -> 5 [B,D,H,M,N]
#
# """
#
#
# def get_max_aligned(root: Node) -> list:
#     if not root:
#         return []
#
#     def is_aligned(node: Node, level: int) -> bool:
#         if not node:
#             return False
#         return node.value == level
#
#     max_aligned = 0
#     path = []
#
#     def visit(node: Node, level: int) -> tuple[int, list[Node]]:
#         if not node:
#             return 0, []
#
#         left, left_path = visit(node.left, level + 1)
#         right, right_path = visit(node.right, level + 1)
#         (current_max, current_path) = (left, left_path) if left > right else (right, right_path)
#
#         if is_aligned(node, level):
#             current_max += 1
#             current_path.append(node)
#
#         nonlocal max_aligned
#         nonlocal path
#
#         if current_max > max_aligned:
#             max_aligned = current_max
#             path = current_path
#         return current_max, current_path
#
#     return visit(root, 0)
#
#
#
#
# a = Node("A", 7)
# b = Node("B", 1)
# c = Node("C", 3)
# d = Node("D", 2)
# e = Node("E", 8)
# f = Node("F", 2)
# g = Node("G", 4)
# h = Node("H", 3)
# i = Node("I", 3)
# j = Node("J", 3)
# k = Node("K", 4)
# l = Node("L", 5)
# m = Node("M", 4)
# n = Node("N", 5)
#
# a.set_left(b)
# a.set_right(c)
# b.set_left(d)
# b.set_right(e)
# c.set_left(f)
# d.set_left(g)
# d.set_right(h)
# f.set_left(i)
# f.set_right(j)
# j.set_left(k)
# k.set_left(l)
# h.set_right(m)
# m.set_right(n)
#
# print(get_tree_level(a))
# print(get_height(g))
# print(get_ancestors(g))
# print(get_grand_children(d))
# print(get_grand_children(a))
# print(get_lca(g, e))  # to continue with lowest common ancestor
# print(get_path(h, j))
#
# print("dfs using preorder traversal:")
# dfs_preorder(a)
# print("dfs using inorder traversal:")
# dfs_inorder(a)
# print("using postorder traversal:")
# dfs_postorder(a)
#
# print(get_max_aligned(a))
