import string
from getpass4 import getpass

def check_password_strength():
    password = getpass(prompt="Enter password:")
    print('password', password)
    strength = 0
    remarks = ""
    lower_count = upper_count = digits_count = whitespace_count = special_char_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            digits_count += 1
        elif char in " ":
            whitespace_count += 1
        else:
            special_char_count += 1


    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if digits_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password.'
            ' You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess.'
            ' But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one hell of a strong password!!!')

    print('Your password has:-')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{digits_count} digits')
    print(f'{whitespace_count} whitespaces')
    print(f'{special_char_count} special characters')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: {remarks}')


def check_pwd(another_pwd = False):
    value = False
    if another_pwd:
        question = 'Do you want to check another password\'s strength (y/n) : '
    else:
        question = 'Do you want to check your password\'s strength (y/n) : '

    choice = input(question)

    while choice not in ["y", "n"]:
        choice = input(question)

    if choice.lower() == "y":
        return True
    else:
        print("Exiting...")
        return False


if __name__ == "__main__":
    print("===== Welcome to Password Strength Checker =====")
    do_check_pwd = check_pwd()
    while do_check_pwd:
        check_password_strength()
        do_check_pwd = check_pwd(True)
