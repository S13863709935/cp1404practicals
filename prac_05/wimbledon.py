"""
Wimbledon Champions
Estimate: 60 minutes
Actual:   75 minutes
"""


def load_data(filename):
    """Load data from CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(",") for line in file]


def process_data(data):
    """Process data to count champions and list countries."""
    champions = {}
    countries = set()
    for row in data:
        champions[row[2]] = champions.get(row[2], 0) + 1
        countries.add(row[1])
    return champions, sorted(countries)


def main():
    """Main function to display Wimbledon statistics."""
    data = load_data("wimbledon.csv")
    champions, countries = process_data(data)

    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()