def even_num_in_list(list_as_nums):
    return list(filter(lambda x: x % 2 == 0, list_as_nums))


list_of_numbers = [int(j) for j in input().split(" ")]
filtered_list = even_num_in_list(list_of_numbers)
print(filtered_list)
