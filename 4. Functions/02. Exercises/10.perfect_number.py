def perfect_number(number):
    for num in range(1, number):
        if input_number % num == 0:
            aliquot_sum.append(num)


aliquot_sum = []
input_number = int(input())
perfect_number(input_number)
if sum(aliquot_sum) == input_number:
    #convert_str_list = [str(j) for j in aliquot_sum]
    # print(" + ".join(convert_str_list))
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
