#!/usr/bin/python3
"""Using sub queries.

This module illustrates how to get the list of cities from given states
"""

import re
import sys
import MySQLdb


def print_states(user, password, name, search):
    """Print the list of cities in a given states in database"""
    try:
        host = "localhost"
        port = 3306
        db = MySQLdb.connect(
            host=host, port=port, user=user,
            passwd=password, db=name
        )
        cur = db.cursor()
        cur.execute(
            "SELECT cities.name FROM cities INNER JOIN states ON\
            state_id=states.id\
            WHERE states.name='{}' ORDER BY cities.id ASC".format(
               search
            )
        )
        states = cur.fetchall()
    except Exception as e:
        print("Error: ", str(e))
        return

    for state in states:
        print(state[0], end=", ") if state != states[-1] else print(state[0])


def main():
    """Entry point for the whole program"""
    args = sys.argv[1:]
    if len(args) != 4:
        print("username, password, dbname and search are required")
        return
    if re.search("[;'\"]", args[3]):
        print("Invalid pattern")
        return

    print_states(args[0], args[1], args[2], args[3])


if __name__ == "__main__":
    main()
