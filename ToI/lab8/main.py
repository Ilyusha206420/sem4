import math
from collections import deque

def nCr_bits(n, r):
    if r <= 0 or r > n: return 0
    return math.ceil(math.log2(math.comb(n, r)))

def run_huffman_lab_8(inpStr):
    d = {}
    for char in inpStr:
        d[char] = d.get(char, 0) + 1

    nodes = [[count, char, None, None] for char, count in d.items()]
    
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])
        left = nodes.pop(0)
        right = nodes.pop(0)
        nodes.append([left[0] + right[0], None, left, right])
    
    root = nodes[0]
    lengths = {}
    
    def get_lengths(node, current_l=0):
        if node[1] is not None:
            lengths[node[1]] = current_l
            return
        if node[2]: get_lengths(node[2], current_l + 1)
        if node[3]: get_lengths(node[3], current_l + 1)
    
    get_lengths(root)

    tiers = {}
    for char, l in lengths.items():
        if l not in tiers: tiers[l] = []
        tiers[l].append(char)
    
    max_l = max(tiers.keys())
    regular_codes = {}
    current_code_val = 0
    prev_l = 0
    
    sorted_tiers = sorted(tiers.keys())
    for l in sorted_tiers:
        current_code_val <<= (l - prev_l)
        for char in sorted(tiers[l]): 
            regular_codes[char] = bin(current_code_val)[2:].zfill(l)
            current_code_val += 1
        prev_l = l

    print(f"|{'Символ':^8}|{'Ярус':^6}|{'Регулярный код':^18}|")
    print("-" * 36)
    for char in sorted(regular_codes.keys(), key=lambda x: (lengths[x], x)):
        print(f"|{char:^8}|{lengths[char]:^6}|{regular_codes[char]:^18}|")

    c1_x = ""
    c2_x = "".join([regular_codes[char] for char in inpStr])
    
    rem_chars = 256 
    nodes_on_tier = 1
    
    print(f"\n|{'Ярус':^6}|{'Всего':^8}|{'Концевых':^10}|{'bits nj':^10}|{'bits comb':^10}|")
    print("-" * 50)

    for j in range(max_l + 1):
        nj = len(tiers.get(j, []))
        nj_bits_len = math.ceil(math.log2(nodes_on_tier + 1))
        comb_bits_len = nCr_bits(rem_chars, nj)
        
        if nj_bits_len > 0:
            c1_x += bin(nj)[2:].zfill(nj_bits_len)
        if nj > 0:
            c1_x += "0" * comb_bits_len 

        print(f"|{j:^6}|{nodes_on_tier:^8}|{nj:^10}|{nj_bits_len:^10}|{comb_bits_len:^10}|")
        
        rem_chars -= nj
        nodes_on_tier = (nodes_on_tier - nj) * 2

    print(f"\nc1(x) [длина {len(c1_x)}]: {c1_x}")
    print(f"c2(x) [длина {len(c2_x)}]: {c2_x}")
    
    l1, l2 = len(c1_x), len(c2_x)
    N = len(inpStr)
    H = sum([-(c/N)*math.log2(c/N) for c in d.values()])
    R = l2 / N

    print(f"\nПараметры:")
    print(f"l1 = {l1}, l2 = {l2}, l = {l1 + l2}")
    print(f"H = {H:.5f}, R = {R:.5f}, R-H = {R-H:.5f}")

try:
    with open("../inputText", "r", encoding="utf-8") as f:
        inpStr = f.readline().strip()
    run_huffman_lab_8(inpStr)
except FileNotFoundError:
    print("Файл не найден. Проверь путь.")