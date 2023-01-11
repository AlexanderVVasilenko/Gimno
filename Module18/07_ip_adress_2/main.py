ip_ardess = input("Введите IP: ").split(".")
ip_correct = True

if len(ip_ardess) == 4:
    for number in ip_ardess:
        if number.isdigit():
            if int(number) > 255:
                print(f"{number} перевышает 255")
                ip_correct = False
            elif int(number) < 0:
                print(f"{number} меньше чем 0")
                ip_correct = False
        else:
            print(f"{number} - это не целое число.")
else:
    print("Адрес — это четыре числа, разделённые точками.")

if ip_correct:
    print("IP-адрес корректен.")
