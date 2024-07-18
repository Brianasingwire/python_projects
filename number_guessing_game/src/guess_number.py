'''Number Guessing game'''

import random


def guess_the_number(start_number: int, stop_number: int):
    """
    Guessing a number from a given range of numbers.

    Args:
        start_number (int): Start number in range of numbers to guess from.
        stop_number (int): Stop number in range of numbers to guess from.
    """

    print('')
    random_number = random.randint(start_number, stop_number)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input(
            f"Enter a number between {start_number} and {stop_number}: ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('Please enter a number...')

        if user_guess == random_number:
            print(
                f"Congratulations, you guessed {random_number} correctly ⭐.")
            break
        if user_guess > random_number:
            print('Sorry, try again. Too high 😒.')
        else:
            print('Sorry, try again. Too low 😒.')

    print(f"You got the number in {guesses} guesses.")


if __name__ == '__main__':
    print('')
    start = int(input('Enter a starting number: '))
    stop = int(input('Enter a stopping number: '))

    guess_the_number(start, stop)
