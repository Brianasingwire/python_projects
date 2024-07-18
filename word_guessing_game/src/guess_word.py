'''Word Guessing game'''

import random


words = ['python', 'java', 'javascript',
         'ruby', 'kotlin', 'dart', 'swift', 'rust']


def guess_the_word():
    """
    Guessing a random word from a list of words.
    """

    random_word = random.choice(words)
    print('')
    print('Guess the word...')
    print(f"The word has {len(random_word)} letters.")
    user_guess = ''
    chances = len(random_word) + 1

    while chances > 0:
        wrong_guess = 0
        for character in random_word:
            if character in user_guess:
                print(character)
            else:
                wrong_guess += 1
                print('-')

        if wrong_guess == 0:
            print('Congratutions, you guessed right ⭐.')
            print(f"The word is '{random_word.upper()}'")
            break

        guess = input('Enter your guess: ')
        user_guess += guess

        if guess not in random_word:
            chances -= 1
            print(f"Wrong guess. You've {chances} chances left.")

            if chances == 0:
                print('Game Over. You lose!!!.')


if __name__ == '__main__':
    guess_the_word()
