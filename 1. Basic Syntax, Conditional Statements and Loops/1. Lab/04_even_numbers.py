lines = int(input())
all_even = True
odd_num = 0
for num in range(lines):
    curr_num = int(input())
    if curr_num % 2 != 0:
        all_even = False
        odd_num += curr_num
        break
if all_even:
    print("All numbers are even.")
else:
    print(f"{odd_num} is odd!")
