n = int(input())
searched_word = input()
my_list = []
filtered = []

for _ in range(n):
    current_word = input()
    my_list.append(current_word)
print(my_list)

for i in range(len(my_list)):
    element = my_list[i]
    if searched_word in element:
        filtered.append(element)

print(filtered)