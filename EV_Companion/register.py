from database import register_user

def register():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    register_user(username, password)