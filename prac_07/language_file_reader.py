"""CP1404/CP5632 Practical - Language file reader for original 4-column format."""

from programming_language import ProgrammingLanguage


def main():
    """Read and display programming languages from original data file."""
    languages = load_languages('languages.csv')
    display_languages(languages)


def load_languages(filename):
    """Load languages from original 4-column CSV file.

    Args:
        filename: str - Path to CSV file (must have 4 columns)

    Returns:
        list: List of ProgrammingLanguage objects
    """
    languages = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:  # Strictly enforce original format
                language = ProgrammingLanguage(parts[0], parts[1], parts[2], int(parts[3]))
                languages.append(language)
    return languages


def display_languages(languages):
    """Display all languages."""
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()