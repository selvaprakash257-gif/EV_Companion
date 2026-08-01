from database import save_trip_to_database
from user import User

def save_trip():

    name = input("Enter Your Name: ")
    vehicle = input("Enter Vehicle Model: ")
    battery = input("Enter Battery Percentage: ")
    destination = input("Enter Destination: ")

    user1 = User(name, vehicle, battery, destination)
    user1.display_details()

    save_trip_to_database(
    user1.name,
    user1.vehicle,
    user1.battery,
    user1.destination
)

    print("Trip saved successfully!")