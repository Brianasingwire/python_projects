'''Main entry point function'''

from src.generate_password import generate_password


def main():
    """
    Main entry point for the Password Generator project, this is a project to
    generate passwords of different lengths and complexities. Password
    generated contains uppercase, lowercase letters, digits and special
    characters.
    """

    while True:
        try:
            print('')
            password_length = int(
                input('Enter the desired length of your password: ').strip()
                or '8')
            if password_length < 8:
                raise ValueError
            break
        except ValueError:
            print('Password must have more than 8 characters')

    password = generate_password(
        password_length)

    print('Your generated password is:', password)


if __name__ == '__main__':
    main()
