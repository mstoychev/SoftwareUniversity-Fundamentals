orders = {}
while True:
    command = input()
    if command == "buy":
        break
    command = command.split()
    key = command[0]
    value = [float(command[1]), int(command[2])]
    if key not in orders:
        orders[key] = value
    else:
        orders[key][0] = value[0]
        orders[key][1] += value[1]

for key, value in orders.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")


