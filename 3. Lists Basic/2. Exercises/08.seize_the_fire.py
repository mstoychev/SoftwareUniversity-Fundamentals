cells = input().split("#")
water = int(input())
total_fire = 0
processed_cells = []

for cell in cells:
    cell_args = cell.split(" = ")
    level = cell_args[0]
    value = int(cell_args[1])

    if level == "High" and (value < 81 or value > 125):
        continue

    if level == "Medium" and (value < 51 or value > 80):
        continue

    if level == "Low" and (value < 1 or value > 50):
        continue

    if value > water:  #Skip it and try the next one if you do not have enough water to put out a given cell.
        continue

    water -= value
    total_fire += value
    processed_cells.append(value)

print("Cells:")
for processed_cell in processed_cells:
    print(f" - {processed_cell}")

effort = 0.25 * total_fire
print(f"Effort: {effort:.2f}")

print(f"Total Fire: {total_fire}")

