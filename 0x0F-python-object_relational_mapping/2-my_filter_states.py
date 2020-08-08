#!/usr/bin/python3
"""
Use a specified filter.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    my_filter = argv[4]

    credentials = {
        'host': "localhost",
        'port': 3306,
        'user': user,
        'passwd': passwd,
        'db': database
    }

    dtbs = MySQLdb.connect(**credentials)
    cursor = dtbs.cursor()
    cursor.execute("""SELECT * FROM states WHERE
                   name LIKE BINARY '{}' ORDER BY id""".format(my_filter))
    row = cursor.fetchall()
    for mv in row:
        print(mv)
    cursor.close()
    dtbs.close()
