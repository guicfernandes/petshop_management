"""
This module contains the services for the Human model.
The services include adding, getting, updating, and deleting humans.

The services are:
    add_human(name, telephone, email)
    get_humans()
    get_human_by_id(human_id)
    update_human(human_id, name=None, telephone=None, email=None)
    delete_human(human_id)
"""

from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Human


engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_human(name: str, telephone: str, email: str):
    """Add a human to the database.

    Args:
        name (str): client name
        telephone (str): client telephone
        email (str): client email
    """
    human = Human(name=name, telephone=telephone, email=email)
    session.add(human)
    session.commit()


def get_humans() -> list:
    """Get all clients from the database.

    Returns:
        list: A list of all clients in the database.
    """
    return session.query(Human).all()


def get_human_by_id(human_id: int):
    """Get a client by ID from the database.

    Args:
        human_id (int): The ID of the client.

    Returns:
        Human: The client with the specified ID.
    """
    return session.query(Human).filter_by(id=human_id).first()


def update_human(
    human_id: int, name: str = None, telephone: str = None, email: str = None
):
    """Update a client in the database.

    Args:
        human_id (int): The ID of the client.
        name (str, optional): The client name. Defaults to None.
        telephone (str, optional): The client telephone. Defaults to None.
        email (str, optional): The client email. Defaults to None.
    """
    human = get_human_by_id(human_id)
    if human:
        if name:
            human.name = name
        if telephone:
            human.telephone = telephone
        if email:
            human.email = email
        session.commit()


def delete_human(human_id: int):
    """Delete a client from the database.

    Args:
        human_id (int): The ID of the client.
    """
    human = get_human_by_id(human_id)
    if human:
        session.delete(human)
        session.commit()
