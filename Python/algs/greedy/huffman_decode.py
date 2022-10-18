import re
import sys
import os

sys.path.append(os.path.abspath('../../'))
from dstructs.node import Node

def add_node(parent: Node, child: Node, to_left: bool):
    if to_left:
        parent.left = child
    else:
        parent.right = child

def build_tree(chars_codes: dict):
    curr_node = root = Node()
    for char, code in chars_codes.items():
        last_idx = len(code) - 1
        for idx, c in enumerate(code):
            to_left = c == '0'
            if idx == last_idx:
                leaf = Node(char)
                add_node(curr_node, leaf, to_left)

            elif to_left:
                if curr_node.left is None:
                    add_node(curr_node, Node(), to_left)
                curr_node = curr_node.left

            else:
                if curr_node.right is None:
                    add_node(curr_node, Node(), to_left)
                curr_node = curr_node.right
            
        curr_node = root
    return root

def decode(s: str, root: Node):
    decoded_str = ""
    curr_node = root
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

        decoded_str += curr_node.val
        curr_node = root

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