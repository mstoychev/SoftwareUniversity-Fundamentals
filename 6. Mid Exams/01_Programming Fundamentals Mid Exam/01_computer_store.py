command = input()
total = 0
while True:
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total += price
    command = input()

taxes = 0.2 * total
final = total + taxes
if command == "special":
    final *= 0.9

if total == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final:.2f}$")



