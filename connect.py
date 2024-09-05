import mysql.connector

# Initialize a variable to hold the database connection
conn = None

try:
    # Attempt to establish a connection to the MySQL database
    conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='pub',
                                   user='<user>',
                                   password='<password>')
    
    # Check if the connection is successfully established
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    # Print an error message if a connection error occurs
    print(e)

finally:
    # Close the database connection in the 'finally' block to ensure it happens
    if conn is not None and conn.is_connected():
        conn.close()

from mysql.connector import MySQLConnection, Error
from config import read_config


def connect(config):
    """ Connect to MySQL database """
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**config)

        if conn.is_connected():
            print('Connection is established.')
        else:
            print('Connection is failed.')
    except Error as error:
        print(error)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection is closed.')


if __name__ == '__main__':
    config = read_config()
    connect(config)