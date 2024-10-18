"""
Module to create the hair table in the database.
This module creates the hair table in the database. The hair table stores the
hair types of the pet shop clients.
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class Hair(Base):
    """Hair class to store the hair types of pet shop clients.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "hairs"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
