"""CP1404/CP5632 Practical - Client code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    """Create and display a list of Guitar objects."""
    guitars = []

    print("My guitars!")
    name = get_non_empty_input("Name: ")
    while name:  # More pythonic than while True with break
        year = int(get_non_empty_input("Year: "))
        cost = float(get_non_empty_input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = get_non_empty_input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_non_empty_input(prompt):
    """Get non-empty input from user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:  # If input is not empty
            return user_input
        print("Input cannot be empty. Please try again.")


if __name__ == "__main__":
    main()