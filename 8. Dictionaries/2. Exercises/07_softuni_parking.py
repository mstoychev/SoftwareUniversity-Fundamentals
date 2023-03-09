n = int(input())
parking = {}

for _ in range(n):
    command = input().split()
    register = command[0]
    username = command[1]
    if register == "register":
        license_num = command[-1]
        key, value = username, license_num
        if key not in parking:
            parking[key] = value
            print(f"{key} registered {value} successfully")
        else:
            print(f"ERROR: already registered with plate number {value}")
    elif register == "unregister":
        if username in parking:
            print(f"{username} unregistered successfully")
            del parking[username]
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")