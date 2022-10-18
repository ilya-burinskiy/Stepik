from collections import Counter
import sys
import os

sys.path.append(os.path.abspath('../../'))
from dstructs.node import Node
from dstructs.heap import MinHeap

class Leaf(Node):

    def __init__(self, char, freq):
        super().__init__(freq)
        self.c = char
        
def gen_codes(node: Node, curr_code: str, codes: dict):
    if isinstance(node, Leaf):
        if curr_code == "":
            curr_code = '0'
        codes[node.c] = curr_code
        return
    gen_codes(node.right, curr_code + '1', codes)
    gen_codes(node.left, curr_code + '0', codes)
    
def huffman_code(leafs: list):
    n = len(leafs)
    h = MinHeap()

    for i in range(n):
        h.insert(leafs[i])

    for i in range(n - 1):
        z = Node()
        z.left = x = h.extract_min()
        z.right = y = h.extract_min()
        z.val = x.val + y.val
        h.insert(z)
    res = h.extract_min()
    return res

def main():
    s = "abacabad"
    c = Counter()
    
    for char in s:
        c[char] += 1

    c = dict(c)
    chars = []
    for char, freq in c.items():
        chars.append(Leaf(char, freq))

    htree_root = huffman_code(chars)
    curr_code = ""
    codes = {}
    gen_codes(htree_root, curr_code, codes)

    was_printed = set()
    encoded_str = ""
    for c in s:
        if c not in was_printed:
            print(c + ': ' + codes[c])
            was_printed.add(c)
        encoded_str += codes[c]
    print(encoded_str)

    
if __name__ == "__main__":
    main()
