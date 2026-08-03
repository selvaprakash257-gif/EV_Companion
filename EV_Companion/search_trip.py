from database import search_trip

def search_trip_menu(logged_user):

    user_id = logged_user[0]

    destination = input("Enter Destination: ")

    search_trip(user_id, destination)