def sum_numbers(fist, second):
    return fist + second

def subtract(sum, third):
    return sum - third


def add_and_subtract(n1, n2, n3):
    result_of_sum = sum_numbers(n1, n2)
    result = subtract(result_of_sum, n3)
    return result


n1 = int(input())
n2 = int(input())
n3 = int(input())
print(add_and_subtract(n1, n2, n3))






