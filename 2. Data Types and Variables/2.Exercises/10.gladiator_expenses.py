count_loss_figth = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
total_money = 0
shield_count = 0

for fight in range(1, count_loss_figth + 1):
    if fight % 2 == 0:
        total_money += helmet_price

    if fight % 3 == 0:
        total_money += sword_price
        if fight % 2 == 0:
            total_money += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                total_money += armour_price

print(f"Gladiator expenses: {total_money:.2f} aureus")


