import random
num_amount = int(input("Введите кол-во чесел в списке: "))


num_list = [random.randint(0, 2) for _ in range(num_amount)]
result = [x for x in num_list if x != 0]
count_zero = len(num_list) - len(result)
result += [0 for _ in range(count_zero)]
for _ in range(count_zero):
    result.pop()

print("Список до сжатия:", num_list)
print("Список после сжатия:", result)