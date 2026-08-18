vehicles = {
    "Tata Nexon EV": {
        "30 kWh": {
            "claimed_range": 325,
            "real_range": 260
        },
        "45 kWh": {
            "claimed_range": 489,
            "real_range": 375
        }
    },

    "Tata Punch EV": {
        "25 kWh": {
            "claimed_range": 315,
            "real_range": 250
        },
        "35 kWh": {
            "claimed_range": 468,
            "real_range": 355
        }
    },

    "MG ZS EV": {
        "50.3 kWh": {
            "claimed_range": 461,
            "real_range": 360
        }
    },

    "Mahindra XUV400": {
        "34.5 kWh": {
            "claimed_range": 375,
            "real_range": 280
        },
        "39.4 kWh": {
            "claimed_range": 456,
            "real_range": 330
        }
    }
}
def predict_range(vehicle, variant, battery, driving_style, ac_preference):

    real_range = vehicles[vehicle][variant]["real_range"]

    estimated_range = (battery / 100) * real_range

    if driving_style == "Eco":
        estimated_range = estimated_range * 1.05

    elif driving_style == "Sport":
        estimated_range = estimated_range * 0.90

    if ac_preference == "Usually ON":
        estimated_range = estimated_range * 0.92

    return estimated_range
def battery_prediction(logged_user):

    user_id = logged_user[0]

    print("\n========== Battery Prediction ==========")

    # Get saved profile
    from database import get_user_profile

    profile = get_user_profile(user_id)

    vehicle = profile[0]
    variant = profile[1]
    driving_style = profile[2]
    ac_preference = profile[3]

    print("Vehicle:", vehicle)
    print("Variant:", variant)
    print("Driving Style:", driving_style)
    print("AC Preference:", ac_preference)

    battery = int(input("Enter Current Battery Percentage: "))

    estimated_range = predict_range(
        vehicle,
        variant,
        battery,
        driving_style,
        ac_preference
    )

    print("\nEstimated Range:", round(estimated_range, 1), "km")
