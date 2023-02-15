list_of_integers = [int(j) for j in input().split(" ")]
middle_of_list = len(list_of_integers) // 2
left_side_list = list_of_integers[0:middle_of_list]
right_side_list = list_of_integers[-1: middle_of_list: -1]
left_side_time = 0
right_side_time = 0

for current_num in left_side_list:
    if current_num == 0:
        left_side_time *= 0.8

    left_side_time += current_num

for current_num in right_side_list:
    if current_num == 0:
        right_side_time *= 0.8

    right_side_time += current_num

if left_side_time < right_side_time:
    print(f"The winner is left with total time: {left_side_time:.1f}")
elif left_side_time > right_side_time:
    print(f"The winner is right with total time: {right_side_time:.1f}")
else:
    pass

