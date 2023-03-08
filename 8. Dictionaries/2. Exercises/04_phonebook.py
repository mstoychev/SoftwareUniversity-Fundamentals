phone_data_base = {}
command = input()
while "-" in command:
    phone_nums = command.split("-")
    name = phone_nums[0]
    tlf = phone_nums[1]
    phone_data_base[name] = tlf
    command = input()
n = int(command)
for _ in range(n):
    name = input()
    if name in phone_data_base.keys():
        print(f"{name} -> {phone_data_base[name]}")
    else:
        print(f"Contact {name} does not exist.")
