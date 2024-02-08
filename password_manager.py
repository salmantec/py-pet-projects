# Do not use it in real-life, just for to do the fun project
from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# TODO: Need to include master password based encryption and decryptiong
key = load_key()
fer = Fernet(key)

# To view the username and password
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print(f"Username: {username} | Password: {fer.decrypt(password.encode()).decode()}")

# To add the passwords along with username
def add():
    username = input("Enter account name: ")
    password = input("Enter password: ")

    # Write these details into a file
    with open("passwords.txt", "a") as f:
        f.write(f"{username}|{fer.encrypt(password.encode()).decode()}\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue