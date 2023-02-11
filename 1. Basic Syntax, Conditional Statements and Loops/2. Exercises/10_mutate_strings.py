initial_str = input()
final_str = input()
initial_lst = list(initial_str)

for i in range(len(initial_str)):
    if initial_str[i] == final_str[i]:
        pass
    else:
        initial_lst.pop(i)
        initial_lst.insert(i, final_str[i])
        print("".join(initial_lst))

# same exercise without using lists
# result = initial_str
# for idx in range(len(final_str)):
#     if initial_str[idx] == final_str[idx]:
#         continue
#     result = final_str[:idx + 1] + initial_str[idx + 1:]
#     print(result)
