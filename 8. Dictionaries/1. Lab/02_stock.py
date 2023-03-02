stock = input().split()
products = input().split()
stock_dict = {}
for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    stock_dict[key] = int(value)

for element in products:
    if element in stock_dict.keys():
        print(f"We have {stock_dict[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")