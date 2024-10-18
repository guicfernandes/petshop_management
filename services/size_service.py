from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Size  # Import Size directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_size(name: str, description: str):
    """Add a new size to the database.

    Args:
        name (str): Size name
        description (str): Size description
    """
    size = Size(name=name, description=description)
    session.add(size)
    session.commit()


def get_sizes() -> list:
    """Get all sizes from the database."""
    return session.query(Size).all()


def get_size_by_id(size_id: int) -> Size:
    """Get a size by ID.

    Args:
        size_id (int): The ID of the size.

    Returns:
        Size: The size object.
    """
    return session.query(Size).filter_by(id=size_id).first()


def update_size(size_id: int, name: str = None, description: str = None):
    """Update a size's information.

    Args:
        size_id (int): The ID of the size.
        name (str, optional): The new name. Defaults to None.
        description (str, optional): The new description. Defaults to None.
    """
    size = get_size_by_id(size_id)
    if size and (name or description):
        size.name = name if name else size.name
        size.description = description if description else size.description
        session.commit()


def delete_size(size_id: int):
    """Delete a size from the database.

    Args:
        size_id (int): The ID of the size.
    """
    size = get_size_by_id(size_id)
    if size:
        session.delete(size)
        session.commit()
