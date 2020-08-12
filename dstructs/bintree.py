from dstructs.node import BinTreeNode

class BinTree:

    def __init__(self):
        self.root = None

    @staticmethod
    def read_bintree():
        n = int(input())
        nodes = [None for _ in range(n)]
        for i in range(n):
            nodes[i] = tuple(map(int, input().split()))

        return nodes

    def build_right_subtree(self, root, node_idx, nodes):
        if node_idx != -1:
            key = nodes[node_idx][0]
            node = BinTreeNode(key)
            root.right = node
            node.parent = root

            left_subtree_root_idx = nodes[node_idx][1]
            right_subtree_root_idx = nodes[node_idx][2]

            self.build_left_subtree(node, left_subtree_root_idx, nodes)
            self.build_right_subtree(node, right_subtree_root_idx, nodes)

    def build_left_subtree(self, root, node_idx, nodes):
        if node_idx != -1:
            key = nodes[node_idx][0]
            node = BinTreeNode(key)
            root.left = node
            node.parent = root

            left_subtree_root_idx = nodes[node_idx][1]
            right_subtree_root_idx = nodes[node_idx][2]

            self.build_left_subtree(node, left_subtree_root_idx, nodes)
            self.build_right_subtree(node, right_subtree_root_idx, nodes)

    def build_bintree(self, nodes):
        self.root = BinTreeNode(nodes[0][0])
        left_subtree_root_idx = nodes[0][1]
        right_subtree_root_idx = nodes[0][2]
        self.build_left_subtree(self.root, left_subtree_root_idx, nodes)
        self.build_right_subtree(self.root, right_subtree_root_idx, nodes)


    def isbts(self):
        def check(node, min_, max_):
            if node is None:
                return True
            if node.key <= min_ or max_ <= node.key:
                return False
            return check(node.left, min_, node.key) and \
                check(node.right, node.key, max_)

        return check(self.root, -float('inf'), float('inf'))

    def subtree_max(self, node):
        while node.right != None:
            node = node.right
        return node
    
    def subtree_min(self, node):
        while node.left != None:
            node = node.left
        return node

    def node_predecessor(self, node):
        if node.left != None:
            return self.subtree_max(node.left)

        parent = node.parent
        while parent != None and node == parent.left:
            node = parent
            parent = node.parent
        return parent

    def node_successor(self, node):
        if node.right != None:
            return self.subtree_min(node.right)

        parent = node.parent
        while parent != None and node == parent.right:
            node = parent
            parent = node.parent
        
        return parent