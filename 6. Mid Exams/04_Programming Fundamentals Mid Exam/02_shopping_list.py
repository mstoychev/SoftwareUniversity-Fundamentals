lst = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent":
        if item not in lst:
            lst.insert(0, item)
    elif action == "Unnecessary":
        if item in lst:
            lst.remove(item)
    elif action == "Correct":
        if item in lst:
            new_item = command[2]
            idx = lst.index(item)
            lst.pop(idx)
            lst.insert(idx, new_item)
    elif action == "Rearrange":
        if item in lst:
            lst.remove(item)
            lst.append(item)

    command = input()
print(", ".join(lst))
