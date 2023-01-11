text = input("Введите строку: ").split()
line_len = [len(word) for word in text]
print("Самое длинное слово:", text[line_len.index(max(line_len))])
print("Длина этого слова:", max(line_len))