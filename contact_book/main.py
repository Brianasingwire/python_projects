'''Main Entry Point function'''

import sys

from src.contact_book_operation import (
    DataBaseService, ExcelDatabaseService, CSVDatabaseService, ContactBook)


def contact_book_menu():
    """
    Displays Contact Book menu.
    """
    print('')
    print('Enter 1 to add contact.')
    print('Enter 2 to view a contact(s).')
    print('Enter 3 to delete a contact.')
    print('Enter 4 to clear contact book.')
    print('Enter 5 to exit.')
    print("Enter 'csv' or 'excel' to switch storage.")
    print('')


def get_service_provider(service_provider_type: str) -> DataBaseService:
    """
    Gets a databse service provider.

    Args:
        service_provider_type (str): Name of database service.

    Returns:
        DataBaseService: Database service abstract class.
    """
    try:
        if service_provider_type == 'csv':
            database_service = CSVDatabaseService('Contact.csv')
        elif service_provider_type == 'excel':
            database_service = ExcelDatabaseService('Contact.xlsx')
    except SyntaxError as e:
        print(e)
        sys.exit(0)

    return database_service


def main() -> None:
    """
    Main Entry point function for the Contact Book project. This is
    a GUI based project for storing information about a person like name,
    contact number and email. The project includes functionalities like a5dd,
    update, delete, view and reset contacts.
    """
    database_service = get_service_provider('csv')
    contact_book = ContactBook(database_service)

    while True:
        contact_book_menu()

        command = input('Enter a number between 1 and 5: ')

        if command == '1':
            name = input('Enter a name: ')
            phone_number = input('Enter a number: ').strip()
            email = input('Enter email address: ').strip()
            contact_book.add_contacts(name, phone_number, email)
            print(f"\nContact {name} added successfully...")

        elif command == '2':
            name = input('Enter a contact name(s) to view: ')
            contacts = contact_book.view_contacts(name)

            for contact in contacts:
                print(f"\t{contact}")

        elif command == '3':
            name = input('Enter a contact name to be deleted: ')
            contact_book.delete_contact(name)
            print(f"Contact {name} successfully deleted.")

        elif command == '4':
            contact_book.clear_contact_book()
            print('\nContact Book cleared successfully...')

        elif command == '5':
            print('Terminated program successfully...')
            sys.exit(0)

        elif command in ('csv', 'excel'):
            database_service = get_service_provider(command)
            contact_book.change_service_provider(database_service)
            print(f"Swithed to '{command}'")

        else:
            print('\nInvalid command. Please enter a number between 1 and 5.')


if __name__ == '__main__':
    main()
