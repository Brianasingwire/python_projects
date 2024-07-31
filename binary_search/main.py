'''Main Entry Point Function'''

from src.generate_primes import generate_primes
from src.binary_search import binary_search


def main() -> None:
    """
    Main entry point function for the binary search algorithm. The algorithm
    will search through a sortedarray for the target value by repeatedly
    dividing the search array in half until the target value is found. If the
    target value is not found in the array, the algorithm will return -1.
    """
    n = 100
    prime_number = generate_primes(n)
    print(f"Prime numbers up to {n}: {prime_number}")

    target = 29
    result = binary_search(prime_number, target)

    if result != -1:
        print(f"Number found at index {result}")
    else:
        print('Number not found')


if __name__ == '__main__':
    main()
