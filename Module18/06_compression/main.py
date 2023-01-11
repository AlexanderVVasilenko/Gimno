def compression(use_list):
    count = 1
    compressed = []

    for symbol in range(len(use_list)):
        if use_list[symbol] == use_list[symbol + 1: symbol + 2]:
            count += 1
            continue
        compressed.append(use_list[symbol] + str(count))
        count = 1
    return compressed


input_str = input("Введите строку: ")
print("Закодированная строка:", "".join(compression(input_str)))
