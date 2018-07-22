#!/usr/bin/python3
""" Changes the name of a State object from the database hbtn_0e_6_usa
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

    name = {'name': 'New Mexico'}
    states = session.query(State) \
        .filter(State.id == 2) \
        .update(name, synchronize_session=False)

    session.commit()
    session.close()
