import getpass
import os

user_data_file = 'users.txt'
users = {}

def load_users():
        if os.path.exists(user_data_file):
            with open("user_data_file", "r") as file: 
                for line in file:
                    username, password = line.strip().split(":")
                users[username] = password

def save_users():
    with open(user_data_file, "w") as file:
        for username, password in users.items():
            file.write(f"{username}: {password}\n")



def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exist!")
        return
    password = getpass.getpass("Enter  password: ")
    users[username] = password
    print("Registration Succesful!")

def login():
    username = input("Enter a username: ")
    if username not in users:
        print("Username not found!")
        return
    password = getpass.getpass("Enter your password: ")
    if users[username] == password:
        print("Login Succesfully!")
    else:
        ("incorrect password!")

def change_password():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found!")
        return
    password = getpass.getpass("Enter your current password: ")
    if users[username] == password:
        new_password = getpass.getpass("Enter a new password: ")
        users[username] = new_password
        print("Password changed!")
    else:
        print("Incorrect current password!")

     
def main():

    while True:
        print("\n Login")
        print("a. register")
        print("b. login")
        print("c. change_password")
        print("d. exit")
        
        choice = input("Enter your choice: ")

        if choice == "a":
            register()

        elif choice == "b":
            login()

        elif choice == "c":
            change_password()

        elif choice == "d":
            exit()

        else:
            print("Invalid choice! please try again.")

if __name__ == "__main__":
    main()