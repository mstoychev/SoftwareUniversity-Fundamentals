def ascending_order(number_list):
    return sorted(number_list)


def descending_order(number_list):
    return sorted(number_list, reverse=True)


number_as_input = [int(j) for j in input().split(" ")]
result_ascend = ascending_order(number_as_input)
result_decrease = descending_order(number_as_input)
print(result_ascend)
print(result_decrease)