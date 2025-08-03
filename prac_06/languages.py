"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create ProgrammingLanguage objects and display dynamically typed ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()