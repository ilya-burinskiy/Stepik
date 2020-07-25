class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self):
        return repr(self.val)

class BinTreeNode(Node):

    def __init__(self, key, val=None, left=None, right=None):
        super().__init__(val, left, right)
        self.key = key