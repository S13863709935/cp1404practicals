from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
DEFAULT_FANCINESS = 2


def main():
    """Run the taxi simulator program."""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, DEFAULT_FANCINESS),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            total_bill = process_drive(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Let user choose a taxi from the list."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def process_drive(taxi, current_bill):
    """Process driving a taxi."""
    if not taxi:
        print("You need to choose a taxi first")
        return current_bill

    try:
        distance = float(input("Drive how far? "))
        if distance <= 0:
            print("Distance must be > 0")
            return current_bill

        taxi.start_fare()
        distance_driven = taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return current_bill + fare
    except ValueError:
        print("Invalid input")
        return current_bill


def display_taxis(taxis):
    """Display all taxis with their numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()