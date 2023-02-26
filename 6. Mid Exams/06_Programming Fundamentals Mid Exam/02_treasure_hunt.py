treasure = input().split("|")
command = input()
new = []
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        for i in range(1, len(command)):
            curr_item = command[i]
            if curr_item not in treasure:
                treasure.insert(0, curr_item)
    elif action == "Drop":
        index = int(command[1])
        if index in range(0, len(treasure)):
            remove = treasure.pop(index)
            treasure.append(remove)
    elif action == "Steal":
        count = int(command[1])
        if count < len(treasure):
            new = treasure[-count:]
            treasure = treasure[:-count]
        else:
            new = treasure
            treasure = []
        print(*new, sep=", ")

    command = input()

sum = 0
if not treasure:
    print("Failed treasure hunt.")
else:
    for i in range(len(treasure)):
        length = len(treasure[i])
        sum += length
    average = sum / len(treasure)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
