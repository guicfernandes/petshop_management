from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Hair  # Import Hair directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_hair(name: str, description: str):
    """Add a new hair type to the database.

    Args:
        name (str): Hair type name
        description (str): Hair type description
    """
    hair = Hair(name=name, description=description)
    session.add(hair)
    session.commit()


def get_hairs() -> list:
    """Get all hair types from the database."""
    return session.query(Hair).all()


def get_hair_by_id(hair_id: int) -> Hair:
    """Get a hair type by ID.

    Args:
        hair_id (int): The ID of the hair type.

    Returns:
        Hair: The hair type object.
    """
    return session.query(Hair).filter_by(id=hair_id).first()


def update_hair(hair_id: int, name: str = None, description: str = None):
    """Update a hair type's information.

    Args:
        hair_id (int): The ID of the hair type.
        name (str, optional): The new name. Defaults to None
        description (str, optional): The new description. Defaults to None.
    """
    hair = get_hair_by_id(hair_id)
    if hair and (name or description):
        hair.name = name if name else hair.name
        hair.description = description if description else hair.description
        session.commit()


def delete_hair(hair_id: int):
    """Delete a hair type from the database.

    Args:
        hair_id (int): The ID of the hair type.
    """
    hair = get_hair_by_id(hair_id)
    if hair:
        session.delete(hair)
        session.commit()
