from battery_prediction import battery_prediction
from database import get_user_profile
from setup_profile import setup_profile
from dashboard import dashboard
from register import register
from login import login
from search_trip import search_trip_menu
from update_trip import update_trip
from delete_trip import delete_trip_menu
from charging_cost import charging_cost
from view_trip import view_trip
from save_trip import save_trip


def ev_menu(logged_user):

    while True:
        print("1. Save Trip")
        print("2. View Trip History")
        print("3. Battery Prediction")
        print("4. Charging Cost Calculator")
        print("5. Delete Trip")
        print("6. Update Battery")
        print("7. Search Trip")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            save_trip(logged_user)

        elif choice == "2":
            view_trip(logged_user)

        elif choice == "3":
            battery_prediction(logged_user)

        elif choice == "4":
            charging_cost(logged_user)

        elif choice == "5":
            delete_trip_menu(logged_user)

        elif choice == "6":
            update_trip(logged_user)

        elif choice == "7":
            search_trip_menu(logged_user)

        elif choice == "8":
            print("Logged out successfully!")
            break

        else:
            print("Invalid Choice!")


while True:

    print("\n========== Welcome ==========")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":

        logged_user = login()

        if logged_user:

            profile = get_user_profile(logged_user[0])

            if profile[0] is None:
                setup_profile(logged_user)

            dashboard(logged_user)
            ev_menu(logged_user)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")