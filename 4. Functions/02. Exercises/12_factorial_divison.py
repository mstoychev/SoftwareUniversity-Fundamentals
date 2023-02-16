def factorial(num):
    for i in range(num - 1, 0, -1):
        num *= i
    return num


first_num = int(input())
second_num = int(input())
result = (factorial(first_num) / factorial(second_num))
print(f"{result:.2f}")