def calculation(num1, num2, operation):
    if operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 // num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


operation = input()
num1 = int(input())
num2 = int(input())
print(calculation(num1, num2, operation))