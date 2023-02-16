# def repeat_string(input_word, n):
#     return input_word * n
#
#
# input_string = input()
# n = int(input())
# print(repeat_string(input_string, n))

string_input = input()
n = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string_input, n)
print(result)