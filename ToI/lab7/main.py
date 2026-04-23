import math
from collections import deque

def run_huffman_lab_7(inpStr):
    # Статистика
    d = {}
    for char in inpStr:
        d[char] = d.get(char, 0) + 1

    nodes = [[count, char, None, None] for char, count in d.items()]
    
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])  #
        left = nodes.pop(0)
        right = nodes.pop(0)
        nodes.append([left[0] + right[0], None, left, right])
    
    root = nodes[0]
    codes = {}
    
    def build_codes(node, current_code=""):
        if node[1] is not None:
            codes[node[1]] = current_code
            return
        if node[2]: build_codes(node[2], current_code + "0")
        if node[3]: build_codes(node[3], current_code + "1")
    
    build_codes(root)

    tree_bits = ""
    leaves_symbols = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr[1] is None:
            tree_bits += "0"
            if curr[2]: queue.append(curr[2])
            if curr[3]: queue.append(curr[3])
        else:
            tree_bits += "1"
            leaves_symbols.append(curr[1])
    
    c1_x = tree_bits
    for char in leaves_symbols:

        c1_x += bin(ord(char.encode('cp1251')))[2:].zfill(8)

    c2_x = "".join([codes[char] for char in inpStr])

    print(f"|{'Символ':^8}|{'ASCII':^8}|{'Частота':^8}|{'Длина':^6}|{'Код':^12}|")
    print("-" * 50)
    for char in sorted(d.keys()):
        ascii_val = ord(char.encode('cp1251'))
        print(f"|{char:^8}|{bin(ascii_val):^8}|{d[char]:^8}|{len(codes[char]):^6}|{codes[char]:^12}|")

    print(f"\nc1(x) [служебная]: {c1_x}")
    print(f"\nc2(x) [сообщение]: {c2_x}")

    l1, l2 = len(c1_x), len(c2_x)
    N = len(inpStr)
    H = sum([-(c/N)*math.log2(c/N) for c in d.values()])
    
    print(f"\nПараметры:")
    print(f"l1 = {l1} бит, l2 = {l2} бит, l = {l1+l2} бит")

with open("../inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()

run_huffman_lab_7(inpStr)