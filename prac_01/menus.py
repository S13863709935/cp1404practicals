"""
CP1404/CP5632 - Practical
Menu-driven program example
Displays a greeting or goodbye using a name entered by the user.
"""

# Get name
name = input("Enter name: ")

# Display menu
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input(">>> ").upper()

# Process menu choices
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print(menu)
    choice = input(">>> ").upper()

print("Finished.")
