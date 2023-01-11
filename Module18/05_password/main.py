while True:
    password = input("Придумайте пароль: ")
    numbers = [str(x) for x in range(1, 11)]
    count = 0
    if not password.islower() and len(password) >= 8:
        for symbols in password:
            if symbols in numbers:
                count += 1
    if count >= 3:
        print("Это надёжный пароль!")
        break
    print("Пароль ненадёжный. Попробуйте ещё раз.")