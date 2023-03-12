input_line = input().split()
for element in input_line:
    print(element * len(element), end="")

# [print(element * len(element), end="") for element in input().split()]