n_orders = int(input())
total_orders = 0
for _ in range(n_orders):
    price_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if 0.01 <= price_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2000:
        price = price_capsule * days * capsule_per_day
        total_orders += price
        print(f"The price for the coffee is: ${price:.2f}")
    else:
        pass
print(f"Total: ${total_orders:.2f}")