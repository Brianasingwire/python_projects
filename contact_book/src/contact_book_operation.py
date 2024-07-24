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

    def view_contacts(self, name: str) -> list:
        """
        Views a contact.

        Args:
            name (str): Name to be viewed.
        """
        contacts = []
        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            if name.lower() in row[0].lower():
                contacts.append(list(row))

        return sorted(contacts)

    def delete_contact(self, name: str) -> bool:
        """
        Deletes a contact.

        Args:
            name (str): Name to be deleted.
        """
        for idx, row in enumerate(self.sheet.iter_rows(values_only=True), 1):
            if row[0] == name:
                self.sheet.delete_rows(idx, 1)
                self.workbook.save(self.file_name)
                return True
        return False

    def clear_contact_book(self):
        """
        Clears all contacts.
        """
        while self.sheet.max_row > 1:
            self.sheet.delete_rows(2)
        self.workbook.save(self.file_name)
