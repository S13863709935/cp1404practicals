from musician import Musician


class Band:
    """Represent a band made up of musicians."""

    def __init__(self, name):
        """Initialize a band with a name and empty musicians list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of band."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing all musicians playing."""
        return "\n".join(musician.play() for musician in self.musicians)