"""CP1404/CP5632 Practical - Guitar collection program."""

from guitar import Guitar


def main():
    """Main guitar collection program."""
    print("My guitars!")
    guitars = load_guitars()

    if not guitars:
        print("No guitars loaded")
        return

    guitars.sort()
    display_guitars(guitars)
    add_new_guitars(guitars)
    save_guitars(guitars)


def load_guitars(filename='guitars.csv'):
    """Load guitars from CSV file.

    Args:
        filename: str - path to CSV file

    Returns:
        list: List of Guitar objects
    """
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    except FileNotFoundError:
        print(f"Warning: {filename} not found - starting with empty list")
    return guitars


def display_guitars(guitars):
    """Display sorted list of guitars.

    Args:
        guitars: list - List of Guitar objects
    """
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


def add_new_guitars(guitars):
    """Prompt user to add new guitars.

    Args:
        guitars: list - List to add new Guitar objects to
    """
    print("\nEnter new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = get_valid_input("Year: ", int)
        cost = get_valid_input("Cost: $", float)
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")


def get_valid_input(prompt, type_func):
    """Get valid user input of specified type.

    Args:
        prompt: str - input prompt
        type_func: type - type to convert to

    Returns:
        Validated user input
    """
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input; please enter a valid value")


def save_guitars(guitars, filename='guitars.csv'):
    """Save guitars to CSV file.

    Args:
        guitars: list - List of Guitar objects to save
        filename: str - path to save file
    """
    with open(filename, 'w') as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)


if __name__ == "__main__":
    main()