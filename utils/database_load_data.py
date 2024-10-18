import sys
import os
import json

# Add the root directory of your project to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.category_service import add_category
from services.service_service import add_service
from services.hair_service import add_hair
from services.size_service import add_size
from services.price_service import add_price
from services.human_service import add_human
from services.pet_service import add_pet

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate up one level to the parent directory
parent_dir = os.path.dirname(current_dir)

# Construct the path to the JSON files
CATEGORIES_FILE = os.path.join(parent_dir, "assets", "categories.json")
HAIRS_FILE = os.path.join(parent_dir, "assets", "hairs.json")
SERVICES_FILE = os.path.join(parent_dir, "assets", "services.json")
SIZES_FILE = os.path.join(parent_dir, "assets", "sizes.json")
PRICES_FILE = os.path.join(parent_dir, "assets", "prices.json")
HUMANS_FILE = os.path.join(parent_dir, "assets", "humans.json")
PETS_FILE = os.path.join(parent_dir, "assets", "pets.json")


def load_categories_from_json():
    """Load categories from a JSON file and add them to the database."""
    print(f"Loading categories from JSON file: {CATEGORIES_FILE}")
    with open(CATEGORIES_FILE, "r", encoding="utf-8") as file:
        categories = json.load(file)
        for category in categories:
            name = category.get("name")
            description = category.get("description")
            add_category(name, description)


def load_services_from_json():
    """Load services from a JSON file and add them to the database."""
    print(f"Loading services from JSON file: {SERVICES_FILE}")
    with open(SERVICES_FILE, "r", encoding="utf-8") as file:
        services = json.load(file)
        for service in services:
            name = service.get("name")
            description = service.get("description")
            add_service(name, description)


def load_hair_from_json():
    """Load hair types from a JSON file and add them to the database."""
    print(f"Loading hair types from JSON file: {HAIRS_FILE}")
    with open(HAIRS_FILE, "r", encoding="utf-8") as file:
        hairs = json.load(file)
        for hair in hairs:
            name = hair.get("name")
            description = hair.get("description")
            add_hair(name, description)


def load_sizes_from_json():
    """Load sizes from a JSON file and add them to the database."""
    print(f"Loading sizes from JSON file: {SIZES_FILE}")
    with open(SIZES_FILE, "r", encoding="utf-8") as file:
        sizes = json.load(file)
        for size in sizes:
            name = size.get("name")
            description = size.get("description")
            add_size(name, description)


def choose_tables_to_be_populated() -> dict:
    """
    Choose the tables to be populated with data.
    Example:
    To populate specific tables, add the table name and the respective function to the dictionary.
    {
        "categories": load_categories_from_json,
        "hair": load_hair_from_json,
        "services": load_services_from_json,
        "sizes": load_sizes_from_json,
        "prices": load_prices_from_json,
        "humans": load_humans_from_json,
        "pets": load_pets_from_json,
        "agenda": load_agenda_from_json,
    }
    To populate all tables, return the dictionary with all tables and their respective functions

    Returns:
        dict: A dictionary with the tables to be populated and their respective functions.
    """
    return {
        "hair": load_hair_from_json,
        "services": load_services_from_json,
        "sizes": load_sizes_from_json,
    }


if __name__ == "__main__":
    tables_to_be_populates = choose_tables_to_be_populated()
    for table, function in tables_to_be_populates.items():
        function()
        print(f"{table.capitalize()} populated successfully.")
