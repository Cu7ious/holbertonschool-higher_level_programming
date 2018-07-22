#!/usr/bin/python3
""" Lists all State objects that contain the letter 'a'
    from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv

    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State) \
        .filter(State.name.like("%a%")) \
        .order_by(State.id).all()

    if states is None:
        print("Nothing")
    else:
        for rows in states:
            if "a" in rows.name:
                print("{}: {}".format(rows.id, rows.name))

    session.close()
