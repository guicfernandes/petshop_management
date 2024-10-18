"""
This module is responsible for creating the database schema and setting up the database.
It creates the following tables:
- categories: stores the categories of the clients (e.g. normal, vip, regular)
- sizes: stores the sizes of the pets (e.g. small, medium, large)
- hairs: stores the hair types of the pets (e.g. short, medium, long)
- services: stores the services that can be provided to the pets (e.g. bath, haircut, nail trimming)
- prices: stores the prices of the services for each category, size, and hair type
- humans: stores the information of the humans that own the pets
- pets: stores the information of the pets
- agenda: stores the appointments made for the pets

The tables are related as follows:
- The prices table has foreign keys to the categories, sizes, hairs, and services tables
- The pets table has foreign keys to the categories, sizes, hairs, and humans tables
- The agenda table has foreign keys to the pets and services tables
- The pets and humans tables have a one-to-many relationship

The setup_database function creates the database schema and returns the engine object.
If the module is run as the main program, it calls the setup_database function to create the database.

The module uses the SQLAlchemy library to interact with the database.
"""

from sqlalchemy import create_engine
from models import Base


def setup_database(database_name: str = "petshop.db") -> create_engine:
    """Create the database schema and return the engine object.

    Args:
        database_name (str): The name of the database file. Defaults to "petshop.db".

    Returns:
        create_engine: The engine object to interact with the database.
    """
    engine = create_engine(f"sqlite:///{database_name}")
    Base.metadata.create_all(engine)
    return engine


if __name__ == "__main__":
    # It should be executed only if the database doesn't exist yet
    setup_database()
