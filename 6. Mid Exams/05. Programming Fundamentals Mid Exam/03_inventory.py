collection = input().split(", ")
command = input()
while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in collection:
            collection.append(item)

    elif action == "Drop":
        if item in collection:
            collection.remove(item)

    elif action == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in collection:
            idx = int(collection.index(old_item)) + 1  #add the new item after the old one
            collection.insert(idx, new_item)

    elif action == "Renew":
        if item in collection:
            collection.remove(item)
            collection.append(item)

    command = input()

print(", ".join(collection))