health = 100
bitcoins = 0
dungeon = input().split("|")
amount = 0
room_number = 0
alive = True
for room in dungeon:
    room_number += 1
    action = room.split(" ")[0]
    num = int(room.split(" ")[1])

    if action == "potion":
        diff = 0
        if health < 100:
            diff = 100 - health
            health += num
            amount = num
            if health > 100:
                health = 100
                amount = diff
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoins += num
        print(f"You found {num} bitcoins.")

    else:
        if health - num > 0:
            health -= num
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {room_number}")
            alive = False
            break
if alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
