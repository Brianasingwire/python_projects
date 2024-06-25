'''Contact Book Project'''

from .csv_operations import save_contacts


def menu():
    """Function to printout Contact Book menu"""

    print('')
    print('==========MENU==========')
    print('Press 0 to view an existing contact.')
    print('Press 1 to add a contact.')
    print('Press 2 to update an existing contact.')
    print('Press 3 to delete a contact.')
    print('Press 4 to view all contacts.')
    print('Press 5 to clear contact book.')
    print('Press 6 to terminate program.')
    print('')


def view_contact(contacts):
    """Function to view a contact in the Contact Book"""

    name = input('Name of contact to view: ').upper()

    if name in contacts:
        print(f'Number of {name}: {contacts[name]}')

    else:
        print(f'Contact {name} not found.')


def add_contact(contacts):
    """Function to add a contact to the Contact Book"""

    name = input('Name of new contact: ').upper()
    number = input('Enter phone number (10 digit number): ')

    if not number.isdigit() or (len(number) < 10):
        print(f'The phone number {number} is invalid. Try again.')

    else:
        contacts[name] = int(number)
        save_contacts(contacts)
        print(f'Contact {name} added.')
    return contacts


def update_contact(contacts):
    """Function to update a contact in the Contact Book"""

    name = input('Name of contact to update: ').upper()

    if name in contacts:
        number = input('Enter a new phone number (10 digit number): ')
        if not number.isdigit() or (len(number) < 10):
            print(f'The phone number {number} is invalid. Try again.')

        else:
            contacts[name] = int(number)
            save_contacts(contacts)
            print(f'Contact {name} updated: {contacts[name]}')

    else:
        print(f'Contact {name} not found.')
    return contacts


def delete_contact(contacts):
    """Function to delete a contact from the Contact Book"""

    name = input('Name of contact to delete: ').upper()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f'Contact {name} deleted.')

    else:
        print(f'Contact {name} not found.')
    return contacts


def view_all_contacts(contacts):
    """Function to view all contacts in the Contact Book"""

    if contacts:
        for key, value in contacts.items():
            print(f'{key}: {value}')

    else:
        print('No contacts found.')


def clear_contact_book(contacts):
    """Function to clear all contacts from the Contact Book"""

    contacts.clear()
    save_contacts(contacts)
    print('Contact book cleared.')
    return {}


def terminate_program():
    """Function to terminate Contact Book program"""

    print('Terminating program.')
