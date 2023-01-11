text = input("Введите текст: ")
vowels = 'ауоыиэяюёе'
vowels_list_in_text = [x for x in text if x in vowels]
print(f"Список гласных букв: {vowels_list_in_text}")
print(f"Длинна списка: {len(vowels_list_in_text)}")