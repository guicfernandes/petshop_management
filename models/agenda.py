"""
Module to define the Agenda class.

This module defines the Agenda class, which represents the appointments made 
for the pets in the pet shop.
"""

from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from .pet import Pet
from .service import Service

from .base import Base


class Agenda(Base):
    """Agenda class to store the appointments of the pet shop.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "agenda"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    # pet_id = Column(Integer, ForeignKey("pets.id"))
    # service_id = Column(Integer, ForeignKey("services.id"))
    pet_id = Column(Integer, ForeignKey(Pet.id))
    service_id = Column(Integer, ForeignKey(Service.id))
    # pet = relationship("Pet")
    # service = relationship("Service")
    pet = relationship(Pet)
    service = relationship(Service)

    # TODO: implement logic to return the pet name and the service name
