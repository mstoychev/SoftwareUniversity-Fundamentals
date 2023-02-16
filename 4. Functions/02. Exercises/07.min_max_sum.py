def min_number_in_list(number):
    return min(number)


def max_number_in_list(number):
    return max(number)


def sum_number_in_list(number):
    return sum(number)


numbers_input = [int(j) for j in input().split()]

minimum_number = min_number_in_list(numbers_input)
maximum_number = max_number_in_list(numbers_input)
sum_of_all_numbers = sum_number_in_list(numbers_input)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
