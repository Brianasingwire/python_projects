'''Tests for Password Generator Project'''

import string

import pytest

from src.generate_password import generate_password


def test_contains_letters_digits_specials():
    """
    Test for letters, digits and specials
    """

    password = generate_password(12)
    assert any(c in string.ascii_letters for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)


@pytest.mark.parametrize('length', [8, 12, 16, 20])
def test_various_password_lengths(length):
    """
    Testing various password lenghts
    """

    password = generate_password(length)
    assert len(password) == length
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
