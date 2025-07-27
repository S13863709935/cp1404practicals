from unreliable_car import UnreliableCar

TEST_RELIABILITY = 50  # 50% reliability for testing
TEST_ATTEMPTS = 100


def run_tests():
    """Test the UnreliableCar class."""
    unreliable_car = UnreliableCar("Old Bomb", 100, TEST_RELIABILITY)

    successful_drives = 0
    for _ in range(TEST_ATTEMPTS):
        if unreliable_car.drive(10) > 0:
            successful_drives += 1

    success_rate = successful_drives / TEST_ATTEMPTS * 100
    print(f"Success rate: {success_rate:.1f}% (should be close to {TEST_RELIABILITY}%)")


if __name__ == '__main__':
    run_tests()