list_len = int(input("Введите длину списка: "))
num_list = [1 if x % 2 == 0 else x % 5 for x in range(1, list_len + 1)]
print("Результат:", num_list)