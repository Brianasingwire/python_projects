'''Contact Book Project'''

from openpyxl import load_workbook, Workbook


class ContactBook:
    """
    Contact Book class for storing contact information like name, phone number
    and email address of a person.
    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name

        try:
            self.workbook = load_workbook(self.file_name)
            self.sheet = self.workbook.active
        except FileNotFoundError:
            self.workbook = Workbook()
            self.sheet = self.workbook.active
            self.sheet.append(['Name', 'Number', 'Email'])

    def add_contacts(self, name, number, email):
        """
        Function to add or update contact.

        Args:
            name (str): Name to be added or updated.
            number (int): Number to be added or updated.
            email (str): Email to be added or updated.
        """
        for idx, row in enumerate(self.sheet.iter_rows(values_only=True), 1):
            if row[0] == name:
                self.sheet.cell(row=idx, column=2, value=number)
                self.sheet.cell(row=idx, column=3, value=email)
                break
        else:
            self.sheet.append([name, number, email])

    def view_contact(self, name):
        """
        Function to view a contact in Contact Book.

        Args:
            name (str): Name to be viewed.
        """
        for row in self.sheet.iter_rows(values_only=True):
            if row[0] == name:
                return {'Name': row[0], 'Phone': row[1], 'Email': row[2]}
        return None

    def delete_contact(self, name):
        """
        Function to delete a contact.

        Args:
            name (str): Name to be deleted.
        """
        for idx, row in enumerate(self.sheet.iter_rows(values_only=True), 1):
            if row[0] == name:
                self.sheet.delete_rows(idx, 1)

    def clear_contact_book(self):
        """
        Function to clear the Contact Book.
        """
        while self.sheet.max_row > 1:
            self.sheet.delete_rows(2)

    def display_contacts(self):
        """
        Function to display all contacts in Contact Book.
        """
        for row in self.sheet.iter_rows(values_only=True):
            print(row)

    def save_contacts(self):
        """
        Function to save the Contact Book.
        """
        self.workbook.save(self.file_name)

    def contact_book_menu(self):
        """
        Function to display Contact Book menu.
        """
        print('')
        print('Enter 1 to add contact.')
        print('Enter 2 to view a contact.')
        print('Enter 3 to delete a contact.')
        print('Enter 4 to clear contact book.')
        print('Enter 5 to display contacts.')
        print('Enter 6 to save contacts.')
        print('')
