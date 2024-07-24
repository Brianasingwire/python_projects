'''Main Entry Point function'''

import sys

from src.contact_book_operation import ContactBook


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
    print('')


def main() -> None:
    """
    Main Entry point function for the Contact Book project. This is
    a GUI based project for storing information about a person like name,
    contact number and email. The project includes functionalities like add,
    update, delete, view and reset contacts.
    """

    file_name = 'Contact.xlsx'
    contact_book = ContactBook(file_name)

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
            name = input('Enter a name: ')
            contacts = contact_book.view_contacts(name)

            if len(contacts) == 0:
                print('\nNo contacts found...')
            else:
                print('\nCONTACTS: ')
                for contact in contacts:
                    print(f"\t{contact}")

        elif command == '3':
            name = input('Enter a name: ')
            is_deleted = contact_book.delete_contact(name)
            if is_deleted:
                print(f'\nContact {name} successfully deleted...')
            else:
                print('\nNo contact was deleted...')

        elif command == '4':
            contact_book.clear_contact_book()
            print('\nContact Book cleared successfully...')

        elif command == '5':
            print('Terminated program successfully...')
            sys.exit(0)

        else:
            print('\nInvalid command. Please enter a number between 1 and 5.')


if __name__ == '__main__':
    main()
