import csv
import os
import json
import sys

# Add the root directory of your project to the PYTHONPATH
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# print(sys.path)

from utils.commons import format_phone_number

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
HUMANS_FILE = os.path.join(parent_dir, "assets", "humans.csv")
PETS_FILE = os.path.join(parent_dir, "assets", "pets.csv")


def load_categories_from_json():
    """Load categories from a JSON file and add them to the database."""
    from services.category_service import add_category

    print(f"Loading categories from JSON file: {CATEGORIES_FILE}")
    with open(CATEGORIES_FILE, mode="r", encoding="utf-8") as file:
        categories = json.load(file)
        for category in categories:
            name = category.get("name")
            description = category.get("description")
            add_category(name, description)


def load_services_from_json():
    """Load services from a JSON file and add them to the database."""
    from services.service_service import add_service

    print(f"Loading services from JSON file: {SERVICES_FILE}")
    with open(SERVICES_FILE, mode="r", encoding="utf-8") as file:
        services = json.load(file)
        for service in services:
            name = service.get("name")
            description = service.get("description")
            add_service(name, description)


def load_hair_from_json():
    """Load hair types from a JSON file and add them to the database."""
    from services.hair_service import add_hair

    print(f"Loading hair types from JSON file: {HAIRS_FILE}")
    with open(HAIRS_FILE, mode="r", encoding="utf-8") as file:
        hairs = json.load(file)
        for hair in hairs:
            name = hair.get("name")
            description = hair.get("description")
            add_hair(name, description)


def load_sizes_from_json():
    """Load sizes from a JSON file and add them to the database."""
    from services.size_service import add_size

    print(f"Loading sizes from JSON file: {SIZES_FILE}")
    with open(SIZES_FILE, mode="r", encoding="utf-8") as file:
        sizes = json.load(file)
        for size in sizes:
            name = size.get("name")
            description = size.get("description")
            add_size(name, description)


def load_humans_from_csv():
    """Load humans from a CSV file and add them to the database."""
    from services.human_service import add_human

    print(f"Loading humans from CSV file: {HUMANS_FILE}")
    with open(HUMANS_FILE, mode="r", encoding="latin1") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            name = row.get("name")
            phone = format_phone_number(row.get("phone").strip())
            email = row.get("email") if row.get("email") else None
            add_human(name, phone, email)
            # print(f"Name: {name}, phone: {phone}, Email: {email}\n")


def load_pets_from_csv():
    """Load pets from a CSV file and add them to the database."""
    from services.pet_service import add_pet

    print(f"Loading pets from CSV file: {PETS_FILE}")
    with open(PETS_FILE, mode="r", encoding="latin1") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            name = row.get("name")
            category_id = row.get("category_id")
            hair_id = row.get("hair_id")
            size_id = row.get("size_id")
            human_id = row.get("human_id")
            special_needs = True if row.get("special_needs") == "0" else False
            add_pet(
                name=name,
                category_id=category_id,
                size_id=size_id,
                hair_id=hair_id,
                human_id=human_id,
                special_needs=special_needs,
            )
            # add_pet(name, species, breed, birthdate, hair_id, size_id, human_id)
            print(
                f"Name: {name}, Category ID: {category_id}, Hair ID: {hair_id}, Size ID: {size_id}, Human ID: {human_id}, Special Needs: {special_needs}\n"
            )


def load_prices_from_json():
    """Load prices from a JSON file and add them to the database."""
    from services.price_service import add_price

    print(f"Loading prices from JSON file: {PRICES_FILE}")
    with open(PRICES_FILE, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            service_id = row["service_id"]
            size_id = row["size_id"]
            price = row["price"]
            # add_price(service_id, size_id, price)
            print(f"Service ID: {service_id}, Size ID: {size_id}, Price: {price}\n")


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
        "pets": load_pets_from_csv,
    }


if __name__ == "__main__":
    tables_to_be_populates = choose_tables_to_be_populated()
    for table, function in tables_to_be_populates.items():
        function()
        print(f"{table.capitalize()} populated successfully.")
