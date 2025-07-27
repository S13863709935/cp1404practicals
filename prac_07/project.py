"""CP1404/CP5632 Practical - Project class."""

from datetime import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost, completion):
        """Initialize a Project instance.

        Args:
            name: str - project name
            start_date: str - start date in dd/mm/yyyy format
            priority: int - project priority
            cost: float - estimated cost
            completion: int - completion percentage
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return formatted string representation."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting.

        Args:
            other: Project - another Project object

        Returns:
            bool: True if this project has higher priority
        """
        return self.priority < other.priority

    def is_complete(self):
        """Check if project is complete.

        Returns:
            bool: True if completion is 100%
        """
        return self.completion == 100