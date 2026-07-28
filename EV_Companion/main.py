from charging_cost import charging_cost
from view_trip import view_trip
from save_trip import save_trip
while True:
        print("========== EV Companion ==========")
        print("1. Save Trip")
        print("2. View Trip History")
        print("3. Charging Cost Calculator")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            save_trip()

        elif choice == "2":
            view_trip()

        elif choice == "3":
            charging_cost()

        elif choice == "4":
            print("Thank you for using EV Companion!")
            break

        else:
            print("Invalid Choice!")