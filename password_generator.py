import string
import secrets

def create_pwd(pwd_length=12):
    letters, digits, special_chars = string.ascii_letters, string.digits, string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ""
    pwd_strong = False

    while not pwd_strong:
        pwd = ""

        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2):
            pwd_strong = True

    return pwd

if __name__ == "__main__":
    print(create_pwd())