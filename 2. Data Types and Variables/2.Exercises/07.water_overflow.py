capacity = 255
n = int(input())     #the number of lines, which will follow
total = 0

for _ in range(n):
    current_liters = int(input())
    total += current_liters

    if total <= capacity:
        continue
    else:
        total -= current_liters
        print("Insufficient capacity!")

print(total)
