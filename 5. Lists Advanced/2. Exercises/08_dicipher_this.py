code = input().split()
for index, word in enumerate(code):
    number = ""
    letters = ""

    for char in word:
        if char.isdigit():
            number += char
            continue

        letters += char
    number = chr(int(number))
    current_word = number + letters
    code[index] = current_word

    word = code[index]  # here we have transform numbers in word to letters
    word = [char for char in word]  #switch in list
    word[1], word[-1] = word[-1], word[1]  # the second and the last letter are switched
    word = "".join(word)

    print(word, end=" ")


