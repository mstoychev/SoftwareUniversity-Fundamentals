budget = float(input())
flour_price = float(input())
loaf = (1 * flour_price) + (1 * 0.75 * flour_price) + (0.25 * 1.25 * flour_price)
colored_eggs = 0
bread = 0
while True:
    if budget - loaf < 0:
        break
    budget -= loaf
    bread += 1
    colored_eggs += 3
    if bread % 3 == 0:
        colored_eggs -= (bread - 2)
print(f"You made {bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
