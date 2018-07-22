#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv as argv

    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    import MySQLdb

    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    connection = MySQLdb.connect(host, user, passwd, db, port)
    cursor = connection.cursor()

    cursor.execute(("SELECT cities.id, cities.name, states.name FROM cities "
                    "INNER JOIN states ON cities.state_id = states.id "
                    "ORDER BY cities.id"))

    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
