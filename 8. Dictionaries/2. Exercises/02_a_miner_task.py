miner_task = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in miner_task:
        miner_task[resource] = quantity
    else:
        miner_task[resource] += quantity

for resource, quantity in miner_task.items():
    print(f"{resource} -> {quantity}")
