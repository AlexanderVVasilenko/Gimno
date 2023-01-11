def test(text1, text2):
    step = 1
    test = False
    while step <= len(text2):
        result = text1[-step:] + text1[:-step]
        if result == text2:
            test = True
            break
        step += 1
    return f"Первая строка получается из второй со сдвигом {step}." \
        if test else "Первую строку нельзя получить из второй с помощью циклического сдвига."


word1 = input("Введите первую строку: ")
word2 = input("Введите вторую строку: ")
print(test(word1, word2))