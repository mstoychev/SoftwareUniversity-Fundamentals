pass_not_valid = []


def validation_password(password):
    if len(password) < 6 or len(password) > 10:
        pass_not_valid.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        pass_not_valid.append("Password must consist only of letters and digits")

    counter = 0
    for character in password:
        if character.isdigit():
            counter += 1
    if counter < 2:
        pass_not_valid.append("Password must have at least 2 digits")


password_input = input()
validation_password(password_input)
if len(pass_not_valid) == 0:
    print("Password is valid")
else:
    for error in pass_not_valid:
        print(error)
