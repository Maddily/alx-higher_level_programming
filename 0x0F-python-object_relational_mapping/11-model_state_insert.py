#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to a database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name='Louisiana')

    session.add(louisiana)
    session.commit()

    print(louisiana.id)
