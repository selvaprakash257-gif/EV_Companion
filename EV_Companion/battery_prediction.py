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
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c


def predict_range(
    vehicle,
    variant,
    battery,
    driving_style,
    ac_preference
):

    real_range = vehicles[vehicle][variant]["real_range"]

    estimated_range = (
        battery / 100
    ) * real_range

    if driving_style == "Eco":
        estimated_range *= 1.05

    elif driving_style == "Sport":
        estimated_range *= 0.90

    if ac_preference == "Usually ON":
        estimated_range *= 0.92

    return estimated_range


def get_station_route_distance(
    station,
    route_coordinates
):

    address_info = station.get(
        "AddressInfo",
        {}
    )

    station_latitude = address_info.get(
        "Latitude"
    )

    station_longitude = address_info.get(
        "Longitude"
    )

    if (
        station_latitude is None
        or station_longitude is None
    ):
        return None

    nearest_distance = float("inf")
    nearest_route_distance = 0

    travelled_distance = 0

    for i in range(
        len(route_coordinates) - 1
    ):

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

            nearest_route_distance = (
                travelled_distance
            )

        travelled_distance += segment_distance

    return nearest_route_distance

def recommend_charging_station(
    estimated_range,
    station_results
):

    reachable_stations = []

    for station_distance, station_name in station_results:

        if station_distance < estimated_range:

            reachable_stations.append(
                (
                    station_distance,
                    station_name
                )
            )

    if not reachable_stations:
        return None

    # Choose the farthest reachable station
    recommended_station = max(
        reachable_stations,
        key=lambda x: x[0]
    )

    return recommended_station
def battery_prediction(logged_user):

    user_id = logged_user[0]

    print(
        "\n========== Battery Prediction =========="
    )

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

    battery = int(
        input(
            "Enter Current Battery Percentage: "
        )
    )

    estimated_range = predict_range(
        vehicle,
        variant,
        battery,
        driving_style,
        ac_preference
    )

    print(
        "\nEstimated Range:",
        round(estimated_range, 1),
        "km"
    )

    start, destination, trip_distance = (
        route_planner()
    )

    trip_distance, stations, route_coordinates = (
        create_map(
            start,
            destination
        )
    )

    print(
        "\n========== Charging Station Analysis =========="
    )

    # Check EVERY charging station
    station_results = []

    for station in stations:

        station_distance = (
            get_station_route_distance(
                station,
                route_coordinates
            )
        )

        if station_distance is None:
            continue

        address_info = station.get(
            "AddressInfo",
            {}
        )

        station_name = address_info.get(
            "Title",
            "EV Charging Station"
        )

        station_results.append(
            (
                station_distance,
                station_name
            )
        )

    # Sort stations by distance from start
    station_results.sort(
        key=lambda x: x[0]
    )

    # Display all stations
    for station_distance, station_name in (
        station_results
    ):

        print(
            f"{station_name} - "
            f"{station_distance:.1f} km from start"
        )

    remaining_range = (
        estimated_range - trip_distance
    )

    if remaining_range >= 0:

        print(
            "\nYou can reach your destination!"
        )

        print(
            "Remaining Range:",
            round(remaining_range, 1),
            "km"
        )

    else:

        additional_range = (
            trip_distance - estimated_range
        )

        print(
            "\nBattery may not be sufficient."
        )

        print(
            "Estimated Range:",
            round(estimated_range, 1),
            "km"
        )

        print(
            "Trip Distance:",
            round(trip_distance, 1),
            "km"
        )

        print(
            "Additional Range Needed:",
            round(additional_range, 1),
            "km"
        )

        print(
            "\nCharging Recommendation:"
        )

        print(
            "Charging is required during the journey."
        )

        recommended_station = recommend_charging_station(
            estimated_range,
            station_results
        )

        if recommended_station is not None:

            station_distance, station_name = recommended_station

            print(
                "\nRecommended Charging Station:"
            )

            print(
                "Station:",
                station_name
            )

            print(
                "Distance from start:",
                round(station_distance, 1),
                "km"
            )

        else:

            print(
                "\nNo reachable charging station found "
                "within the estimated range."
            )