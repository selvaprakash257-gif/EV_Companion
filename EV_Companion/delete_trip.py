from database import delete_trip, check_trip_owner

def delete_trip_menu(logged_user):

    user_id = logged_user[0]

    id = int(input("Enter Trip ID to Delete: "))

    trip = check_trip_owner(id, user_id)

    if trip:

        delete_trip(id, user_id)

        print("Trip Deleted Successfully!")

    else:

        print("Trip not found or doesn't belong to you.")