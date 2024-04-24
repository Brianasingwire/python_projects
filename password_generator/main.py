'''Main calling function'''

from src.generate_password import generate_password


def main():
    '''Calling function'''
    while True:
        try:
            print('')
            min_length = int(
                input('Enter the desired length of your password: '))
            if min_length < 8:
                raise ValueError
            break
        except ValueError:
            print('Password must have more than 8 characters')

    numbers = input('Do you want to include numbers? (y/n): ').lower() == 'y'
    special_characters = input(
        'Do you want to include special characters? (y/n): ').lower() == 'y'

    password = generate_password(
        min_length, numbers, special_characters)

    print('Your generated password is:', password)


if __name__ == '__main__':
    main()


# Variable length
# Contains letters, numbers and special characters
