'''Contact Book Project'''

from openpyxl import load_workbook, Workbook


class ContactBook:
    """
    Contact Book class for storing contact information like name, phone number
    and email address of a person.
    """

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

        try:
            self.workbook = load_workbook(self.file_name)
            self.sheet = self.workbook.active
        except FileNotFoundError:
            self.workbook = Workbook()
            self.sheet = self.workbook.active
            self.sheet.append(['Name', 'Number', 'Email'])

    def add_contacts(self, name: str, phone_number: int, email: str) -> None:
        """
        Adds a contact.

        Args:
            name (str): Name to be added or updated.
            number (int): Number to be added or updated.
            email (str): Email to be added or updated.
        """
        self.sheet.append([name, phone_number, email])
        self.workbook.save(self.file_name)

    def view_contact(self, name: str) -> dict:
        """
        Views a contact.

        Args:
            name (str): Name to be viewed.
        """
        contacts = []
        for row in self.sheet.iter_rows(values_only=True):
            if name.lower() in row[0].lower():
                contacts.append(list(row))

        for contact in contacts:
            print(contact)

    def delete_contact(self, name: str) -> None:
        """
        Deletes a contact.

        Args:
            name (str): Name to be deleted.
        """
        for idx, row in enumerate(self.sheet.iter_rows(values_only=True), 1):
            if row[0] == name:
                self.sheet.delete_rows(idx, 1)
        self.workbook.save(self.file_name)

    def clear_contact_book(self):
        """
        Clears all contacts.
        """
        while self.sheet.max_row > 1:
            self.sheet.delete_rows(2)
        self.workbook.save(self.file_name)

    def display_contacts(self):
        """
        Displays all contacts.
        """
        contacts = []
        for row in self.sheet.iter_rows(values_only=True):
            contacts.append(list(row))

        sorted_contacts = sorted(contacts[1:])
        print(contacts[0])
        for contact in sorted_contacts:
            print(contact)

    def exit(self):
        """
        Exits the program.
        """
        # print('Contacts saved successfully...')

    def contact_book_menu(self):
        """
        Displays Contact Book menu.
        """
        print('')
        print('Enter 1 to add contact.')
        print('Enter 2 to view a contact.')
        print('Enter 3 to delete a contact.')
        print('Enter 4 to clear contact book.')
        print('Enter 5 to display contacts.')
        print('Enter 6 to exit.')
        print('')
