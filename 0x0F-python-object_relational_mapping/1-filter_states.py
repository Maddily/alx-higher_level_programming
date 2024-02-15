#!/usr/bin/python3
"""
This script lists all states with a name starting with N.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute(
        "SELECT DISTINCT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
        )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
