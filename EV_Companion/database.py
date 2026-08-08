import sqlite3


def save_trip_to_database(user_id, vehicle, battery, destination):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        vehicle TEXT,
        battery INTEGER,
        destination TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO trips(user_id, vehicle, battery, destination)
    VALUES(?, ?, ?, ?)
    """, (user_id, vehicle, battery, destination))

    connection.commit()

    connection.close()

    print("Trip saved in Database!")


def view_trip_database(user_id):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
    "SELECT * FROM trips WHERE user_id = ?",
    (user_id,)
)

    trips = cursor.fetchall()

    for trip in trips:
        print("----------------------------")
        print("ID:", trip[0])
        print("User ID:", trip[1])
        print("Vehicle:", trip[2])
        print("Battery:", trip[3])
        print("Destination:", trip[4])

    connection.close()


def delete_trip(id, user_id):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
    "DELETE FROM trips WHERE id = ? AND user_id = ?",
    (id, user_id)
)

    connection.commit()

    connection.close()

    print("Trip Deleted Successfully!")
def check_trip_owner(id, user_id):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM trips WHERE id = ? AND user_id = ?",
        (id, user_id)
    )

    trip = cursor.fetchone()

    connection.close()

    return trip
def update_battery(id, battery, user_id):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
    "UPDATE trips SET battery = ? WHERE id = ? AND user_id = ?",
    (battery, id, user_id)
    )

    connection.commit()

    connection.close()

    print("Battery Updated Successfully!")
def search_trip(user_id, destination):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
    "SELECT * FROM trips WHERE user_id = ? AND destination = ?",
    (user_id, destination)

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
        password TEXT,
        vehicle TEXT,
        variant TEXT,
        driving_style TEXT,
        ac_preference TEXT
         )
        """)

    connection.commit()

    connection.close()

    print("Users table created!")
def add_profile_columns():

    connection = sqlite3.connect("ev_companion.db")
    cursor = connection.cursor()

    cursor.execute("ALTER TABLE users ADD COLUMN vehicle TEXT")
    cursor.execute("ALTER TABLE users ADD COLUMN variant TEXT")
    cursor.execute("ALTER TABLE users ADD COLUMN driving_style TEXT")
    cursor.execute("ALTER TABLE users ADD COLUMN ac_preference TEXT")

    connection.commit()
    connection.close()

    print("Profile columns added successfully!")

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
def login_user(username, password):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()

    connection.close()

    return user
def get_total_trips(user_id):

    connection = sqlite3.connect("ev_companion.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM trips WHERE user_id = ?",
        (user_id,)
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total
def get_average_battery(user_id):
    connection = sqlite3.connect("ev_companion.db")
    
    cursor = connection.cursor()
    cursor.execute(
        "SELECT AVG(battery)FROM trips WHERE user_id = ?",
        (user_id,)
    )

    average = cursor.fetchone()[0]

    connection.close()

    if average is None:
        return 0

    return average
def get_last_destination(user_id):
    connection = sqlite3.connect("ev_companion.db")
        
    cursor = connection.cursor()
    cursor.execute(
            """SELECT destination 
            FROM trips 
            WHERE user_id = ? 
            ORDER BY id DESC 
            LIMIT 1""",
            (user_id,)
    )
    result = cursor.fetchone()

    connection.close()

    if result is None:
        return "No Trips"

    return result[0]
def update_user_profile(user_id, vehicle, variant, driving_style, ac_preference):

    connection = sqlite3.connect("ev_companion.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE users
    SET vehicle = ?,
        variant = ?,
        driving_style = ?,
        ac_preference = ?
    WHERE id = ?
    """, (vehicle, variant, driving_style, ac_preference, user_id))

    connection.commit()
    connection.close()

    print("Profile Saved Successfully!")
def get_user_profile(user_id):

    connection = sqlite3.connect("ev_companion.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT vehicle, variant, driving_style, ac_preference
    FROM users
    WHERE id = ?
    """, (user_id,))

    profile = cursor.fetchone()

    connection.close()

    return profile