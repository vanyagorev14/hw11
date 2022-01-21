import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user_name = user_name,
            user_password = user_password
        )
        print("Connection to MySql DB succ.")
    except Error as e:
        print(f"The error '{e}' is occured")

    return connection
