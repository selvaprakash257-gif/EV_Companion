class User:

    def __init__(self, name, vehicle, battery, destination):
        self.name = name
        self.vehicle = vehicle
        self.battery = battery
        self.destination = destination

    def display_details(self):
        print("Name:", self.name)
        print("Vehicle:", self.vehicle)
        print("Battery:", self.battery)
        print("Destination:", self.destination)

    def save_to_file(self):
        file = open("trip_history.txt", "a")

        file.write("Name: " + self.name + "\n")
        file.write("Vehicle: " + self.vehicle + "\n")
        file.write("Battery: " + self.battery + "%\n")
        file.write("Destination: " + self.destination + "\n")
        file.write("-----------------------------\n")

        file.close()