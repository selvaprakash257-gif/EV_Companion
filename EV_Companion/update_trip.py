from database import update_battery

def update_trip():

    id = int(input("Enter Trip ID: "))
    battery = int(input("Enter New Battery Percentage: "))

    update_battery(id, battery)
    