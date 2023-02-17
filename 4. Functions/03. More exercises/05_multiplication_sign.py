#Try to do this WITHOUT multiplying the 3 numbers.
def multiplication_sign(my_list):
    count_negative = 0
    for num in my_list:
        if num < 0:
            count_negative += 1
        elif num == 0:
            return "zero"
        else:
            pass
    if count_negative % 2 == 0:
        return "positive"
    else:
        return "negative"


list_numbers = []
for _ in range(3):
    current_input = int(input())
    list_numbers.append(current_input)
print(multiplication_sign(list_numbers))
