from database import get_total_trips
from database import get_average_battery
from database import get_total_trips, get_average_battery, get_last_destination

def dashboard(logged_user):


    user_id = logged_user[0]
    username = logged_user[1]

    total = get_total_trips(user_id)
    average = get_average_battery(user_id)
    last_destination = get_last_destination(user_id)
    print("==============================")
    print("      EV Companion")
    print("==============================")
    print(f"Welcome {username}")
    print()
    print(f"Total Trips : {total}")
    print(f"Average Battery : {average:.1f}%")
    print(f"Last Destination : {last_destination}")
    print("==============================")