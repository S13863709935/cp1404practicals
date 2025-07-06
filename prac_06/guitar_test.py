"""CP1404/CP5632 Practical - Test code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class methods with expected and actual results."""
    CURRENT_YEAR = 2022  # Constant for current year
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 0)

    print(f"{gibson.name} get_age() - Expected {CURRENT_YEAR - 1922}. Got {gibson.get_age(CURRENT_YEAR)}")
    print(
        f"{another_guitar.name} get_age() - Expected {CURRENT_YEAR - 2013}. Got {another_guitar.get_age(CURRENT_YEAR)}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(CURRENT_YEAR)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(CURRENT_YEAR)}")


if __name__ == "__main__":
    main()