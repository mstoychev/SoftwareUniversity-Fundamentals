def loading_bar(percent):
    for i in range(1, 11):
        if i * 10 <= percent:
            element = "%"
            loaging_list.append(element)
        else:
            element = "."
            loaging_list.append(element)
    return "".join(loaging_list)


input_number = int(input())
loaging_list = []
result = loading_bar(input_number)
if 0 <= input_number < 100:
    print(f"{input_number}% [{result}]")
    print("Still loading...")
else:
    print(f"{input_number}% Complete!")
    print(f"[{result}]")