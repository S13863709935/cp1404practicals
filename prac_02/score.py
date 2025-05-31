"""CP1404/CP5632 - Practical
Refactored program to determine score status using functions.
Includes user input and random score evaluation.
"""

import random

def main():
    score = float(input("Enter score: "))
    print(determine_result(score))

    print("Random score result:")
    random_score = random.randint(0, 100)
    print(random_score)
    print(determine_result(random_score))

def determine_result(score):
    """Return the result message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
