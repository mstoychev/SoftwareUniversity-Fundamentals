text = input()
counter_dict = {}
for char in text:
    if char == " ":
        continue
    if char not in counter_dict:
        counter_dict[char] = 1
    else:
        counter_dict[char] += 1
for key, value in counter_dict.items():
    print(f"{key} -> {value}")
