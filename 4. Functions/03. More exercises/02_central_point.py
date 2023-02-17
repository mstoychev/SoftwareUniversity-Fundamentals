import math


def calculate_the_closest(first_x, first_y, second_x, second_y):
    if abs(first_x) + abs(first_y) <= abs(second_x) + abs(second_y):
        print((math.floor(first_x), math.floor(first_y)))
    else:
        print((math.floor(second_x), math.floor(second_y)))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
calculate_the_closest(x1, y1, x2, y2)
