# import section

import mysql.connector
from mysql.connector import Error
import config

# initialize connection
def dbConnection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        print("Connection successful!")
    except Error as E:
        print(f"Checkout error: '{E}'.")

    return connection


# test connection to database
connection = dbConnection()
