def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def char_is_valid(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def valid_user(name):
    if length_is_valid(name) and char_is_valid(name):
        return True
    else:
        return False


usernames = input().split(", ")
valid = []

for user in usernames:
    if valid_user(user):
        print(user)
