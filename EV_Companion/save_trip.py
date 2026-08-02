from database import save_trip_to_database

def save_trip(logged_user):

    user_id = logged_user[0]

    vehicle = input("Enter Vehicle Model: ")
    battery = input("Enter Battery Percentage: ")
    destination = input("Enter Destination: ")

    save_trip_to_database(
        user_id,
        vehicle,
        battery,
        destination
    )

    print("Trip saved successfully!")