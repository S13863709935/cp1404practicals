"""CP1404/CP5632 - Practical
Password check program with functions.
Prompts the user for a password and displays asterisks as feedback.
"""

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password (at least 8 characters) from the user."""
    pwd = input("Enter your password: ")
    while len(pwd) < 8:
        print("Too short!")
        pwd = input("Enter your password: ")
    return pwd

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))

main()

