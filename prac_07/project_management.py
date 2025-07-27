"""CP1404/CP5632 Practical - Project management program."""

from project import Project
from datetime import datetime
import sys


def main():
    """Main project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        display_menu()
        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            if confirm_save():
                save_projects(projects, 'projects.txt')
            print("Thank you for using custom-built project management software.")
            sys.exit()
        else:
            print("Invalid menu choice")


def display_menu():
    """Display the main menu."""
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from specified file.

    Args:
        filename: str - path to project file

    Returns:
        list: List of Project objects
    """
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 5:
                    projects.append(Project(
                        parts[0], parts[1], int(parts[2]),
                        float(parts[3]), int(parts[4])))
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    return projects


def save_projects(projects, filename):
    """Save projects to specified file.

    Args:
        projects: list - List of Project objects
        filename: str - path to save file
    """
    with open(filename, 'w') as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost}\t{project.completion}", file=file)


def display_projects(projects):
    """Display projects grouped by completion status.

    Args:
        projects: list - List of Project objects
    """
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects after specified date.

    Args:
        projects: list - List of Project objects
    """
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered = [p for p in projects if p.start_date > filter_date]
        for project in sorted(filtered, key=lambda x: x.start_date):
            print(project)
    except ValueError:
        print("Invalid date format")


def add_new_project(projects):
    """Add a new project to the list.

    Args:
        projects: list - List to add new Project to
    """
    print("\nLet's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update an existing project's completion and priority.

    Args:
        projects: list - List of Project objects
    """
    print("\nSelect project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_completion = input("New Percentage: ")
        if new_completion:
            project.completion = int(new_completion)

        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid project selection")


def confirm_save():
    """Confirm if user wants to save before quitting.

    Returns:
        bool: True if user wants to save
    """
    response = input("Would you like to save to projects.txt? ").lower()
    return response.startswith('y')


if __name__ == "__main__":
    main()