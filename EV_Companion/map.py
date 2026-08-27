import os
import requests
import folium
from dotenv import load_dotenv
from charging_stations import get_stations_along_route

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

tamil_nadu_places = {
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Madurai": (9.9252, 78.1198),
    "Trichy": (10.7905, 78.7047),
    "Salem": (11.6643, 78.1460),
    "Tirunelveli": (8.7139, 77.7567),
    "Thanjavur": (10.7870, 79.1378),
    "Erode": (11.3410, 77.7172),
    "Tiruppur": (11.1085, 77.3411),
    "Vellore": (12.9165, 79.1325),
    "Kanchipuram": (12.8342, 79.7036),
    "Dindigul": (10.3673, 77.9803),
    "Thoothukudi": (8.7642, 78.1348),
    "Pondicherry": (11.9416, 79.8083)
}


def create_map(start, destination):

    start_coordinates = tamil_nadu_places[start]
    destination_coordinates = tamil_nadu_places[destination]
    

    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"

    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "coordinates": [
            [start_coordinates[1], start_coordinates[0]],
            [destination_coordinates[1], destination_coordinates[0]]
        ]
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    if response.status_code != 200:
        print("Map API Error:", response.text)
        return

    result = response.json()

    distance = (
        result["features"][0]["properties"]["summary"]["distance"]
        / 1000
    )

    route_coordinates = result["features"][0]["geometry"]["coordinates"]
    stations = get_stations_along_route(route_coordinates)

    print("Charging Stations Found:", len(stations))

    route_for_map = [
        [coordinate[1], coordinate[0]]
        for coordinate in route_coordinates
    ]

    map_center = [
        (start_coordinates[0] + destination_coordinates[0]) / 2,
        (start_coordinates[1] + destination_coordinates[1]) / 2
    ]

    ev_map = folium.Map(
        location=map_center,
        zoom_start=8
    )

    folium.Marker(
        start_coordinates,
        popup=f"Starting Location: {start}",
        tooltip=start
    ).add_to(ev_map)

    folium.Marker(
        destination_coordinates,
        popup=f"Destination: {destination}",
        tooltip=destination
    ).add_to(ev_map)

    folium.PolyLine(
        route_for_map,
        tooltip=f"Road Distance: {distance:.1f} km"
    ).add_to(ev_map)
    for station in stations:

        address_info = station.get("AddressInfo", {})

    station_name = address_info.get("Title", "EV Charging Station")
    latitude = address_info.get("Latitude")
    longitude = address_info.get("Longitude")
    address = address_info.get("AddressLine1", "Address not available")

    if latitude is not None and longitude is not None:

        folium.Marker(
    [latitude, longitude],
    popup=f"{station_name}<br>{address}",
    tooltip="⚡ EV Charging Station",
    icon=folium.Icon(
        color="green",
        icon="flash",
        prefix="glyphicon"
    )
).add_to(ev_map)

    file_path = os.path.join(
        os.path.dirname(__file__),
        "tamil_nadu_map.html"
    )

    ev_map.save(file_path)

    print("Map created successfully!")
    print("Starting Location:", start)
    print("Destination:", destination)
    print("Road Distance:", round(distance, 1), "km")

    return distance, stations, route_coordinates