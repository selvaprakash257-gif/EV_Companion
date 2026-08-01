import sqlite3


def save_trip_to_database(name, vehicle, battery, destination):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        vehicle TEXT,
        battery INTEGER,
        destination TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO trips(name, vehicle, battery, destination)
    VALUES(?, ?, ?, ?)
    """, (name, vehicle, battery, destination))

    connection.commit()

    connection.close()

    print("Trip saved in Database!")


def view_trip_database():

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM trips")

    trips = cursor.fetchall()

    for trip in trips:
        print("----------------------------")
        print("ID:", trip[0])
        print("Name:", trip[1])
        print("Vehicle:", trip[2])
        print("Battery:", trip[3])
        print("Destination:", trip[4])

    connection.close()


def delete_trip(id):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM trips WHERE id = ?", (id,))

    connection.commit()

    connection.close()

    print("Trip Deleted Successfully!")
def update_battery(id, battery):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
        "UPDATE trips SET battery = ? WHERE id = ?",
        (battery, id)
    )

    connection.commit()

    connection.close()

    print("Battery Updated Successfully!")
def search_trip(destination):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM trips WHERE destination = ?",
        (destination,)
    )

    trips = cursor.fetchall()

    if trips:
        for trip in trips:
            print("----------------------------")
            print("ID:", trip[0])
            print("Name:", trip[1])
            print("Vehicle:", trip[2])
            print("Battery:", trip[3])
            print("Destination:", trip[4])
    else:
        print("No trips found!")

    connection.close()
def create_users_table():

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    connection.commit()

    connection.close()

    print("Users table created!")
def register_user(username, password):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO users(username, password)
    VALUES(?, ?)
    """, (username, password))

    connection.commit()

    connection.close()

    print("User Registered Successfully!")