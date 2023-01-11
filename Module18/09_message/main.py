def reverse_line(line):
    rev_word = ""
    new_line = ""
    for letter in line:
        if letter.isalpha():
            rev_word += letter
        else:
            rev_word = rev_word[::-1]
            new_line += rev_word
            new_line += letter
            rev_word = ""
    return new_line


line = input("Введите сообщение: ")
print(f"Новое сообщение: {reverse_line(line)}")
