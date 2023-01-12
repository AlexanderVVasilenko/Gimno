def print_years_with_3_same_digits(low_year, up_year):
    for year in range(low_year, up_year + 1):
        counter_1 = 1
        counter_2 = 1
        first_number = year % 10
        second_number = (year // 10) % 10
        if first_number == second_number:
            counter_1 += 1
        year_ = year // 100
        for _ in range(2):
            if year_ % 10 == first_number:
                counter_1 += 1
            elif year_ % 10 == second_number:
                counter_2 += 1
            year_ //= 10
        if counter_1 >= 3 or counter_2 >= 3:
            print(year)


first_year = int(input("Enter the first year: "))
second_year = int(input("Enter the second year: "))

print(f"\nYears with 3 same digits from {first_year} to {second_year}:")
print_years_with_3_same_digits(first_year, second_year)
