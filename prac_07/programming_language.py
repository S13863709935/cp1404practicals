"""CP1404/CP5632 Practical - Programming Language class for original 5-language dataset."""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance from original 4-column data.

        Args:
            name: str - Language name
            typing: str - Static/Dynamic
            reflection: str - Yes/No
            year: int - First appeared year
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection == "Yes"
        self.year = year
        self.pointer_arithmetic = self._determine_pointer_arithmetic()

    def _determine_pointer_arithmetic(self):
        """Determine if language supports pointer arithmetic (for original 5 languages only)."""
        return self.name == "C++"  # Only C++ in original dataset supports it

    def __str__(self):
        """Return formatted string representation."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def is_dynamic(self):
        """Check if language is dynamically typed."""
        return self.typing.lower() == "dynamic"