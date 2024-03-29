#!/usr/bin/python3
"""
This script lists all states with a specific name.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute(
        """SELECT * FROM states WHERE name LIKE BINARY '{}'
        ORDER BY states.id""".format(state))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
