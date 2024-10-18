from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Category  # Import Category directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_category(name: str, description: str):
    """Add a new category to the database.

    Args:
        name (str): Category name
        description (str): Category description
    """
    category = Category(name=name, description=description)
    session.add(category)
    session.commit()


def get_categories() -> list:
    """Get all categories from the database."""
    return session.query(Category).all()


def get_category_by_id(category_id: int) -> Category:
    """Get a category by ID.

    Args:
        category_id (int): The ID of the category.

    Returns:
        Category: The category object.
    """
    return session.query(Category).filter_by(id=category_id).first()


def update_category(category_id: int, name: str = None, description: str = None):
    """Update a category's information.

    Args:
        category_id (int): The ID of the category.
        name (str, optional): The new name. Defaults to None
        description (str, optional): The new description. Defaults to None.
    """
    category = get_category_by_id(category_id)
    if category and (name or description):
        category.name = name if name else category.name
        category.description = description if description else category.description
        session.commit()


def delete_category(category_id: int):
    """Delete a category from the database.

    Args:
        category_id (int): The ID of the category.
    """
    category = get_category_by_id(category_id)
    if category:
        session.delete(category)
        session.commit()
