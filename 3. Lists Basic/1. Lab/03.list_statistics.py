positive_list = []
negative_list = []
n = int(input())
positive_counter = 0
negative_sum = 0

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_counter += 1
        positive_list.append(current_number)
    else:
        negative_sum += current_number
        negative_list.append(current_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_counter}")
# print(f"Count of positives: {len(positive_list)}") # To get the count of the positives, we can use the len function.
print(f"Sum of negatives: {negative_sum}")
# print(f"Sum of negatives: {sum(negative_list)}") # To get the sum of the negatives, we can use the sum function.




