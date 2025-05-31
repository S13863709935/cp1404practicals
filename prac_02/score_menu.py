"""CP1404/CP5632 - Practical
Menu-driven score program using functions.
Allows getting a valid score, displaying result, showing stars, or quitting.
"""

def main():
    score = None  # 初始化为 None
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            if score is None:
                print("You need to get a score first!")
            else:
                print("Result:", determine_result(score))
        elif choice == 'S':
            if score is None:
                print("You need to get a score first!")
            else:
                show_stars(score)
        elif choice == 'Q':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def get_valid_score():
    """Get a valid score from 0 to 100 inclusive."""
    while True:
        try:
            score = int(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def determine_result(score):
    """Return the result message based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print stars equal to the score."""
    print("*" * score)

main()

