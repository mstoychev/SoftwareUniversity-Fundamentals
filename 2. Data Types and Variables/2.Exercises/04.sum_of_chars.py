n = int(input())
total_sum = 0

for _ in range(n):
    character = input()
    ascii_convert = ord(character)
    total_sum += ascii_convert
print(f"The sum equals: {total_sum}")
