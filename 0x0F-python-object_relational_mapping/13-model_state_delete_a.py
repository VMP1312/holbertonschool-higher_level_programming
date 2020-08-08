#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database
"""

from sys import argv
from model_state import Base, State
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
    s = Session()

    for mv in s.query(State).filter(State.name.like('%a%')).order_by(State.id):
        s.delete(mv)

    s.commit()
    s.close()
