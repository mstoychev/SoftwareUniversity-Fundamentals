import math
students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendances = 0
for i in range(1, students + 1):
    attendances = int(input())
    bonus = (attendances / lectures) * (5 + additional_bonus)
    if attendances > max_attendances:
        max_attendances = attendances
        max_bonus = bonus
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
