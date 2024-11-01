import csv
from utils import database_setup, database_load_data


def delete_database_tables():
    """Delete all tables from the database."""
    table_list = ["pets"]
    for table in table_list:
        database_setup.delete_table(table)


def populate_database():
    """Populate the database with data from CSV and JSON files."""
    tables_to_be_populates = database_load_data.choose_tables_to_be_populated()
    for table, function in tables_to_be_populates.items():
        function()
        print(f"{table.capitalize()} populated successfully.")


def list_pets():
    """List all pets from the database."""
    from services.pet_service import get_pets

    pets = get_pets()
    for pet in pets:
        print(
            f"ID: {pet.id}, Name: {pet.name}, Category: {pet.category.name}, Size: {pet.size.name}, Hair: {pet.hair.name}, Special Needs: {pet.special_needs}, Human: {pet.human.name}"
        )


def write_list_of_pets_csv():
    """Write all pets to a CSV file."""
    from services.pet_service import get_pets

    pets = get_pets()
    file_path = "assets/result_pets.csv"
    with open(file_path, mode="w", newline="", encoding="latin1") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["ID", "Name", "Category", "Size", "Hair", "Special Needs", "Human"]
        )
        for pet in pets:
            writer.writerow(
                [
                    pet.id,
                    pet.name,
                    pet.category.name if pet.category else None,
                    pet.size.name if pet.size else None,
                    pet.hair.name if pet.hair else None,
                    pet.special_needs,
                    pet.human.name if pet.human else None,
                ]
            )
    print(f"Pets data has been written to {file_path}")


if "__main__" == __name__:
    # delete_database_tables()
    # populate_database()
    # write_list_of_pets_csv()
    list_pets()
