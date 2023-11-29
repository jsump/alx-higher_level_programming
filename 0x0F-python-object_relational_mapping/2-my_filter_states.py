#!/usr/bin/python3
"""
Module: 2-my_filter_states

This module contains a function that takes in an argument
and displays all the values in the states table of hbtn_0e_0_usa
where name matches the argument
"""


import sys
import MySQLdb


def display_name_matching_argument(username, password, database, state_name):
    """
    This function taked an argument and displays all the values
    in the states table of hbtn_0e_0_usa where name matches argument
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    display_name_matching_argument(username, password, database, state_name)
