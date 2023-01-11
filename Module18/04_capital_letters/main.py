text = input("Введите строку: ").split()
new_text = [x.capitalize() for x in text]
print(" ".join(new_text))