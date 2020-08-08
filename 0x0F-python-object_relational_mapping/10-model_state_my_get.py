#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    names = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    info = session.query(State).filter_by(name=names).first()

    if info:
        print(info.id)
    else:
        print("Not found")
    session.close()
