#!/usr/bin/python3
import MySQLdb
from sys import argv as argv
""" Lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    connection = MySQLdb.connect(host, user, passwd, db, port)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
