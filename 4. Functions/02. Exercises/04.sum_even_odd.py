def sum_digits(number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for digit in number:
        digit_as_num = int(digit)
        if digit_as_num % 2 == 0:
            sum_of_even_digits += digit_as_num
        else:
            sum_of_odd_digits += digit_as_num
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


input_word = input()
print(sum_digits(input_word))
