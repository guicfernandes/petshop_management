"""
This is the main file that will be run to interact with the application.
It provides a menu to add, view, update, and delete humans from the database.

The main function displays a menu with the following options:
1. Add Human: Allows the user to add a new human to the database.
2. View Humans: Displays a list of all humans in the database.
3. Update Human: Allows the user to update the information of an existing human.
"""

from services.human_service import add_human, get_humans, update_human, delete_human
from services.pet_service import add_pet


def main():
    """
    Main function to interact with the application.
    It displays a menu with options to add, view, update, and delete humans from the database.

    The function runs in a loop until the user chooses to exit the application.
    """
    while True:
        print("1. Add Human")
        print("2. View Humans")
        print("3. Update Human")
        print("4. Delete Human")
        print("5. Add Pet")
        print("6. Exit")
        choice = input("Enter choice (press 6 to stop the app): ")

        if choice == "1":
            name = input("Enter name: ")
            telephone = input("Enter telephone: ")
            email = input("Enter email: ")
            add_human(name, telephone, email)
        elif choice == "2":
            humans = get_humans()
            for human in humans:
                print(
                    f"ID: {human.id}, Name: {human.name}, Telephone: {human.telephone}, Email: {human.email}"
                )
        elif choice == "3":
            human_id = int(input("Enter human ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            telephone = input("Enter new telephone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            update_human(human_id, name, telephone, email)
        elif choice == "4":
            human_id = int(input("Enter human ID to delete: "))
            delete_human(human_id)
        elif choice == "5":
            name = input("Enter name: ")
            category_id = int(input("Enter category ID: "))
            size_id = int(input("Enter size ID: "))
            hair_id = int(input("Enter hair ID: "))
            special_needs = input("Enter special needs: ")
            add_pet(name, category_id, size_id, hair_id, special_needs)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
