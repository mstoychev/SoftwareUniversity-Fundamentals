lst = list(map(int, input().split("@")))
command = input()
curr_position = 0
while command != "Love!":
    command = command.split()
    length = int(command[1])
    if curr_position + length <= len(lst) - 1:
        curr_position += length
        if lst[curr_position] > 0:
            lst[curr_position] -= 2
            if lst[curr_position] == 0:
                print(f"Place {curr_position} has Valentine's day.")
        elif lst[curr_position] == 0:
            print(f"Place {curr_position} already had Valentine's day.")
    elif curr_position + length >= len(lst):
        curr_position = 0
        if lst[curr_position] > 0:
            lst[curr_position] -= 2
            if lst[curr_position] == 0:
                print(f"Place {lst[curr_position]} has Valentine's day.")
        elif lst[curr_position] == 0:
            print(f"Place {curr_position} already had Valentine's day.")

    command = input()
print(f"Cupid's last position was {curr_position}.")
if any(lst):
    house_count = len([x for x in lst if x > 0])
    print(f"Cupid has failed {house_count} places.")
else:
    print("Mission was successful.")