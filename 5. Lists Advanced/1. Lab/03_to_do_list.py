task = []
while True:
    command = input()
    if command == "End":
        break

    current_command = command.split("-")
    priority = int(current_command[0])
    current_task = current_command[1]
    task.append((priority, current_task))

result = [element[1] for element in sorted(task)]
print(result)
