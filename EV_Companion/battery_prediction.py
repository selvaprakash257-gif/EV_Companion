from route_planner import route_planner
from map import create_map
import math
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
def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
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

    start, destination, trip_distance = route_planner()

    trip_distance, stations, route_coordinates = create_map(
        start,
        destination
    )
    print("\n========== Charging Station Analysis ==========")

    for station in stations:

        station_distance = get_station_route_distance(
            station,
            route_coordinates
    )

    address_info = station.get("AddressInfo", {})

    station_name = address_info.get(
        "Title",
        "EV Charging Station"
    )

    print(
    f"{station_name} - "
    f"{station_distance} km from start"
)
    remaining_range = estimated_range - trip_distance

    if remaining_range >= 0:
        print("\nYou can reach your destination!")
        print("Remaining Range:", round(remaining_range, 1), "km")

    else:
        additional_range = trip_distance - estimated_range
        charging_segments = int(trip_distance / estimated_range) + 1
        charging_stops = charging_segments - 1

        print("\nBattery may not be sufficient.")
        print("Estimated Range:", round(estimated_range, 1), "km")
        print("Trip Distance:", round(trip_distance, 1), "km")
        print("Additional Range Needed:", round(additional_range, 1), "km")

        print("\n🔋 Recommendation:")
        print("Charging is required during the journey.")
        print("Approximate Charging Stops:", charging_stops)
def get_station_route_distance(station, route_coordinates):

    address_info = station.get("AddressInfo", {})

    station_latitude = address_info.get("Latitude")
    station_longitude = address_info.get("Longitude")

    if station_latitude is None or station_longitude is None:
        return None

    nearest_distance = float("inf")
    nearest_route_distance = 0

    travelled_distance = 0

    for i in range(len(route_coordinates) - 1):

        lon1, lat1 = route_coordinates[i]
        lon2, lat2 = route_coordinates[i + 1]

        segment_distance = calculate_distance(
            lat1,
            lon1,
            lat2,
            lon2
        )

        distance_to_station = calculate_distance(
            station_latitude,
            station_longitude,
            lat1,
            lon1
        )

        if distance_to_station < nearest_distance:

            nearest_distance = distance_to_station
            nearest_route_distance = travelled_distance

        travelled_distance += segment_distance

    return nearest_route_distance
