from database import get_user_profile


def charging_cost(logged_user):

    user_id = logged_user[0]

    profile = get_user_profile(user_id)

    vehicle = profile[0]
    variant = profile[1]

    print("\n========== Charging Cost Calculator ==========")
    print("Vehicle:", vehicle)
    print("Battery Variant:", variant)

    battery_capacity = {
        "Tata Nexon EV": {
            "30 kWh": 30,
            "45 kWh": 45
        },

        "Tata Punch EV": {
            "25 kWh": 25,
            "35 kWh": 35
        },

        "MG ZS EV": {
            "50.3 kWh": 50.3
        },

        "Mahindra XUV400": {
            "34.5 kWh": 34.5,
            "39.4 kWh": 39.4
        }
    }

    capacity = battery_capacity[vehicle][variant]

    current_battery = float(
        input("Enter Current Battery Percentage: ")
    )

    target_battery = float(
        input("Enter Target Battery Percentage: ")
    )

    price_per_unit = float(
        input("Enter Price Per Unit (₹): ")
    )

    energy_needed = capacity * (
        (target_battery - current_battery) / 100
    )

    total_cost = energy_needed * price_per_unit

    print("\nEnergy Needed:", round(energy_needed, 2), "kWh")
    print("Charging Cost: ₹", round(total_cost, 2))