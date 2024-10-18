"""
Size model to store the sizes of the pets of the pet shop.
This module creates the size table in the database. The size table stores the
sizes of the pets of the pet shop.
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class Size(Base):
    """
    Size class to store the sizes of the pets of the pet shop.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
