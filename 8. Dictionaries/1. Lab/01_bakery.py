bakery_lst = input().split()
bakery_dict = {}
for i in range(0, len(bakery_lst), 2):
    key = bakery_lst[i]
    value = bakery_lst[i + 1]
    bakery_dict[key] = int(value)
print(bakery_dict)