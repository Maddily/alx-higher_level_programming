#!/usr/bin/python3
"""
This script lists all cities of a given state.
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

    query = """
            SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """

    cursor.execute(query, (state,))

    result = cursor.fetchone()[0]

    if result:
        print(result)
    else:
        print()

    cursor.close()
    db.close()
