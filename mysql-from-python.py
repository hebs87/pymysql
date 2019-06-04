# Import os (operating system) and pymysql libraries
import os
# CREATING TABLE LESSON - Import datetime, as this will be one of our col values
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

'''
*********************************TESTING***************************************
try:
    # cursor() is default and returns row data as tuples
    # cursor(pymysql.cursors.DictCursor) returns data in dictionary and includes the column names
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        
        This is for testing
        result = cursor.fetchall()
        print(result)
        
        # To iterate over each row and return the data, we need a for loop
        for row in cursor:
            print(row)
'''

'''
CREATING AND INSERTING INTO TABLE
try:
    # Use default cursor as we aren't pulling data from the table
    with connection.cursor() as cursor:
        # 2. Values for the table stored in a tuple
        row = ("Bob", 21, "1990-02-06 23:04:56")
        # 1. Creating a new table if it doesn't exist - run file after this to add table to database
        #cursor.execute("""CREATE TABLE IF NOT EXISTS
                        # Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
        # 3. Use INSERT command to insert data into the table after created
        cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()
'''

'''
EXECUTING MANY STATEMENTS
try:
    # Use default cursor as we aren't pulling data from the table
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:54"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
        connection.commit()
'''

'''
UPDATE, ALTERNATIVE UPDATE AND UPDATE MANY
try:
    with connection.cursor() as cursor:
        # UPDATE MANY
        rows = [(23, "Bob"),
                (24, "Jim"),
                (25, "Fred")]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        # UPDATE
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'BOB';")
        # ALTERNATIVE
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (23, 'Bob'))
        connection.commit()
'''

'''
DELETE, ALETERNATE DELETE AND DELETE MANY
'''
try:
    with connection.cursor() as cursor:
        
        # DELETE
        # cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        # ALTERNATIVE
        cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')
        connection.commit()

finally:
    # Close the connection to MySQL, regardless of whether code works
    connection.close()