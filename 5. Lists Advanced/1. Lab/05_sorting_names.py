names = input().split(", ")
result = sorted(names, key=lambda item: (-len(item), item))  #first sorted with len, second alphabetical
print(result)
