"""
State Names
Estimate: 30 minutes
Actual:   25 minutes
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

def main():
    """Main function to lookup state names."""
    print("State Names Program")
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {STATE_NAMES[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    print("\nAll states:")
    for code, name in STATE_NAMES.items():
        print(f"{code:3} is {name}")

if __name__ == "__main__":
    main()