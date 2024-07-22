'''Password Generator Project'''

import string

import random

import math


def generate_password(password_length: int) -> str:
    """
    Function generating random passwords.

    Args:
        password_length (int): Length of the password to be generated.

    Returns:
        str: Password that has been generated.
    """

    num_letters = math.ceil(password_length / 2)
    num_digits = math.floor(password_length / 4)
    num_special = password_length - (num_letters + num_digits)

    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    special = random.choices(string.punctuation, k=num_special)

    combined_list = letters+digits+special

    random.shuffle(combined_list)

    password = ''.join(combined_list)

    return password
