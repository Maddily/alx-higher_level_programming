#!/usr/bin/python3
"""
This module contains a class State that links to states table.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

Base = declarative_base()


class State(Base):
    """
    Class Attributes:
    - id (int): A column of auto-generated, unique integer
    that can't be null and is a primary key.
    - name (str): A column of a string with maximum
    128 characters and can't be null.
    """

    __tablename__ = 'states'

    id = Column(
        'id', Integer, nullable=False, autoincrement=True, primary_key=True
        )
    name = Column('name', String(128), nullable=False)

    def __init__(self, name):
        """Instantiates a state"""

        self.name = name
