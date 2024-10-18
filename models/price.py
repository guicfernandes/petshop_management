"""
Price model to store the prices of the services of the pet shop.
This module creates the price table in the database. The price table stores the
prices of the services of the pet shop.
"""

from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from .service import Service
from .category import Category
from .size import Size
from .hair import Hair

from .base import Base


class Price(Base):
    """Price class to store the prices of the services of the pet shop.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "prices"
    id = Column(Integer, primary_key=True)
    # service_id = Column(Integer, ForeignKey("services.id"))
    # category_id = Column(Integer, ForeignKey("categories.id"))
    # size_id = Column(Integer, ForeignKey("sizes.id"))
    # hair_id = Column(Integer, ForeignKey("hairs.id"))
    service_id = Column(Integer, ForeignKey(Service.id))
    category_id = Column(Integer, ForeignKey(Category.id))
    size_id = Column(Integer, ForeignKey(Size.id))
    hair_id = Column(Integer, ForeignKey(Hair.id))
    price_value = Column(Float, nullable=False)
    # service = relationship("Service")
    # category = relationship("Category")
    # size = relationship("Size")
    # hair = relationship("Hair")
    service = relationship(Service)
    category = relationship(Category)
    size = relationship(Size)
    hair = relationship(Hair)
