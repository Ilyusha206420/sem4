import math

with open("../inputText", "r", encoding="utf-8") as f:
    inpStr = f.read().strip()

char_counts = {}
for char in inpStr:
    char_counts[char] = char_counts.get(char, 0) + 1

total_chars = len(inpStr)
alphabet = sorted(char_counts.keys())

probs = {}
cum_probs = {}
entropy = 0
current_cum = 0

for char in alphabet:
    p = char_counts[char] / total_chars
    probs[char] = p
    cum_probs[char] = current_cum
    entropy += p * -math.log2(p) 
    current_cum += p

def arithmetic_encode_block(block):
    F = 0.0
    G = 1.0
    
    for char in block:
        q_i = cum_probs[char]
        p_i = probs[char]
        
        F = F + q_i * G
        G = G * p_i
        
    l_size = math.ceil(-math.log2(G)) + 1
    
    value = F + G / 2
    code = ""
    temp_v = value
    for _ in range(l_size):
        temp_v *= 2
        if temp_v >= 1:
            code += "1"
            temp_v -= 1
        else:
            code += "0"
    return code, l_size

block_size = 6
print(f"{'Блок':^10} | {'Длина кода':^10} | {'Кодовое слово'}")
print("-" * 50)

total_bits = 0
num_blocks = 0

for i in range(0, len(inpStr), block_size):
    block = inpStr[i:i+block_size] 
    res_code, res_len = arithmetic_encode_block(block)
    total_bits += res_len
    num_blocks += 1
    print(f"{block:^10} | {res_len:^10} | {res_code}")
    if len(block) < block_size: break

if num_blocks > 0:
    avg_R = (total_bits / (num_blocks * block_size))
    print(f"\nСредняя скорость кодирования R_ap = {avg_R:.4f} бит/символ\nЭнотропия: {entropy}\nИзбыточность: {}")
