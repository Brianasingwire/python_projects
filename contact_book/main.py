'''Main entry point function'''

from src.contact_book_operations import (add_contact,
                                         view_all_contacts, view_contact,
                                         update_contact, delete_contact,
                                         clear_contact_book, menu,
                                         terminate_program)

from src.csv_operations import load_contacts


def main():
    """
    Main Entry point function for the Contact Book project. This is
    a GUI based project for storing information about a person like name
    and contact number. The project includes functionalities like add, update,
    delete, view and reset contactc.
    """

    contacts = load_contacts()

    while True:
        menu()

        choice = input('Enter command: ')

        if not choice.isdigit():
            print('Invalid input. Please enter a number between 0 and 6.')

        choice = int(choice)

        if choice == 0:
            view_contact(contacts)

        elif choice == 1:
            contacts = add_contact(contacts)

        elif choice == 2:
            contacts = update_contact(contacts)

        elif choice == 3:
            contacts = delete_contact(contacts)

        elif choice == 4:
            view_all_contacts(contacts)

        elif choice == 5:
            contacts = clear_contact_book(contacts)

        elif choice == 6:
            terminate_program()
            break

        else:
            print('Invalid choice. Please enter a number between 0 and 6.')


if __name__ == '__main__':
    main()


# Classes
