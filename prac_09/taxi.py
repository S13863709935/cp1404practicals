from car import Car

FARE_PER_KM = 1.23  # Price per kilometer for all taxis


class Taxi(Car):
    """Represent a taxi that charges fare based on distance."""

    def __init__(self, name, fuel):
        """Initialize a taxi instance."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = FARE_PER_KM

    def __str__(self):
        """Return string representation of taxi."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Calculate and return the current fare."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the taxi and update fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven