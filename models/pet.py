"""
Pet class to store the pets of the pet shop.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
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
    name = Column(String, nullable=False)
    # category_id = Column(Integer, ForeignKey("categories.id"))
    # size_id = Column(Integer, ForeignKey("sizes.id"))
    # hair_id = Column(Integer, ForeignKey("hairs.id"))
    category_id = Column(Integer, ForeignKey(Category.id))
    size_id = Column(Integer, ForeignKey(Size.id))
    hair_id = Column(Integer, ForeignKey(Hair.id))
    special_needs = Column(String, nullable=True)
    human_id = Column(Integer, ForeignKey("humans.id"))
    # human_id = Column(Integer, ForeignKey(Human.id))
    # human = relationship("Human", back_populates="pets")
    # category = relationship("Category")
    # size = relationship("Size")
    # hair = relationship("Hair")
    # human = relationship(Human, back_populates="pets")
    category = relationship(Category)
    size = relationship(Size)
    hair = relationship(Hair)
    human = relationship(Human)

    # TODO: implement logic to return the human, category, size and hair name
    # instead of the ids
