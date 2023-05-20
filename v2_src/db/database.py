import os
import dotenv
import mysql.connector
from mysql.connector import Error

def create_db_connection():
    dotenv.load_dotenv(dotenv.find_dotenv())
    connection = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),  # Database host
            user=os.getenv('DB_USER'),  # Database user
            passwd=os.getenv('DB_PASS'),  # Database password
            database=os.getenv('DB_NAME')  # Database name
        )
        print("MySQL Database connection successful")

    except Error as err:
        print(f"Error: '{err}'")

    return connection
