from cryptography.fernet import Fernet


def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():
    print("All info is listed below: \n")
    with open("pass.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username: ", username)
            print("Password: ", fernet.decrypt(password.encode()).decode())
            # print("Password: ", password)


def add():
    name = input("Enter Account Name? \n")
    pwd = input("Enter Password? \n")

    with open("pass.txt", "a") as f:
        f.write(name + "|" + fernet.encrypt(pwd.encode()).decode() + "\n")


master_pwd = input("Master Pass? \n")
# create_key()
key = load_key() + master_pwd.encode()

fernet = Fernet(key)


while True:
    mode = input("add new one or view the current one?(A) or (V) or press q to quit \n")

    if mode == "q":
        break

    if mode == "V":
        view()
    elif mode == "A":
        add()
    else:
        print("invalid input")
