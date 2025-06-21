"""
Hex Colours
Estimate: 20 minutes
Actual:   15 minutes
"""

COLOUR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2"
}

def main():
    """Look up hexadecimal colour codes by name."""
    colour_name = input("Enter colour name: ").upper()
    while colour_name != "":
        try:
            print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").upper()

if __name__ == "__main__":
    main()