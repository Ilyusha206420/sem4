import math

def elias_gamma_mon(l):
    if l == 1:
        return "0"
    k = int(math.log2(l))
    prefix = "1" * k + "0"
    binary_l = bin(l)[2:]
    suffix = binary_l[1:] 
    return prefix + suffix

def lz77_encode(text):
    history = ""
    i = 1
    total_bits = 0

    print(f"{'i':^4} | {'Флаг':^4} | {'Словарь':^12} | {'d':^9} | {'l':^3} | {'Кодовая последовательность':^27} | {'Затраты':^7} |")
    print("-" * 86)
    
    idx = 0
    while idx < len(text):
        match_dist = 0
        match_len = 0

        for length in range(1, len(text) - idx + 1):
            substring = text[idx:idx+length]
            pos = history.rfind(substring)
            if pos != -1:
                match_dist = len(history) - pos
                match_len = length
            else:
                break
                
        if match_len > 0:
            flag = 1
            dict_val = text[idx:idx+match_len]
            history_size = len(history)
            
            d_bits_count = math.ceil(math.log2(history_size))
            d_bin = bin(match_dist)[2:].zfill(d_bits_count)
            
            l_code = elias_gamma_mon(match_len)
            
            code_seq = f"1{d_bin}{l_code}"
            bits = len(code_seq)
            
            d_str = f"{match_dist}({history_size})"
            print(f"{i:^4} | {flag:^4} | {dict_val:^12} | {d_str:^9} | {match_len:^3} | {code_seq:^27} | {bits:^7} |")
            
            history += dict_val
            idx += match_len
        else:
            flag = 0
            char = text[idx]
            dict_val = char
            
            code_seq = f"0bin({char})"
            bits = 9  
            
            print(f"{i:^4} | {flag:^4} | {dict_val:^12} | {'-':^9} | {0:^3} | {code_seq:^27} | {bits:^7} |")
            
            history += char
            idx += 1
            
        total_bits += bits
        i += 1
        
    print("-" * 86)
    print(f"Итоговые затраты в битах: l(x) = {total_bits} бит.")

with open("../inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()
lz77_encode(inpStr)