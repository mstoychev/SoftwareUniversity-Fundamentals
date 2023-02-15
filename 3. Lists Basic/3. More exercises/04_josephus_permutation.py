list_input = input().split(" ")
people_left_to_kill = len(list_input)
k = int(input()) - 1  #the k person is executed
list_to_print_as_string = []
displacement = 0

while people_left_to_kill != 0:
    displacement = (displacement + k) % people_left_to_kill
    executed = list_input.pop(displacement)
    list_to_print_as_string.append(executed)
    people_left_to_kill -= 1

# list_to_print_as_int = [int(j) for j in list_to_print_as_string]  #the result looks like a list but is it not

string = ",".join(list_to_print_as_string)
print(f"[{string}]")
