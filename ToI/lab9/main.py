def get_mon_code(i):
    if i == 1: return "0"
    bin_full = bin(i)[2:]
    bin_prime = bin_full[1:]
    n = len(bin_full)
    unar = "1" * (n - 1) + "0"
    return unar + bin_prime

def solve_book_stack(text_str):
    try:
        data = text_str.encode('cp1251')
    except UnicodeEncodeError:
        print("Ошибка: В строке есть символы, не входящие в таблицу CP1251")
        return

    stack = list(range(256))
    
    encoded_bits = ""
    print(f"{'i':<3} | {'xi':<4} | {'ASCII':<5} | {'Интервал':<8} | {'Кодовое слово':<16} | {'li'}")
    print("-" * 65)
    
    for idx, byte_val in enumerate(data, 1):
        pos_in_stack = stack.index(byte_val)
        interval = pos_in_stack 
        
        code = get_mon_code(interval)
        li = len(code)
        encoded_bits += code
        
        char_display = bytes([byte_val]).decode('cp1251', errors='replace')
        if byte_val == 32: char_display = '_' 
        
        print(f"{idx:<3} | {char_display:<4} | {byte_val:<5} | {interval:<8} | {code:<16} | {li}")
    
        stack.pop(pos_in_stack)
        stack.insert(0, byte_val)

    print("-" * 65)
    print(f"\nЗакодированное сообщение c(x):\n{encoded_bits}")
    print(f"\nИтоговые затраты L(x) = {len(encoded_bits)} бит.")

with open("../inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()

solve_book_stack(inpStr)