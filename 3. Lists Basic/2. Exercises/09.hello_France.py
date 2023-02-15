ticket_price = 150
#you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup
collection_of_items = input().split("|")
budget = int(input())
incremented_price_line = ""
profit = 0
new_prices_sum = 0

for item in collection_of_items:
    item_args = item.split("->")
    current_item = item_args[0]
    current_price = float(item_args[1])
    incremented_current_price = 0
    flag = False

    if current_item == "Clothes":
        if current_price <= 50.00 and budget >= current_price:
            budget -= current_price
            flag = True

    elif current_item == "Shoes":
        if current_price <= 35.00 and budget >= current_price:
            budget -= current_price
            flag = True

    elif current_item == "Accessories":
        if current_price <= 20.50 and budget >= current_price:
            budget -= current_price
            flag = True

    if flag:
        incremented_current_price = current_price * 1.4
        new_prices_sum += incremented_current_price
        profit += (incremented_current_price - current_price)
        incremented_price_line += (str(round(incremented_current_price, 2)) + " ")

print(incremented_price_line)
print(f"Profit: {profit:.2f}")
if (budget + new_prices_sum) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")