#!/usr/bin/python3
"""
This module contains a class State that links to states table.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


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
        Integer, nullable=False, autoincrement=True, primary_key=True
        )
    name = Column(String(128), nullable=False)

    cities = relationship(
        'City',
        cascade='all, delete-orphan',
        back_populates='state'
        )
