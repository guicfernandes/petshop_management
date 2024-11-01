"""
This module contains the services for the Human model.
The services include adding, getting, updating, and deleting humans.

The services are:
    add_human(name, phone, email)
    get_humans()
    get_human_by_id(human_id)
    update_human(human_id, name=None, phone=None, email=None)
    delete_human(human_id)
"""

from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Human


engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_human(name: str, phone: str, email: str):
    """Add a human to the database.

    Args:
        name (str): client name
        phone (str): client phone
        email (str): client email
    """
    human = Human(name=name, phone=phone, email=email)
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


def update_human(human_id: int, name: str = None, phone: str = None, email: str = None):
    """Update a client in the database.

    Args:
        human_id (int): The ID of the client.
        name (str, optional): The client name. Defaults to None.
        phone (str, optional): The client phone. Defaults to None.
        email (str, optional): The client email. Defaults to None.
    """
    human = get_human_by_id(human_id)
    if human:
        if name:
            human.name = name
        if phone:
            human.phone = phone
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
