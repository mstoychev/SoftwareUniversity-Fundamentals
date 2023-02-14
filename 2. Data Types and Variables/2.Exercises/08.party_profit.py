group_size = int(input())
days = int(input())
total_coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2

    if i % 15 == 0:
        group_size += 5

    total_coins += 50     #earn 50 coins every day
    total_coins -= 2*group_size     #spend 2 coins per companion for food
    if i % 3 == 0:
        total_coins -= 3*group_size  #motivational party, spending 3 coins per companion

    if i % 5 == 0:
        total_coins += 20*group_size  #gain 20 coins per companion
        if i % 3 == 0:
            total_coins -= 2*group_size

print(f"{group_size} companions received {total_coins // group_size} coins each.")
