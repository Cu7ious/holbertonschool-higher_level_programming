#!/usr/bin/python3
""" Takes the name of a state as an argument and lists all cities of the state
    using the database hbtn_0e_4_usa
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
    state = (argv[4],)

    connection = MySQLdb.connect(host, user, passwd, db, port)
    cursor = connection.cursor()

    cursor.execute(("SELECT cities.name FROM cities "
                    "INNER JOIN states ON cities.state_id = states.id "
                    "WHERE states.name=%s "
                    "ORDER BY cities.id"), state)

    rows = cursor.fetchall()
    connection.close()

    print(", ".join(item[0] for item in rows))
