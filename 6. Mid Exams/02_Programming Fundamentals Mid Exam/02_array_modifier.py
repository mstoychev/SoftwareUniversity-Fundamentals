lst = [int(x) for x in input().split()]
command = input()
while command != "end":
    command = command.split()
    action = command[0]
    if action == "swap":
        idx_1 = int(command[1])
        idx_2 = int(command[2])
        lst[idx_1], lst[idx_2] = lst[idx_2], lst[idx_1]
    elif action == "multiply":
        idx_1 = int(command[1])
        idx_2 = int(command[2])
        lst[idx_1] *= lst[idx_2]
    elif action == "decrease":
        for i in range(len(lst)):
            lst[i] -= 1

    command = input()

print(*lst, sep=", ")