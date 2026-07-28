file = open("trip_history.txt", "w")

vehicle = input("Enter Vehicle Model: ")
battery = input("Enter Battery Percentage: ")
destination = input("Enter Destination: ")
file.write("Vehicle:"+ vehicle +"/n")
file.write("Battery:" + battery +"/n")
file.write("Destination: " + destination + "/n")

file.close()

print("Trip saved successfully!")