money_list = input().split(",")
# ["1", "2", "3", "4", "5"]
money_list_as_digit = []
for element in money_list:
    money_list_as_digit.append(int(element))
#[1, 2, 3, 4, 5]

count_of_beggars = int(input())
starting_index = 0
final_sum = []

while starting_index < count_of_beggars:
    sum_for_current_beggar = 0

    for current_index in range(starting_index, len(money_list_as_digit), count_of_beggars):
        sum_for_current_beggar += money_list_as_digit[current_index]

    final_sum.append(sum_for_current_beggar)
    starting_index += 1

print(final_sum)