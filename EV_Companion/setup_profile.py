from database import update_user_profile


def setup_profile(logged_user):

    user_id = logged_user[0]

    print("============================")
    print(" Complete Your EV Profile ")
    print("============================")

    # Vehicle
    print("1. Tata Nexon EV")
    print("2. Tata Punch EV")
    print("3. MG ZS EV")
    print("4. Mahindra XUV400")

    choice = input("Choose your vehicle: ")

    if choice == "1":
        vehicle = "Tata Nexon EV"
        print("\nChoose Battery Variant")
        print("1. 30 kWh")
        print("2. 45 kWh")

        variant_choice = input("Enter your choice: ")

        if variant_choice == "1":
            variant = "30 kWh"
        elif variant_choice == "2":
            variant = "45 kWh"
        else:
            print("Invalid Choice!")
            return

    elif choice == "2":
        vehicle = "Tata Punch EV"
        print("\nChoose Battery Variant")
        print("1. 25 kWh")
        print("2. 35 kWh")

        variant_choice = input("Enter your choice: ")

        if variant_choice == "1":
            variant = "25 kWh"
        elif variant_choice == "2":
            variant = "35 kWh"
        else:
            print("Invalid Choice!")
            return

    elif choice == "3":
        vehicle = "MG ZS EV"
        variant = "50.3 kWh"

    elif choice == "4":
        vehicle = "Mahindra XUV400"
        print("\nChoose Battery Variant")
        print("1. 34.5 kWh")
        print("2. 39.4 kWh")

        variant_choice = input("Enter your choice: ")

        if variant_choice == "1":
            variant = "34.5 kWh"
        elif variant_choice == "2":
            variant = "39.4 kWh"
        else:
            print("Invalid Choice!")
            return

    else:
        print("Invalid Choice!")
        return

    # Driving Style
    print("\nDriving Style")
    print("1. Eco")
    print("2. Normal")
    print("3. Sport")

    driving_choice = input("Choose your driving style: ")

    if driving_choice == "1":
        driving_style = "Eco"
    elif driving_choice == "2":
        driving_style = "Normal"
    elif driving_choice == "3":
        driving_style = "Sport"
    else:
        print("Invalid Choice!")
        return

    # AC Preference
    print("\nAC Preference")
    print("1. Usually ON")
    print("2. Usually OFF")

    ac_choice = input("Choose your preference: ")

    if ac_choice == "1":
        ac_preference = "Usually ON"
    elif ac_choice == "2":
        ac_preference = "Usually OFF"
    else:
        print("Invalid Choice!")
        return

    # Save profile
    update_user_profile(
        user_id,
        vehicle,
        variant,
        driving_style,
        ac_preference
    )