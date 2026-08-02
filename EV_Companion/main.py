from register import register
from login import login
from search_trip import search_trip_menu
from update_trip import update_trip
from delete_trip import delete_trip_menu
from charging_cost import charging_cost
from view_trip import view_trip
from save_trip import save_trip


def ev_menu(logged_user):
    print(f"Welcome {logged_user[1]}!")

    while True:
        print("\n========== EV Companion ==========")
        print("1. Save Trip")
        print("2. View Trip History")
        print("3. Charging Cost Calculator")
        print("4. Delete Trip")
        print("5. Update Battery")
        print("6. Search Trip")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
             save_trip(logged_user)

        elif choice == "2":
            view_trip()

        elif choice == "3":
            charging_cost()

        elif choice == "4":
            delete_trip_menu()

        elif choice == "5":
            update_trip()

        elif choice == "6":
            search_trip_menu()

        elif choice == "7":
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
            ev_menu(logged_user)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
