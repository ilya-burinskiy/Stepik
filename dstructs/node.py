class Node:

    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val 
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)

class BinTreeNode(Node):

    def __init__(self, key, val=None, left=None, right=None):
        super().__init__(val, left, right)
        self.key = key