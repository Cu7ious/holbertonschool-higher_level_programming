#!/usr/bin/python3
""" Takes in an argument and displays all values in the `states` table
    of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    from sys import argv as argv

    if len(argv) < 5:
        print("Error: this script requires 4 arguments")
        exit()

    import MySQLdb

    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    connection = MySQLdb.connect(host, user, passwd, db, port)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states"
                   + " WHERE name='{:s}'".format(name)
                   + "ORDER BY id")

    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
