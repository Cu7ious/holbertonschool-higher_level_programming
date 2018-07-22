#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        if row[1][0] == "N":
            print(row)
