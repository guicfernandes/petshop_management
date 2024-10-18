from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Price  # Import Price directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_price(service_id, category_id, size_id, hair_id, price_value):
    """Add a new price to the database.

    Args:
        service_id (int): Service ID
        category_id (int): Category ID
        size_id (int): Size ID
        hair_id (int): Hair ID
        price_value (float): Price value
    """
    price = Price(
        service_id=service_id,
        category_id=category_id,
        size_id=size_id,
        hair_id=hair_id,
        price_value=price_value,
    )
    session.add(price)
    session.commit()


def get_prices() -> list:
    """Get all prices from the database."""
    return session.query(Price).all()


def get_price_by_id(price_id: int) -> Price:
    """Get a price by ID.

    Args:
        price_id (int): The ID of the price.

    Returns:
        Price: The price object.
    """
    return session.query(Price).filter_by(id=price_id).first()


def get_prices_by_service(service_id: int) -> list:
    """Get all prices for a specific
    service from the database.

    Args:
        service_id (int): The ID of the service.

    Returns:
        list: A list of price objects.
    """
    return session.query(Price).filter_by(service_id=service_id).all()


def update_price(
    price_id: int,
    service_id: int = None,
    category_id: int = None,
    size_id: int = None,
    hair_id: int = None,
    price_value: float = None,
):
    """Update a price's information.

    Args:
        price_id (int): The ID of the price.
        service_id (int, optional): The new service ID. Defaults to None.
        category_id (int, optional): The new category ID. Defaults to None.
        size_id (int, optional): The new size ID. Defaults to None.
        hair_id (int, optional): The new hair ID. Defaults to None.
        price_value (float, optional): The new price value. Defaults to None.
    """
    price = get_price_by_id(price_id)
    if price:
        if service_id:
            price.service_id = service_id
        if category_id:
            price.category_id = category_id
        if size_id:
            price.size_id = size_id
        if hair_id:
            price.hair_id = hair_id
        if price_value:
            price.price_value = price_value
        session.commit()


def delete_price(price_id: int):
    """Delete a price from the database.

    Args:
        price_id (int): The ID of the price.
    """
    price = get_price_by_id(price_id)
    if price:
        session.delete(price)
        session.commit()
