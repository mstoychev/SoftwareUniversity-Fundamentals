factor = int(input())
count = int(input())
my_list = [] #create a list with a length of the given count that contains
# only integer numbers, which are multiples of the given factor

for i in range(1, count + 1):
    element_generated = i * factor
    my_list.append(element_generated)
print(my_list)
