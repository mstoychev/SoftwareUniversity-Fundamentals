my_list = input().split()
n = int(input())
my_list_int = []
my_list_str = []

for i in range(len(my_list)):   #need a list with numbers for using min()
    element_int = int(my_list[i])
    my_list_int.append(element_int)

for _ in range(n):
    smallest_num = min(my_list_int)
    my_list_int.remove(smallest_num)

for j in range(len(my_list_int)):    #need a list with str for using join method
    element_str = str(my_list_int[j])
    my_list_str.append(element_str)

print(", ".join(my_list_str))

