numbers = list(map(int, input().split()))
command = input()
while command != "End":
    command = command.split()
    action = command[0]
    index = int(command[1])
    if action == "Shoot":
        if 0 <= index < len(numbers):
            power = int(command[2])
            numbers[index] -= power
            if numbers[index] <= 0:
                numbers.remove(numbers[index])
    elif action == "Add":
        if 0 <= index < len(numbers):
            value = int(command[2])
            numbers.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(command[2])
        min_idx = index - radius
        max_idx = index + radius
        if 0 <= min_idx < len(numbers) and 0 <= max_idx < len(numbers):
            del numbers[min_idx:max_idx + 1]
        else:
            print("Strike missed!")

    command = input()

print(*numbers, sep="|")
