list_of_char = input().split(", ")
character = {key:ord(key) for key in list_of_char}
print(character)