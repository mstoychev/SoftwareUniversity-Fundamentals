# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers
lst_numbers = list(map(int, input().split(", ")))
index_list = []
for i in range(len(lst_numbers)):
    if lst_numbers[i] % 2 == 0:
        index_list.append(i)
print(index_list)
