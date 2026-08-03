from database import update_battery, check_trip_owner

def update_trip(logged_user):

    user_id = logged_user[0]

    id = int(input("Enter Trip ID: "))

    trip = check_trip_owner(id, user_id)

    if trip:

        battery = int(input("Enter New Battery Percentage: "))

        update_battery(id, battery, user_id)

        print("Battery Updated Successfully!")

    else:

        print("Trip not found or doesn't belong to you.")
    