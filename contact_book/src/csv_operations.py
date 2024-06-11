'''CSV file operations for the Contact Book Project'''

import csv


def save_contacts(contacts):
    """Function to save contacts to a JSON file"""
    try:
        with open('contacts.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Contact'])
            for name, number in contacts.items():
                writer.writerow([name, number])
    except FileNotFoundError as e:
        print(f'Error saving contacts: {e}')


def load_contacts():
    """Function to load contacts from a JSON file"""

    try:
        with open('contacts.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            return {rows[0]: int(rows[1]) for rows in reader}
    except FileNotFoundError:
        print('Contact file not found')
        return {}
