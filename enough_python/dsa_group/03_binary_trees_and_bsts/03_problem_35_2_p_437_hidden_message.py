r"""
The self-proclaimend cryptograpthy expert in your friend group has devised their own schema to hide messages in binary
trees. Each node has a text filed with exactly two characters. The first character is either 'b', 'i', or 'a'. The second
character is part of the hidden message. To decode the message, you have to read the hidden-message characters in the
following order:
- If the first character in node is 'b', the node goes before its left subtree, and the left subtree goes before the
    right subtree.
- If it is 'a', the node goes after its right subtree, and the right subtree goes before after the left subtree.
- If it is 'i', the node goes after its left subtree and before its right subtree.

Given the root of a binary tree, return the hidden message.

 b -> preorder traversal
 a -> postorder traversal
 i -> inorder traversal

Example :

            bn
          /   \
        i_     a!
      /   \    /
    ae    it  br
   /  \        \
  bi  bc       ay

Output: nice_try!

"""


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left
        self.left.parent = self

    def set_right(self, right):
        self.right = right
        self.right.parent = self


def get_hidden_message(root):
    if not root:
        return []

    def visit(node):
        if not node:
            return []

        current_message = []
        if node.value[0] == 'b':
            current_message.append(node.value[1])
            current_message.extend(visit(node.left))
            current_message.extend(visit(node.right))
        elif node.value[0] == 'a':
            current_message.extend(visit(node.left))
            current_message.extend(visit(node.right))
            current_message.append(node.value[1])
        else:
            current_message.extend(visit(node.left))
            current_message.append(node.value[1])
            current_message.extend(visit(node.right))
        return current_message

    return visit(root)


bn = Node('bn')
i_ = Node('i_')
a_ = Node("a!")
ae = Node("ae")
it = Node("it")
bi = Node("bi")
bc = Node("bc")
ay = Node("ay")
br = Node("br")

bn.set_left(i_)
bn.set_right(a_)
i_.set_left(ae)
i_.set_right(it)
ae.set_left(bi)
ae.set_right(bc)
a_.set_left(br)
br.set_right(ay)

print(get_hidden_message(bn))
