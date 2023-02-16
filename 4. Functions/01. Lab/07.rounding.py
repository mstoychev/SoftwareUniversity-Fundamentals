# example of input: 1.0 2.5 3.0 4.5
# expected output: [1, 2, 3, 4]
input_line_converted_to_list = list(map(float, input().split()))
rounded_list = [round(num) for num in input_line_converted_to_list]
print(rounded_list)
