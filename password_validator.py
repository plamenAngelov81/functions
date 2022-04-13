def pass_validator(password):
    pass_len = False
    pass_letter_digit = False
    pass_digit_sum = False

    if 6 <= len(password) <= 10:
        pass_len = True
    else:
        print("Password must be between 6 and 10 characters")

    for i in password:
        if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            pass_letter_digit = False
            print("Password must consist only of letters and digits")
            break
        else:
            pass_letter_digit = True

    counter = 0
    for j in password:
        if j in "1234567890":
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
    else:
        pass_digit_sum = True

    if pass_digit_sum and pass_len and pass_letter_digit:
        print("Password is valid")


word = input()

pass_validator(word)
