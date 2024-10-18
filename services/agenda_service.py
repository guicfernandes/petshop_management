from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Agenda  # Import Agenda directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_agenda(date, pet_id, service_id):
    """Add a new agenda entry to the database.

    Args:
        date (datetime.date): The date of the appointment
        pet_id (int): The ID of the pet
        service_id (int): The ID of the service
    """
    agenda = Agenda(date=date, pet_id=pet_id, service_id=service_id)
    session.add(agenda)
    session.commit()


def get_agendas() -> list:
    """Get all agenda entries from the database."""
    return session.query(Agenda).all()


def get_agenda_by_id(agenda_id: int) -> Agenda:
    """Get an agenda entry by ID.

    Args:
        agenda_id (int): The ID of the agenda entry.

    Returns:
        Agenda: The agenda entry object.
    """
    return session.query(Agenda).filter_by(id=agenda_id).first()


def update_agenda(agenda_id: int, date=None, pet_id=None, service_id=None):
    """Update an agenda entry's information.

    Args:
        agenda_id (int): The ID of the agenda entry.
        date (datetime.date, optional): The new date. Defaults to None.
        pet_id (int, optional): The new pet ID. Defaults to None.
        service_id (int, optional): The new service ID. Defaults to None.
    """
    agenda = get_agenda_by_id(agenda_id)
    if agenda:
        if date:
            agenda.date = date
        if pet_id:
            agenda.pet_id = pet_id
        if service_id:
            agenda.service_id = service_id
        session.commit()


def delete_agenda(agenda_id: int):
    """Delete an agenda entry from the database.

    Args:
        agenda_id (int): The ID of the agenda entry.
    """
    agenda = get_agenda_by_id(agenda_id)
    if agenda:
        session.delete(agenda)
        session.commit()
