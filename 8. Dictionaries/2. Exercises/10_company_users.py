users = {}

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" -> ")
    company = command[0]
    id_employee = command[1]
    if company not in users:
        users[company] = [id_employee]
    else:
        if id_employee not in users[company]:
            users[company].append(id_employee)

for key, value in users.items():
    print(f"{key}")
    for element in value:
        print(f"-- {element}")


