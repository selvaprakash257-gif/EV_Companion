import os
import requests
from dotenv import load_dotenv

load_dotenv()

OCM_API_KEY = os.getenv("OCM_API_KEY")

url = "https://api.openchargemap.io/v3/poi/"

params = {
    "key": OCM_API_KEY,
    "latitude": 13.0827,
    "longitude": 80.2707,
    "distance": 20,
    "distanceunit": "KM",
    "maxresults": 10
}

response = requests.get(url, params=params)

if response.status_code == 200:
    stations = response.json()

    print("Charging Stations Found:", len(stations))

    for station in stations:
        address_info = station.get("AddressInfo", {})

        print("----------------------------")
        print("Station:", address_info.get("Title"))
        print("Address:", address_info.get("AddressLine1"))
        print("Latitude:", address_info.get("Latitude"))
        print("Longitude:", address_info.get("Longitude"))

else:
    print("API Error:", response.status_code)
    print(response.text)