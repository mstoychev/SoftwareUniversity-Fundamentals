input_lst = list(map(int, input().split(", ")))
positive = []
negative = []
even = []
odd = []
for num in input_lst:
    if num >= 0:
        positive.append(str(num))
    else:
        negative.append(str(num))

    if num % 2 == 0:
        even.append(str(num))
    else:
        odd.append(str(num))
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
