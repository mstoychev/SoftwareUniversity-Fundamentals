input_line = input().split(", ")
list_integers = []
counter = 0

for element in input_line:
    num_int = int(element)
    list_integers.append(num_int)

for i in range(len(list_integers)):
    int_element = list_integers[i]
    if int_element == 0:
        counter += 1

for _ in range(counter):
    list_integers.remove(0)

for _ in range(len(input_line) - len(list_integers)):
    list_integers.append(0)

print(list_integers)




