num_wagons = int(input())
train = [0] * num_wagons #Create a list (train) with the given length containing only zeros
while True:
    command = input()
    if command == "End":
        break

    current_command = command.split(" ")
    action = current_command[0]
    if action == "add":
        num_people = int(current_command[1])
        train[-1] += num_people

    elif action == "insert":
        index = int(current_command[1])
        num_people = int(current_command[2])
        train[index] += num_people

    elif action == "leave":
        index = int(current_command[1])
        num_people = int(current_command[2])
        train[index] -= num_people

print(train)