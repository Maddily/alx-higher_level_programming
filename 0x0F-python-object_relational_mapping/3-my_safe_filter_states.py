#!/usr/bin/python3
"""
Builds off 2-my_filter_states by making it safe from MySQL injections.
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

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"

    cursor.execute(query, (state,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
