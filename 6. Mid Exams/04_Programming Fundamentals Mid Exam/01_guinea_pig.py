food = float(input())
hay = float(input())
cover = float(input())
pig_weight = float(input())
enough_care = True  # food, hay or cover
for day in range(1, 31):
    if food - 0.3 > 0:
        food -= 0.3
    else:
        enough_care = False
        break

    if day % 2 == 0:
        amount_hay = 0.05 * food
        if hay - amount_hay > 0:
            hay -= amount_hay
        else:
            enough_care = False
            break

    if day % 3 == 0:
        amount_cover = 1/3 * pig_weight
        if cover - amount_cover > 0:
            cover -= amount_cover
        else:
            enough_care = False
            break

if enough_care:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")