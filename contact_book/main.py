'''Main Entry Point function'''

from src.contact_book_operation import ContactBook


def main() -> None:
    """
    Main Entry point function for the Contact Book project. This is
    a GUI based project for storing information about a person like name,
    contact number and email. The project includes functionalities like add,
    update, delete, view and reset contacts.
    """

    file_name = 'Contacts.xlsx'
    contact_book = ContactBook(file_name)

    while True:
        contact_book.contact_book_menu()

        command = input('Enter a number between 1 and 6: ')

        if command == '1':
            name = input('Enter a name: ').capitalize()
            number = input('Enter a number: ').strip()
            email = input('Enter email address: ').strip()
            contact_book.add_contacts(name, number, email)
            print(f"Contact {name} added successfully...")

        elif command == '2':
            name = input('Enter a name: ').capitalize()
            contact = contact_book.view_contact(name)
            if contact is not None:
                print(contact)
            else:
                print(f"Contact {name} not found...")

        elif command == '3':
            name = input('Enter a name: ').capitalize()
            contact_book.delete_contact(name)
            print(f'Contact {name} successfully deleted...')

        elif command == '4':
            contact_book.clear_contact_book()
            print('Contact Book cleared successfully...')

        elif command == '5':
            contact_book.display_contacts()

        elif command == '6':
            contact_book.save_contacts()
            print('Contacts saved successfully...')
            break

        else:
            print('Invalid command. Enter a number between 1 and 6.')


if __name__ == '__main__':
    main()
