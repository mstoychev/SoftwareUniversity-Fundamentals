def password_validation(password_user):
    pass_is_valid = True
    length = len(password_user)
    if length < 6 or length > 10:
        pass_is_valid = False
        print("Password must be between 6 and 10 characters")

    if not password_user.isalnum():
        pass_is_valid = False
        print("Password must consist only of letters and digits")

    digit_counter = 0
    for character in password_user:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        pass_is_valid = False
        print("Password must have at least 2 digits")
    return pass_is_valid


input_password = input()
password_is_valid = password_validation(input_password)
if password_is_valid:
    print("Password is valid")
