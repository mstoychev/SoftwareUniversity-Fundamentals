input_list = input().split()
new_dict = {}
for word in input_list:
    word_lower_case = word.lower()
    if word_lower_case not in new_dict:
        new_dict[word_lower_case] = 1
    else:
        new_dict[word_lower_case] += 1

for key, value in new_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

