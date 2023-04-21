# establishes connection with database to insert new player or verify existing one

import mysql.connector
import traceback


def db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Jump_Jump_Dash"
    )
    return db


def signup(username, passw):
    try:
        my_db = db_connection()
        mycursor = my_db.cursor()
        query = "SELECT PlayerName, Password FROM Player_Info WHERE PlayerName = '" + \
            username+"' LIMIT 1"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row == None:
            mycursor.execute(
                "INSERT INTO Player_Info (PlayerName, Password) VALUES (%s,%s)", (username, passw))
            my_db.commit()
            return 1    # Sign up successful
        else:
            return 2    # Username already exists

    except Exception:
        traceback.print_exc()
        return 3        # some other exception

    finally:
        mycursor.close()
        my_db.close()


def verify_login(username, passw):
    try:
        my_db = db_connection()
        mycursor = my_db.cursor()
        query = "SELECT PlayerName, Password FROM Player_Info WHERE PlayerName = '" + \
            username+"' LIMIT 1"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row == None:
            return 3   # invalid username
        else:
            print("Row found")
            if passw == row[1]:
                return 1     # authentication successful
            else:
                return 2    # invalid password

    except Exception:
        traceback.print_exc()
        return 4        # some other exception

    finally:
        mycursor.close()
        my_db.close()
