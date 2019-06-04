# Import os (operating system) and pymysql libraries
import os
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # cursor() is default and returns row data as tuples
    # cursor(pymysql.cursors.DictCursor) returns data in dictionary and includes the column names
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        '''
        This is for testing
        result = cursor.fetchall()
        print(result)
        '''
        # To iterate over each row and return the data, we need a for loop
        for row in cursor:
            print(row)

finally:
    # Close the connection to MySQL, regardless of whether code works
    connection.close()