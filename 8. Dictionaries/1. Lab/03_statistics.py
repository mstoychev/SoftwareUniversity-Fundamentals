dict_product = {}
command = input()
while command != "statistics":
    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in dict_product.keys():
        dict_product[key] = value
    else:
        dict_product[key] += value

    command = input()

print("Products in stock:")
for key in dict_product.keys():
    print(f"- {key}: {dict_product[key]}")
print(f"Total Products: {len(dict_product.keys())}")
print(f"Total Quantity: {sum(dict_product.values())}")
