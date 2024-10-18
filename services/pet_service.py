from sqlalchemy.orm import sessionmaker
from utils.database_setup import setup_database
from models import Pet  # Import Pet directly from models

engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()


def add_pet(name, category_id, size_id, hair_id, special_needs):
    """Add a new pet to the database.

    Args:
        name (str): Pet name
        category_id (int): Category ID
        size_id (int): Size ID
        hair_id (int): Hair ID
        special_needs (str): Special needs description
        human_id (int): Human ID
    """
    pet = Pet(
        name=name,
        category_id=category_id,
        size_id=size_id,
        hair_id=hair_id,
        special_needs=special_needs,
    )
    session.add(pet)
    session.commit()


def get_pets() -> list:
    """Get all pets from the database."""
    return session.query(Pet).all()


def get_pet_by_id(pet_id: int) -> Pet:
    """Get a pet by ID.

    Args:
        pet_id (int): The ID of the pet.

    Returns:
        Pet: The pet object.
    """
    return session.query(Pet).filter_by(id=pet_id).first()


def update_pet(
    pet_id: int,
    name: str = None,
    category_id: int = None,
    size_id: int = None,
    hair_id: int = None,
    special_needs: str = None,
):
    """Update a pet's information.

    Args:
        pet_id (int): The ID of the pet.
        name (str, optional): The new name. Defaults to None.
        category_id (int, optional): The new category ID. Defaults to None.
        size_id (int, optional): The new size ID. Defaults to None.
        hair_id (int, optional): The new hair ID. Defaults to None.
        special_needs (str, optional): The new special needs description. Defaults to None.
    """
    pet = get_pet_by_id(pet_id)
    if pet:
        if name:
            pet.name = name
        if category_id:
            pet.category_id = category_id
        if size_id:
            pet.size_id = size_id
        if hair_id:
            pet.hair_id = hair_id
        if special_needs:
            pet.special_needs = special_needs
        session.commit()


def delete_pet(pet_id: int):
    """Delete a pet from the database.

    Args:
        pet_id (int): The ID of the pet.
    """
    pet = get_pet_by_id(pet_id)
    if pet:
        session.delete(pet)
        session.commit()
