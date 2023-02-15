current_energy = 100
current_coins = 100
list_of_events = input().split("|")
bakery_is_open = True
for event in list_of_events:
    event_info = event.split("-")
    type_of_event = event_info[0]
    number = int(event_info[1])
    if type_of_event == "rest":
        temporary_energy = current_energy
        current_energy += number
        if current_energy > 100:  #Note: your energy cannot exceed your initial energy (100).
            current_energy = 100
            gained_energy = current_energy - temporary_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {current_energy}.")
        else:
            gained_energy = current_energy - temporary_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {current_energy}.")

    elif type_of_event == "order":
        if current_energy >= 30:
            current_energy -= 30
            current_coins += number
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if current_coins >= number:
            current_coins -= number
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bakery_is_open = False
            break

if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
