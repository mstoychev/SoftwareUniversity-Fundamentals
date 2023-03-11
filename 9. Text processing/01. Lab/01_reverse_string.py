def reverse_str(string):
    reverse_string = string[::-1]
    print(f"{string} = {reverse_string}")


while True:
    string = input()
    if string == "end":
        break
    reverse_str(string)
