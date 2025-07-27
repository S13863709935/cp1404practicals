from taxi import Taxi


def run_tests():
    """Test the Taxi class."""
    taxi = Taxi("Prius 1", 100)

    # Test driving
    distance_driven = taxi.drive(40)
    print(f"Expected: 40, Got: {distance_driven}")
    print(f"Expected details: Prius 1, fuel=60, odometer=40, 40km on current fare, $1.23/km")
    print(f"Got: {taxi}")
    print(f"Expected fare: $49.2, Got: ${taxi.get_fare():.2f}")

    # Test new fare
    taxi.start_fare()
    distance_driven = taxi.drive(100)
    print(f"\nExpected: 60, Got: {distance_driven} (can't drive full 100km)")
    print(f"Expected details: Prius 1, fuel=0, odometer=100, 60km on current fare, $1.23/km")
    print(f"Got: {taxi}")
    print(f"Expected fare: $73.8, Got: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    run_tests()