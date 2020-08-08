#!/usr/bin/python3
"""
Use a safe filter.
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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM states,
                cities WHERE cities.state_id = states.id and states.name = %s\
                ORDER BY cities.id""", (my_filter,))
    info = cursor.fetchall()
    print(", ".join(mv[1] for mv in info))
    cursor.close()
    dtbs.close()
