#!/usr/bin/python3
""" Lists all State objects that contain the letter 'a'
    from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv

    if len(argv) < 5:
        print("Error: this script requires 4 arguments")
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

    name = argv[4]
    states = session.query(State) \
        .filter(State.name.like(name)) \
        .all()

    if states == []:
        print("Not found")
    else:
        for indiv in states:
            print("{}".format(indiv.id))

    session.close()
