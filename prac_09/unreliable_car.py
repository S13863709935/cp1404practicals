from car import Car
import random

MIN_RELIABILITY = 0
MAX_RELIABILITY = 100


class UnreliableCar(Car):
    """Represent a car that may fail to drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize an unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car if it passes reliability check.
        Return distance driven if successful, 0 otherwise.
        """
        if random.randint(MIN_RELIABILITY, MAX_RELIABILITY) < self.reliability:
            return super().drive(distance)
        return 0