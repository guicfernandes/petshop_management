"""
Category model to store the categories of pet shop clients.
This module creates the category table in the database. The category table stores the
categories of the pet shop clients.
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class Category(Base):
    """Category class to store the categories of pet shop clients.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
