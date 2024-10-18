"""
Service model to store the services of the pet shop.
This module creates the service table in the database. The service table stores the
services of the pet shop.
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class Service(Base):
    """Service class to store the services of the pet shop.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
