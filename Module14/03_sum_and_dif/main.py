def digits_amount(num):
    counter = 0
    while num:
        num //= 10
        counter += 1
    return counter


def digits_sum(num):
    sum_ = 0
    while num:
        sum_ += num % 10
        num //= 10
    return sum_


number = int(input("Enter the number: "))
if number < 0:
    print("Error!")
else:
    digits_sum = digits_sum(number)
    digits_amount = digits_amount(number)
    print("Amount of digits in number:", digits_amount)
    print("Sum of digits in number:", digits_sum)
    print("Difference of sum and amount of digits", digits_sum -
          digits_amount)
