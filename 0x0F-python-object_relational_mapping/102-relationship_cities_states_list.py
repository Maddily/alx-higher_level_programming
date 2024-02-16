#!/usr/bin/python3
"""
This script lists all City objects in a database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(State.id, City.id).all()

    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')

    session.close()
