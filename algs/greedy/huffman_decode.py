import re

class Node:
    
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.head = Node()

    def add_node(self, parent: Node, child: Node, to_left: bool):
        if to_left:
            parent.left = child
        else:
            parent.right = child

def build_tree(chars_codes: dict):
    t = Tree()
    curr_node = t.head
    for char, code in chars_codes.items():
        last_idx = len(code) - 1
        for idx, c in enumerate(code):
            to_left = c == '0'
            if idx == last_idx:
                leaf = Node(char)
                t.add_node(curr_node, leaf, to_left)

            elif to_left:
                if curr_node.left is None:
                    t.add_node(curr_node, Node(), to_left)
                curr_node = curr_node.left

            else:
                if curr_node.right is None:
                    t.add_node(curr_node, Node(), to_left)
                curr_node = curr_node.right
            
        curr_node = t.head
    return t

def decode(s: str, t: Tree):
    decoded_str = ""
    curr_node = t.head
    n = len(s)
    i = 0
    to_left = s[i] == '0'

    while i < n:
        while curr_node.left is not None or curr_node.right is not None:
            if to_left:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            i += 1
            to_left = s[i] == '0' if i < n else None

        decoded_str += curr_node.char
        curr_node = t.head

    return decoded_str

def main():
    chars_num, str_len = input().split()
    chars_num, str_len = int(chars_num), int(str_len)

    d = dict()
    pattern = re.compile("([a-z]): (\d+)")
    for _ in range(chars_num):
        s = input()
        match = pattern.match(s)
        char, code = match.group(1), match.group(2)
        d[char] = code

    encoded_str = input()
    t = build_tree(d)
    decoded_str = decode(encoded_str, t) 
    print(decoded_str)

if __name__ == "__main__":
    main()