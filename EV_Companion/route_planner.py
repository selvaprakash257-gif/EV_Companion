import os
import requests
from dotenv import load_dotenv

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
def get_route_distance(start, destination):

    start_coordinates = tamil_nadu_places[start]
    destination_coordinates = tamil_nadu_places[destination]

    url = "https://api.openrouteservice.org/v2/directions/driving-car/json"

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

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print("API Error:", response.text)
        return None

    result = response.json()

    distance_meters = result["routes"][0]["summary"]["distance"]

    return distance_meters / 1000
def choose_location(message):
    places = list(tamil_nadu_places.keys())

    print("\n" + message)

    for i, place in enumerate(places, start=1):
        print(f"{i}. {place}")

    while True:
        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(places):
            return places[int(choice) - 1]

        print("Invalid choice! Please try again.")
def route_planner():

    print("\n========== Tamil Nadu EV Route Planner ==========")

    start = choose_location("Select Starting Location")

    destination = choose_location("Select Destination")

    print("\nStarting Location:", start)
    print("Destination:", destination)

    distance = get_route_distance(start, destination)

    if distance is not None:
        print("Road Distance:", round(distance, 1), "km")

    return distance