lst_input = input().split()
#change = lst_input.copy()
command = input()
while command != "3:1":
    lst_command = command.split()
    action = lst_command[0]
    index = int(lst_command[1])
    if action == "merge":
        final_idx = int(lst_command[2])
        result = "".join(map(lambda x: x, lst_input[index:final_idx]))
        lst_input[index:final_idx] = result
        print(lst_input)
        exit()

    command = input()