from user import User

def save_trip():

    name = input("Enter Your Name: ")
    vehicle = input("Enter Vehicle Model: ")
    battery = input("Enter Battery Percentage: ")
    destination = input("Enter Destination: ")

    user1 = User(name, vehicle, battery, destination)
    user1.display_details()

    user1.save_to_file()

    print("Trip saved successfully!")