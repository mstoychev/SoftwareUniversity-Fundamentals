schedule = input().split(", ")
command = input()
while True:
    if command == "course start":
        break
    command = command.split(":")
    action = command[0]
    title = command[1]
    if action == "Add":
        if title not in schedule:
            schedule.append(title)
    elif action == "Insert":
        index = int(command[2])
        if title not in schedule:
            schedule.insert(index, title)
    elif action == "Remove":
        if title in schedule:
            schedule.remove(title)
    elif action == "Swap":
        second_title = command[2]
        first_idx = schedule.index(title)
        second_idx = schedule.index(second_title)
        schedule[first_idx], schedule[second_idx] = schedule[second_idx], schedule[first_idx]
    elif action == "Exercise":
        new_title = title + "-Exercise"
        if title not in schedule:
            schedule.append(new_title)
        else:
            if "-Exercise" not in schedule:
                idx = schedule.index(title)
                schedule.remove(title)
                schedule.insert(idx, new_title)

    command = input()

task = 0
for course in schedule:
    task += 1
    print(f"{task}.{course}")
