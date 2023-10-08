# pip install mysql-connector-python streamlit
import streamlit as st

from VoterCRM_database import connection

# Establish a database connection
def create_server_connection(connection):
    # Implement the logic to create the server connection
    if connection is None:
        try:
            cursor = connection.cursor()
            print(" My SQL database connection successful")
        except Exception as err:
            print(f"Error:'{err}'")       
    return connection

def create_and_switch_database(connection, database, switch_db):
    cursor = connection.cursor()
    try:
        drop_query = "DROP DATABASE IF EXISTS " + database
        db_query = " CREATE DATABASE " + database
        switch_query = " USE " + switch_db
        cursor.execute(drop_query)
        cursor.execute(db_query)
        cursor.execute(switch_query)
        print(" Database created successfully")
    except Exception as err:
        print("Error in creating database: '{err}'")

def create_table(connection, table_creation_statement):
    cursor = connection.cursor()
    try:
        cursor.execute(table_creation_statement)
        connection.commit()
        print("Table creation successful")
    except Exception as err:
        print("Error in table creation: '{err}'")


def fetch_voter_data():
    try:
        cursor = connection.cursor()
        cursor.execute(" SELECT * FROM VOTER")
        data = cursor.fetchall()

        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return []

# Streamlit app
def main():
    st.title("Voter Database")

    # fetch data from voter table
    voter_data = fetch_voter_data()
    for row in voter_data:
        print(row)

    # display the data in a streamlit table
    st.write("Voter Data")
    st.table(voter_data)

def close_connection(connection):
    if connection:
        connection.close()

if __name__ == "__main__":
    main()
