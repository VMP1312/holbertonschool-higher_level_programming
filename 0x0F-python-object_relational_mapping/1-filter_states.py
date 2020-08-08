#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

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
                   name LIKE BINARY 'N%' ORDER BY id""")
    row = cursor.fetchall()
    for mv in row:
        print(mv)
    cursor.close()
    dtbs.close()
