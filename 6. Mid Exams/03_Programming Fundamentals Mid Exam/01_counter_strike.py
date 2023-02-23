energy = int(input())
command = input()
won_battle = True
count = 0

while command != "End of battle":
    reduced = int(command)
    if energy - reduced >= 0:
        energy -= reduced
        count += 1
        if count % 3 == 0:
            energy += count
    else:
        won_battle = False
        break

    command = input()

if won_battle:
    print(f"Won battles: {count}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
    