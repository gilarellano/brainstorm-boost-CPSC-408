import mysql.connector
from mysql.connector import Error
from models import tables

# Replace these with your own database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "BrainstormBoost"
}

def create_database():
    connection = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
    )

    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {db_config['database']}")
        print(f"Database '{db_config['database']}' created successfully.")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connection.close()


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_tables():
    create_database()
    connection = create_connection()
    if connection:
        for table in tables:
            execute_query(connection, table)
        connection.close()
    else:
        print("Unable to establish connection")


if __name__ == "__main__":
    create_tables()
