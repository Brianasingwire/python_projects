'''Password Generator'''

import string

import secrets

# import random


def generate_password(min_length: int, numbers=True, special_characters=True):
    '''Function to generate random password'''
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits

    if special_characters:
        characters += special

    password = ''.join([secrets.choice(characters) for _ in range(min_length)])

    return password


# password = ''.join(random.sample(characters, min_length))
