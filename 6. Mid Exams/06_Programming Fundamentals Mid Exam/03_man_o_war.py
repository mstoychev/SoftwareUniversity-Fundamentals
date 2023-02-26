ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
health = int(input())
max_health = health
command = input()
while command != "Retire":
    command = command.split()
    action = command[0]
    if action == "Fire":
        idx = int(command[1])
        damage = int(command[2])
        if idx in range(len(war_ship)):
            war_ship[idx] -= damage
            if war_ship[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif action == "Defend":
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx <= len(ship) and 0 <= end_idx <= len(ship):
            for i in range(start_idx, end_idx + 1):
                ship[i] -= damage
                if ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action == "Repair":
        idx = int(command[1])
        repair = int(command[2])
        if idx in range(len(ship)):
            if repair + ship[idx] <= max_health:
                ship[idx] += repair
            else:
                ship[idx] = max_health

    elif action == "Status":
        lower = 0.2 * max_health
        count = len([x for x in ship if x < lower])
        print(f"{count} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(ship)}")
print(f"Warship status: {sum(war_ship)}")
