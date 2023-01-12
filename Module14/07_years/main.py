def print_years_with_3_same_digits(low_year: int, up_year: int):
    for year in range(low_year, up_year + 1):
        if is_year_have_3_same_digits(year):
            print(year)


def is_year_have_3_same_digits(year: int):
    last_digit_counter = 1
    prelast_digit_counter = 1
    first_digit = year % 10
    second_digit = (year // 10) % 10
    if first_digit == second_digit:
        last_digit_counter += 1
    year_ = year // 100
    for _ in range(2):
        if year_ % 10 == first_digit:
            last_digit_counter += 1
        elif year_ % 10 == second_digit:
            prelast_digit_counter += 1
        year_ //= 10
    if last_digit_counter >= 3 or prelast_digit_counter >= 3:
        return True


first_year = int(input("Enter the first year: "))
second_year = int(input("Enter the second year: "))

if first_year < 1000 or second_year < 1000 or first_year > 9999 or \
        second_year > 9999:
    print("Error!")
else:
    print(f"\nYears with 3 same digits from {first_year} to {second_year}:")
    print_years_with_3_same_digits(first_year, second_year)
