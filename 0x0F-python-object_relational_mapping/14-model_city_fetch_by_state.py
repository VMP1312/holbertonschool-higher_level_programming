#!/usr/bin/python3
"""
Changes the name of a State object from the database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    info = session.query(City, State).filter(City.state_id == State.id)
    for ci, st in info:
        print("{}: ({}) {}".format(st.name, ci.id, ci.name))

    session.close()
