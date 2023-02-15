input_string = input()    #single string containing positive and negative numbers separated by a single space
my_list = input_string.split(" ")
inverted_list = []
for i in range(len(my_list)):
    invert_element = int(my_list[i]) * -1
    inverted_list.append(invert_element)
print(inverted_list)
