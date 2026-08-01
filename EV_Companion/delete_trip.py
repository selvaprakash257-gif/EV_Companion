from database import delete_trip

def delete_trip_menu():

    id = int(input("Enter Trip ID to Delete: "))

    delete_trip(id)