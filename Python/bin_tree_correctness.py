class Node:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.key)


def read_bintree():
    n = int(input())
    nodes = [None for _ in range(n)]
    for i in range(n):
        nodes[i] = tuple(map(int, input().split()))

    return nodes

def build_left_subtree(root, node_idx, nodes):
    if node_idx != -1:
        key = nodes[node_idx][0]
        node = Node(key)
        root.left = node

        left_subtree_root_idx = nodes[node_idx][1]
        right_subtree_root_idx = nodes[node_idx][2]

        build_left_subtree(node, left_subtree_root_idx, nodes)
        build_right_subtree(node, right_subtree_root_idx, nodes)

def build_right_subtree(root, node_idx, nodes):
    if node_idx != -1:
        key = nodes[node_idx][0]
        node = Node(key)
        root.right = node

        left_subtree_root_idx = nodes[node_idx][1]
        right_subtree_root_idx = nodes[node_idx][2]

        build_left_subtree(node, left_subtree_root_idx, nodes)
        build_right_subtree(node, right_subtree_root_idx, nodes)




def build_bintree(nodes):
    root = Node(nodes[0][0])
    left_subtree_root_idx = nodes[0][1]
    right_subtree_root_idx = nodes[0][2]
    build_left_subtree(root, left_subtree_root_idx, nodes)
    build_right_subtree(root, right_subtree_root_idx, nodes)

    return root


def is_leaf(node):
    return node.left is None and node.right is None


def is_bst(root):

    def check(node, min_, max_):
        if node is None:
            return True
        if node.key <= min_ or max_ <= node.key:
            return False
        return check(node.left, min_, node.key) and \
               check(node.right, node.key, max_)
    
    return check(root, -float('inf'), float('inf'))


if __name__ == "__main__":
    nodes = read_bintree()
    root = build_bintree(nodes)
    isbst = is_bst(root)

    if isbst:
        print("CORRECT")
    else:
        print("INCORRECT")