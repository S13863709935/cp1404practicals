"""
Emails
Estimate: 40 minutes
Actual:   50 minutes
"""

def extract_name(email):
    """Extract name from email address."""
    username = email.split("@")[0]
    return " ".join(part.title() for part in username.split("."))

def main():
    """Main function to store and display emails with names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ["", "y"]:
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    print("\nStored Emails:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()