employee_lst = [int(input()) for _ in range(4)]
efficiency = sum(employee_lst[0:-1])
students = employee_lst[-1]

time = 0
while students > 0:
    time += 1
    if time % 4 == 0:
        continue
    students -= efficiency
print(f"Time needed: {time}h.")