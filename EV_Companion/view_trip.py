def view_trip():

    file = open("trip_history.txt", "r")

    data = file.read()

    print(data)

    file.close()