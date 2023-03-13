first_string, second_string = input().split()
sum = 0
if len(first_string) > len(second_string):
    for i in range(len(second_string)):
        sum += ord(second_string[i]) * ord(first_string[i])

    for i in range(len(second_string), len(first_string)):
        sum += ord(first_string[i])

elif len(first_string) < len(second_string):
    for i in range(len(first_string)):
        sum += ord(second_string[i]) * ord(first_string[i])

    for i in range(len(first_string), len(second_string)):
        sum += ord(second_string[i])
else:
    for i in range(len(first_string)):
        sum += ord(second_string[i]) * ord(first_string[i])

print(sum)
