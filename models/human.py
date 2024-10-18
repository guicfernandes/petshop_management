"""
Human model to store the humans of the pet shop.
This module creates the human table in the database. The human table stores the
humans of the pet shop.
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class Human(Base):
    """Human class to store the humans of the pet shop.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "humans"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    # pets = relationship("Pet", back_populates="human")
    # TODO: Define how to relate the human and pet tables, humans can have multiple pets
    # pets = relationship(Pet, back_populates="human")
