employees_happiness = list(map(int, input().split()))
factor = int(input())
# employees_happiness_factored = []
# for employee in employees_happiness:    # just use lambda
#     happiness = factor * employee
#     employees_happiness_factored.append(happiness)
employees = list(map(lambda x: x * factor, employees_happiness))
filtered = list(filter(lambda y: y >= sum(employees) / len(employees), employees))
if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
