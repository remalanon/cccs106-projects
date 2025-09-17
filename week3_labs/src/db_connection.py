import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",  # 🔴 Replace with your MySQL password
            database="fletapp"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None
