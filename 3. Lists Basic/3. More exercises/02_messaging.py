input_numbers = input().split(" ")
list_numbers = []
input_text = input()
modified_text = ""
for i in input_text:
    modified_text += i + "-"
modified_text = modified_text.split("-")
modified_text.pop()
# print(modified_text)
final_list = []

for number in input_numbers:
    searched_index = 0
    for i in number:
        char = i
        searched_index += int(char)

    while True:
        length = len(modified_text) - 1
        if searched_index > length:
            searched_index -= len(input_text)

        message_char = modified_text.pop(searched_index)
        final_list.append(message_char)
        break

for j in final_list:
    print(j, end="")

