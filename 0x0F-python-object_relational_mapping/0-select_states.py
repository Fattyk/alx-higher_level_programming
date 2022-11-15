#!/usr/bin/python3
"""This module illustrates how to get the list of items from database"""

import sys
import MySQLdb


def print_states(user, password, name):
    """Print the list of states in database provided"""
    try:
        host = "localhost"
        port = 3306
        db = MySQLdb.connect(
            host=host, port=port, user=user,
            passwd=password, db=name
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        states = cur.fetchall()
    except Exception as e:
        print("Error: ", str(e))
        return

    for state in states:
        print(state)


def main():
    """Entry point for the whole program"""
    args = sys.argv[1:]
    if len(args) != 3:
        print("username, password and dbname is required")
        return

    print_states(args[0], args[1], args[2])


if __name__ == "__main__":
    main()
