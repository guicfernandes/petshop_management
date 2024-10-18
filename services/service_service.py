from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Service  # Import Service directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_service(name: str, description: str):
    """Add a new service to the database.

    Args:
        name (str): Service name
        description (str): Service description
    """
    service = Service(name=name, description=description)
    session.add(service)
    session.commit()


def get_services() -> list:
    """Get all services from the database."""
    return session.query(Service).all()


def get_service_by_id(service_id: int) -> Service:
    """Get a service by ID.

    Args:
        service_id (int): The ID of the service.

    Returns:
        Service: The service object.
    """
    return session.query(Service).filter_by(id=service_id).first()


def update_service(service_id: int, name: str = None, description: str = None):
    """Update a service's information.

    Args:
        service_id (int): The ID of the service.
        name (str, optional): The new name. Defaults to None.
        description (str, optional): The new description. Defaults to None.
    """
    service = get_service_by_id(service_id)
    if service and (name or description):
        service.name = name if name else service.name
        service.description = description if description else service.description
        session.commit()


def delete_service(service_id: int):
    """Delete a service from the database.

    Args:
        service_id (int): The ID of the service.
    """
    service = get_service_by_id(service_id)
    if service:
        session.delete(service)
        session.commit()
