#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    from sys import argv

    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).join(City).order_by(State.id, City.id)

    # print(query.all())
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
