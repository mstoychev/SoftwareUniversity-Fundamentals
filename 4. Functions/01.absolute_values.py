# #solution 1 --> with 2 for loops
# input_list = input().split()
# list_of_numbers = []
# for n in input_list:
#     list_of_numbers.append(float(n))
# list_of_absolute_numbers = []
# for n in list_of_numbers:
#     absolute_number = abs(n)
#     list_of_absolute_numbers.append(absolute_number)
# print(list_of_absolute_numbers)

#solution 2 --> with list comprehension
# input_string = [abs(float(j)) for j in input().split()]
# print(input_string)

#solution 3 --> using map() function
input_string = list(map(float, input().split(" ")))
abs_result = [abs(num) for num in input_string]
print(input_string)