# binary trees and bsts

(book p 429)

trees are everywhere in computer science :

- like SQL databases (which use B-trees)
- git version control system
- Their unique properties (see the big O analysis) make them the ideal backbone of other data structures like heaps,
  union-find, an tries

## terminology

- root A (only node without a parent)
- leaves (nodes without children) : e.g. C, U, W, X
- ancestors of V (B,A)
- parent of V is B
- branching factor of V : 2 (B have 2 children W and X)
- children of V : W and X
- the depth, height or level of a node is the number of ancestors of that node
- the root is height, level, depth zero, its children are depth/height/level 1 and so on
- the depth of the entire tree is the maximum depth among all nodes plus one, or 0 (zero) if there are no nodes
- with our example, the deepest leaves are at depth 4, so the tree's depth is 5

```
             A
            / \
           B   C
          /  \     
         V    U  
        /  \
       W    X
```

## implementation

```python

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left 
    self.right = right
```

using the same image as example we have this instructions
root.left <=> B
root.right <=> C
V <=> B.left <=> root.left.left
and so on

we can warm up with :

- has_left
- has_right
- has_children
- has_grand_children
- get_children
- get_grand_children

## warm up 2

- considering that we are asked to give the node's parent, now we are stuck since there is no information about that
- this leads us to rewrite our definition of the Node as follow :

```python

class Node:
  def __init__(self, val, parent= None, left=None, right=None):
    self.val = val
    self.left = left 
    self.right = right
    self.parent = parent
```

then we can warm up with :

- get_ancestors
- get_level
- get_lca (lowest common ancestor)
- is_root (since the root is the only node without a parent)
- get_distance (between 2 nodes) ...

## DEPTH-FIRST-SEARCH

PREORDER, INORDER, AND POSTORDER TRAVERSALS

