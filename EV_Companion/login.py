from database import login_user

def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    user = login_user(username, password)

    if user:
        print("Login Successful!")
        return True
    else:
        print("Invalid Username or Password!")
        return False