def lowest_divisor(number):
    divisor = 2
    while number % divisor:
        divisor += 1
    print("The smallest divisor other than 1:", divisor)


lowest_divisor(int(input("Enter the number: ")))
