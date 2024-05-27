'''Tests for Password Generator Project'''

import string

import pytest

from src.generate_password import generate_password


def test_generate_password_length_8():
    """
    Test password length is 8
    """

    password = generate_password(8)
    assert len(password) == 8


def test_contains_letters_digits_specials():
    """
    Test for letters, digits and specials
    """

    password = generate_password(12)
    assert any(c in string.ascii_letters for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)


def test_randomness_of_password():
    """
    Test for password randomness
    """

    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2
