#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
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

    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}'
            )

        Session = sessionmaker(bind=engine)
        session = Session()

        california = State(name='California')
        san_francisco = City(name='San Francisco', state_id=california.id)

        session.add(california)
        session.add(san_francisco)
        session.commit()

    except Exception as e:
        print(e)

    finally:
        session.close()
