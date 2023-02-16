# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# num_list = [n1, n2, n3]
def smallest_number(num_list):
    return min(num_list)


num_list = []
for _ in range(3):
    number = int(input())
    num_list.append(number)

print(smallest_number(num_list))
