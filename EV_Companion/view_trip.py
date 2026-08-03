from database import view_trip_database

def view_trip(logged_user):

    user_id = logged_user[0]

    view_trip_database(user_id)