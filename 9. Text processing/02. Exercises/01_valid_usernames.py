usernames = input().split(", ")
valid = []
for username in usernames:
    if 3 <= len(username) <= 16:
        char_ok = 0
        for char in username:
            if char.isalnum() or char == "-" or char == "_":
                char_ok += 1
            else:
                break  #without using a boolean variable
        if char_ok == len(username):
            valid.append(username)

print(*valid, sep="\n")