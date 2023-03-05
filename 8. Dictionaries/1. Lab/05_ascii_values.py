ascii_dict = {}
char_list = input().split(", ")
for char in char_list:
    key = char
    value = ord(char)
    if key not in ascii_dict:
        ascii_dict[key] = value

print(ascii_dict)