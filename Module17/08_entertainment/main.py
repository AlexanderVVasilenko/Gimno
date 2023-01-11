sticks = list(range(1, int(input("Количество палок: ")) + 1))
throws = int(input("Количество бросков: "))
pitch = []
for i in range(throws):
    pitch += [_ for _ in (range(int(input(f"Бросок номер: {i + 1}. Сбиты палки с номера ")),
                                int(input(f"по номер ")) + 1))]
result = ["." if _ in pitch else "I" for _ in sticks]
print("Результат:", "".join(result))

# не получтлось сделть без обыного цикла