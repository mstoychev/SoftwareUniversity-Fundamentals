word = input()
reverse = word[::-1]
print(reverse)
##################################################################################################################


def reversed_word(string):
    reversed_str = "".join(reversed(string))
    return reversed_str


word = input()
print(reversed_word(word))
##################################################################################################################
word_input = input()
reversed_words = ""
for i in range(len(word_input)-1, -1, -1):
    reversed_words += word[i]
print(reversed_words)