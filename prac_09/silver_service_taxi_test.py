from silver_service_taxi import SilverServiceTaxi


def run_tests():
    """Test the SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Hummer", 200, 4)

    # Test initial state
    print(f"Expected: Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50")
    print(f"Got: {taxi}")

    # Test driving
    distance_driven = taxi.drive(10)
    print(f"\nExpected distance: 10, Got: {distance_driven}")
    print(f"Expected fare: $53.70, Got: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    run_tests()