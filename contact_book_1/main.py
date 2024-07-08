'''Main Entry Point Function'''

from src.contact_book_operations import ContactBook


def main():
    """
    Main Entry point function for the Contact Book project. This is
    a GUI based project for storing information about a person like name
    and contact number. The project includes functionalities like add, update,
    delete, view and reset contacts.
    """

    file_name = 'Contacts.xlsx'
    contact_book = ContactBook(file_name)

    while True:
        contact_book.contact_menu()

        command = input('Enter a number between 1 and 5: ')

        if command == '1':
            name = input('Enter name: ').capitalize().strip()
            phone = input('Enter phone number: ').strip()
            email = input('Enter email: ').strip()
            contact_book.add_contact(name, phone, email)
            print(f"Contact {name} added successfully.")

        elif command == '2':
            name = input('Enter name: ').capitalize().strip()
            contact = contact_book.view_contact(name)
            if contact is not None:
                print(contact)
            else:
                print(f"Contact {name} not found.")

        elif command == '3':
            name = input('Enter name: ').capitalize().strip()
            contact_book.remove_contact(name)
            print(f"Contact {name} removed successfully.")

        elif command == '4':
            contact_book.display_contacts()

        elif command == '5':
            contact_book.save_contacts()
            print('Contacts saved successfully.')
            break

        else:
            print('Invalid command. Please try again.')


if __name__ == '__main__':
    main()
