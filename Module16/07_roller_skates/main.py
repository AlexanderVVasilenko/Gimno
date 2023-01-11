skates_list = []
leg_list = []
result = 0

skates = int(input("Введите кол-во конльков: "))
for _ in range(skates):
    print("Размер", _ + 1, "пары:", end=" ")
    skate = int(input())
    skates_list.append(skate)

legs = int(input("Введите кол-во людей: "))
for _ in range(legs):
    print("Размер ноги", _ + 1, "человека:", end=" ")
    leg = int(input())
    leg_list.append(leg)

for skate in skates_list:
    for leg in leg_list:
        if skate == leg:
            result += 1
            leg_list.remove(leg)
        elif skate > leg:
            leg_list.remove(leg)
            result += 1

print("Наибольшее кол-во людей, которые могут взять ролики:", result)