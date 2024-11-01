"""
Pet class to store the pets of the pet shop.
"""

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .category import Category
from .size import Size
from .hair import Hair
from .human import Human


class Pet(Base):
    """Pet class to store the pets of the pet shop.

    Args:
        Base (_type_): Base class from sqlalchemy.ext.declarative.
    """

    __tablename__ = "pets"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=True)
    size_id = Column(Integer, ForeignKey(Size.id), nullable=True)
    hair_id = Column(Integer, ForeignKey(Hair.id), nullable=True)
    special_needs = Column(Boolean, nullable=True)
    human_id = Column(Integer, ForeignKey(Human.id), nullable=True)
    category = relationship(Category)
    size = relationship(Size)
    hair = relationship(Hair)
    human = relationship(Human)
