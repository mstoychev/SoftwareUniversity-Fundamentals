def bill(product, n):
    if product == "coffee":
        return n * 1.50
    elif product == "water":
        return n * 1.00
    elif product == "coke":
        return n * 1.40
    elif product == "snacks":
        return n * 2.00


product = input()
n = int(input())
print(f"{bill(product, n):.2f}")
