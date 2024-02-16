#!/usr/bin/python3
"""
This module contains a class City that links to cities table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    Class Attributes:
    - id (int): A column of auto-generated, unique integer
    that can't be null and is a primary key.
    - name (str): A column of a string with maximum
    128 characters and can't be null.
    - state_id (int): A column representing a foreign key
    that references the id column of the states table.
    """

    __tablename__ = 'cities'

    id = Column(
        'id', Integer, nullable=False, autoincrement=True, primary_key=True
        )
    name = Column('name', String(128), nullable=False)
    state_id = Column(
        'state_id', Integer, ForeignKey('states.id'), nullable=False
        )

    state = relationship("State")

    def __init__(self, name, state_id):
        """Instantiates a city"""

        self.name = name
        self.state_id = state_id
