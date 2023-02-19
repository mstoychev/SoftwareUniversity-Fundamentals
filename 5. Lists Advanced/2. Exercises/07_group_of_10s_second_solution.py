input_int = list(map(int, input().split(', ')))

for group in range(1, 11):
    if len(input_int) == 0:
        break
    group_list = [num for num in input_int if num <= (group * 10)]
    input_int = [num for num in input_int if num not in group_list]
    print(f"Group of {group}0's: {group_list}")