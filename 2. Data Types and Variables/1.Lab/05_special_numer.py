number = int(input())

for i in range(1, number + 1):
    i_str = str(i)
    summation = 0
    for j in range(len(i_str)):
        summation += int(i_str[j])

    if summation == 5 or summation == 7 or summation == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

#n = int(input())
#for num in range(1, n + 1):
   # sum_of_digits = 0
    #digits = num
   # while digits > 0:
        #sum_of_digits += digits % 10
        #digits = int(digits / 10)
