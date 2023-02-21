string = input()
result = []
number_lst = [int(num) for num in string if num.isdigit()]
letter_lst = [char for char in string if not char.isdigit()]

take_lst = [number_lst[i] for i in range(len(number_lst)) if i % 2 == 0]
skip_lst = [number_lst[i] for i in range(len(number_lst)) if not i % 2 == 0]

for i in range(len(take_lst)):
    take_num = take_lst[i]
    skip_num = skip_lst[i]

    result += letter_lst[0:take_num]
    if len(letter_lst) > 0:
        for _ in range(take_num):
            letter_lst.pop(0)
            if len(letter_lst) == 0:
                print("".join(result))
                exit()

    if len(letter_lst) > 0:
        for _ in range(skip_num):
            letter_lst.pop(0)

print(*result, sep="")


