"""CP1404/CP5632 Practical - Guitar class."""


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        Args:
            name: str - name of guitar
            year: int - year guitar was made
            cost: float - cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by year for sorting.

        Args:
            other: Guitar - another Guitar object

        Returns:
            bool: True if this guitar is older
        """
        return self.year < other.year

    def get_age(self, current_year=2023):
        """Calculate guitar's age.

        Args:
            current_year: int - year to calculate age from

        Returns:
            int: age of guitar
        """
        return current_year - self.year

    def is_vintage(self, current_year=2023):
        """Check if guitar is vintage (50+ years old).

        Args:
            current_year: int - year to check from

        Returns:
            bool: True if vintage
        """
        return self.get_age(current_year) >= 50