import os
import dotenv
import mysql.connector
from mysql.connector import Error
from database import create_db_connection
from models import tables

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_database():

    dotenv.load_dotenv(dotenv.find_dotenv())
    # Connect without specifying the database
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASS')
    )
    
    query = "CREATE DATABASE IF NOT EXISTS brainstormboost;"
    execute_query(connection, query)
    
    connection.close()

def main():
    # Create the database
    create_database()

    # Connect to the database
    connection = create_db_connection()

    if connection is not None:
        # Create each table
        for table in tables:
            execute_query(connection, table)
    else:
        print("No connection to the database.")

if __name__ == "__main__":
    main()
