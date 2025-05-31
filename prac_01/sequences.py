"""
CP1404/CP5632 - Practical
Menu-driven number sequence generator
"""

# Menu option constants
EVEN_OPTION = '1'
ODD_OPTION = '2'
SQUARE_OPTION = '3'
EXIT_OPTION = '4'

def show_even_numbers(x, y):
    print("Even numbers:")
    for num in range(x, y + 1):
        if num % 2 == 0:
            print(num, end=' ')
    print()

def show_odd_numbers(x, y):
    print("Odd numbers:")
    for num in range(x, y + 1):
        if num % 2 != 0:
            print(num, end=' ')
    print()

def show_squares(x, y):
    print("Squares:")
    for num in range(x, y + 1):
        print(num ** 2, end=' ')
    print()

def main():
    x = int(input("Enter the starting number (x): "))
    y = int(input("Enter the ending number (y): "))

    choice = ''
    while choice != EXIT_OPTION:
        print("\nMenu:")
        print(f"{EVEN_OPTION}. Show the even numbers from x to y")
        print(f"{ODD_OPTION}. Show the odd numbers from x to y")
        print(f"{SQUARE_OPTION}. Show the squares of the numbers from x to y")
        print(f"{EXIT_OPTION}. Exit the program")

        choice = input("Choose an option: ")

        if choice == EVEN_OPTION:
            show_even_numbers(x, y)
        elif choice == ODD_OPTION:
            show_odd_numbers(x, y)
        elif choice == SQUARE_OPTION:
            show_squares(x, y)
        elif choice == EXIT_OPTION:
            print("Goodbye!")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
