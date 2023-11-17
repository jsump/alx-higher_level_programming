#!/usr/bin/python3
"""
Module: 0-select_states

This module lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


def list_states(username, password, database):
    """
    This function lists all the states in the database
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    cursor.close()
    db.close()

    for row in rows:
        print(row)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python script.py <username> <password> <database>")
