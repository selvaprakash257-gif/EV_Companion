import os
import requests
from dotenv import load_dotenv

load_dotenv()

OCM_API_KEY = os.getenv("OCM_API_KEY")


def get_charging_stations(latitude, longitude):

    url = "https://api.openchargemap.io/v3/poi/"

    params = {
        "key": OCM_API_KEY,
        "latitude": latitude,
        "longitude": longitude,
        "distance": 20,
        "distanceunit": "KM",
        "maxresults": 10
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Charging Station API Error:", response.status_code)
        return []

    return response.json()


def get_stations_along_route(route_coordinates):

    all_stations = []

    route_points = route_coordinates[::max(1, len(route_coordinates) // 10)]

    for i, coordinate in enumerate(route_points, start=1):

        print(f"Searching charging stations: {i}/{len(route_points)}")

    longitude = coordinate[0]
    latitude = coordinate[1]

    stations = get_charging_stations(
        latitude,
        longitude
    )
    all_stations.extend(stations)

    # Remove duplicate stations
    unique_stations = {}

    for station in all_stations:

        address_info = station.get("AddressInfo", {})

        station_id = address_info.get("ID")
        latitude = address_info.get("Latitude")
        longitude = address_info.get("Longitude")

    if (
        station_id is not None
        and latitude is not None
        and longitude is not None
    ):
        unique_stations[station_id] = station

    return list(unique_stations.values())