import sys
number = float(input())
if -sys.maxsize < number < -1000000:
    print("large negative")
elif -1000000 <= number <= -1:
    print("negative")
elif -1 <= number < 0:
    print("small negative")
elif number == 0:
    print("zero")
elif 0 < number < 1:
    print("small positive")
elif 1 <= number <= 1000000:
    print("positive")
else:
    print("large positive")