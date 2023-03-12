input_string = input()
digits = []
letters = []
for char in input_string:
    if char.isdigit():
        digits.append(char)
        input_string = input_string.replace(char, "")
    elif char.isalpha():
        letters.append(char)
        input_string = input_string.replace(char, "")

print("".join(digits))
print("".join(letters))
print(input_string)
