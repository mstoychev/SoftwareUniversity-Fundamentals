# A palindrome is a number that reads the same backward as forward
def palindrome_number(number):
    number_as_string = str(number)
    reversed_string = number_as_string[::-1]
    if reversed_string == number_as_string:
        return True
    else:
        return False


number_input = [int(j) for j in input().split(", ")]
for num in number_input:
    result = palindrome_number(num)
    print(result)
