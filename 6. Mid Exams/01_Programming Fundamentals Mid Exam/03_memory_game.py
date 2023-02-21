sequence = list(map(str, input().split()))
moves = 0
command = input()
while command != "end":
    moves += 1
    command_lst = [int(x) for x in command.split()]
    first_idx = command_lst[0]
    second_idx = command_lst[1]
    if sequence[first_idx] == sequence[second_idx]:
        print(f"Congrats! You have found matching elements - {sequence[first_idx]}!")
        del sequence[first_idx]
        if first_idx < second_idx:
            second_idx -= 1
        del sequence[second_idx]
    elif first_idx == second_idx or not 0 <= first_idx < len(sequence) or not 0 <= second_idx < len(sequence):
        half = len(sequence) // 2
        message = f"-{moves}a"
        sequence.insert(half, message)
        sequence.insert(half, message)
        print("Invalid input! Adding additional elements to the board")
    else:
        print("Try again!")

    if not sequence:
        break

    command = input()


if sequence:
    print("Sorry you lose :(")
    print(*sequence)
else:
    print(f"You have won in {moves} turns!")
