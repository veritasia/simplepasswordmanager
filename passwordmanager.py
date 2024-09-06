#should not be used for actually confidential stuff
#followed https://youtu.be/DLn3jOsNRVE
from cryptography.fernet import Fernet

masterpwd = input("What is the master password?\n")

'''
def WriteKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def LoadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = LoadKey() + masterpwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"user: {user}, password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True: 
    mode = input("Would you like to view you existing passwords or add a new one? (view, add, q): ").lower()

    #straight up exit from the program
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue