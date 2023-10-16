from logging import exception
import mysql.connector
from VoterCRM_database import *

# Database connection parameters
user = "root"
host = "127.0.0.1"
password = "streamlit"
database = "VOTER_DATA"


def create_server_connection(host_name, user_name, user_password, data_base):
    # Implement the logic to create the server connection
        try:
            connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                    database=data_base,
                    auth_plugin = 'mysql_native_password'
                )
            print("MySQL database connection successful")
            return connection
        except Exception as err:
            print(f"Error: {err}")
            return None

        
# Call the function with the global parameters
connection = create_server_connection(host, user, password, database)

if connection is not None:
    cursor = connection.cursor()
    # You can now use the cursor to execute SQL queries or other database operations
else:
    print("Connection to the database was not successful. Check your connection parameters and make sure the database server is running.")


