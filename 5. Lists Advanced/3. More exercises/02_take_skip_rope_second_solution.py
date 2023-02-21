main_string = input()

numbers, letters, result = [], [], []
[numbers.append(int(x)) if x.isdigit() else letters.append(x) for x in main_string]
while numbers:
    take, skip = numbers.pop(0), numbers.pop(0)

    result += letters[:take]
    letters = letters[take + skip:]

print("".join(result))