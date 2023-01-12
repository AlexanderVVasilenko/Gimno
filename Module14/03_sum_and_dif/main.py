def digits_amount(num):
    counter = 0
    while num:
        num //= 10
        counter += 1
    print("Amount of digits in number:", counter)
    return counter


def digits_sum(num):
    sum_ = 0
    while num:
        sum_ += num % 10
        num //= 10
    print("Sum of digits in number:", sum_)
    return sum_


number = int(input("Enter the number: "))
if number < 0:
    print("Error!")
else:
    print("Difference of sum and amount of digits", digits_sum(number) -
          digits_amount(number))
