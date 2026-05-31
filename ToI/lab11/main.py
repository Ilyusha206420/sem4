import math


def lab_lz78_exact(text, char_bits=8):
    # Шаг 0: в словаре изначально только '#'
    dictionary = ["#"]

    steps_data = []
    steps_data.append(
        {
            "step": 0,
            "phrase": "#",
            "j": "-",
            "code_symbols": "-",
            "bits": "-",
        }
    )

    i = 0
    step_counter = 1

    while i < len(text):
        longest_match = ""
        match_index = 0

        # 1. Ищем самое длинное совпадение в текущем словаре (начиная с индекса 1)
        for idx in range(1, len(dictionary)):
            phrase = dictionary[idx]
            if text[i:].startswith(phrase):
                if len(phrase) > len(longest_match):
                    longest_match = phrase
                    match_index = idx

        # Текущий размер словаря ДО внесения изменений на этом шаге
        k = len(dictionary)

        # Вычисляем разрядность j_bits по формуле ⌈log2(k-1)⌉
        # Для k=1 (только '#') и k=2 (один символ) битность равна 0
        if k > 2:
            j_bits = math.ceil(math.log2(k - 1))
        else:
            j_bits = 0

        if match_index == 0:
            # СЛУЧАЙ 1: Совпадений не найдено (новый символ)
            current_char = text[i]
            new_phrase = current_char

            # Префикс из нулей длины j_bits
            prefix = "0" * j_bits if j_bits > 0 else ""
            # Если символ — пробел, выводим визуально понятное ' ', как в вашей таблице
            char_disp = (
                " " if current_char == " " else current_char
            )  # можно заменить на '_' если нужно

            code_str = f"{prefix}bin({char_disp})"
            bit_cost = j_bits + char_bits

            # Добавляем в словарь и сдвигаем указатель строго на 1 символ
            dictionary.append(new_phrase)
            i += 1
        else:
            # СЛУЧАЙ 2: Совпадение найдено
            # Берём следующий за совпадением символ для словаря
            next_char_idx = i + len(longest_match)
            if next_char_idx < len(text):
                next_char = text[next_char_idx]
                new_phrase = longest_match + next_char
            else:
                new_phrase = longest_match

            # Кодируем только индекс j в двоичном виде с разрядностью j_bits
            code_str = format(match_index, f"0{j_bits}b")
            bit_cost = j_bits

            # Добавляем новую фразу в словарь (если её там ещё нет)
            if new_phrase not in dictionary:
                dictionary.append(new_phrase)

            # ВАЖНО: Сдвиг по тексту только на длину совпадения (longest_match)
            i += len(longest_match)

        steps_data.append(
            {
                "step": step_counter,
                "phrase": new_phrase,
                "j": match_index,
                "code_symbols": code_str,
                "bits": bit_cost,
            }
        )
        step_counter += 1

    return steps_data

with open("../inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()
results = lab_lz78_exact(inpStr)

# Печать красивой таблицы
print(
    f"{'Шаг':<5} | {'Словарь':<10} | {'Номер слова (j)':<16} | {'Кодовые символы':<18} | {'Затраты в битах':<15}"
)
print("-" * 75)

total_bits = 0
for row in results:
    # Заменяем пробелы в визуализации словаря на видимый пробел для удобства проверки
    phrase_disp = row["phrase"].replace(" ", " ")
    print(
        f"{row['step']:<5} | {phrase_disp:<10} | {row['j']:<16} | {row['code_symbols']:<18} | {row['bits']:<15}"
    )
    if row["bits"] != "-":
        total_bits += row["bits"]

print("-" * 75)
print(f"Итоговые затраты: I(x) = {total_bits} бит.")
