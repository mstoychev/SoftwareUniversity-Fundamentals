days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total = 0
for day in range(1, days + 1):
    if day % 3 == 0:
        total += (1.5 * daily_plunder)  #additional plunder to their total gain, which is 50% of the daily plunder
        if day % 3 == 0 and day % 5 == 0:
            total -= ((30/100) * total)
    elif day % 5 == 0:
        total += daily_plunder
        total -= ((30/100) * total)  #warship, and after the battle, they lose 30% of their total plunder
    else:
        total += daily_plunder

if total >= expected_plunder:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    print(f"Collected only {((total/expected_plunder) * 100):.2f}% of the plunder.")
