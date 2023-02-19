first_input_line = input().split(", ")
second_input_line = input().split(", ")
new_lst = []
for element in first_input_line:
    for word in second_input_line:
        if element in word:
            new_lst.append(element)
            break
print(new_lst)