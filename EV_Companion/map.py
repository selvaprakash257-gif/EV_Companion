import os
import requests
import folium
from dotenv import load_dotenv

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

start = "Chennai"
destination = "Vellore"

places = {
    "Chennai": (13.0827, 80.2707),
    "Vellore": (12.9165, 79.1325)
}

start_coordinates = places[start]
destination_coordinates = places[destination]

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
    print("API Error:", response.text)
else:
    result = response.json()

    distance = result["features"][0]["properties"]["summary"]["distance"] / 1000

    route_coordinates = result["features"][0]["geometry"]["coordinates"]

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
        popup="Starting Location: Chennai",
        tooltip="Chennai"
    ).add_to(ev_map)

    folium.Marker(
        destination_coordinates,
        popup="Destination: Vellore",
        tooltip="Vellore"
    ).add_to(ev_map)

    folium.PolyLine(
        route_for_map,
        tooltip=f"Road Distance: {distance:.1f} km"
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