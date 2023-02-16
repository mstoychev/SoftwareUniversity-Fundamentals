def all_char_between(first, second):
    character_list = []
    for i in range(first + 1, second):
        character_list.append(chr(i))
    return character_list


char1 = ord(input())
char2 = ord(input())
result = all_char_between(char1, char2)
print(" ".join(result))