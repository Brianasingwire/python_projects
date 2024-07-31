'''Generate Prime Numbers'''

import math


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num (int): Number being checked to see if it's a prime number.

    Returns:
        bool: Validation of whether number is a prime number or not.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def generate_primes(n: int) -> list:
    """
    Generate a list of prime numbers up to n (inclusive).

    Args:
        n (int): The endpoint limit for generating prime numbers.

    Returns:
        list: A list of prime numbers that have been generated.
    """
    prime_numbers = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
