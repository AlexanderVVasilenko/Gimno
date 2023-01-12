def int_reverse(number):
    number = int(number)
    rev_number = 0
    while number:
        rev_number *= 10
        rev_number += number % 10
        number //= 10
    return rev_number


def full_reverse(number):
    int_part = int_reverse(number)
    dig_after_point = 0
    while number - int(number):
        number *= 10
        dig_after_point += 1
    float_part = number % (10 ** dig_after_point)
    float_part = int_reverse(float_part)
    while float_part > 1:
        float_part /= 10
    return int_part + float_part


a = float(input("Enter the first number: "))
a = full_reverse(a)
b = float(input("Enter the second number: "))
b = full_reverse(b)
print("\nThe reversed first number:", a)
print("The reversed second number:", b)
print("Sum:", a + b)
