#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
        )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .order_by(State.id)
        )

    for state in states:
        print(f'{state.id}: {state.name}')

        cities = sorted(state.cities, key=lambda city: city.id)

        for city in cities:
            print(f'    {city.id}: {city.name}')

    session.close()