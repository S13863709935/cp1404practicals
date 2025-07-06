"""CP1404/CP5632 Practical - Guitar class."""


class Guitar:
    """Represent a Guitar object."""

    VINTAGE_AGE = 50  # Class constant for vintage age threshold

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance with name, year and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return how old the guitar is in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if guitar is VINTAGE_AGE or more years old."""
        return self.get_age(current_year) >= self.VINTAGE_AGE