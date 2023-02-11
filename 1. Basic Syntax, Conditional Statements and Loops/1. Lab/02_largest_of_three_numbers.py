import sys
largest = - sys.maxsize
for _ in range(3):
    current_num = int(input())
    if current_num > largest:
        largest = current_num
print(largest)