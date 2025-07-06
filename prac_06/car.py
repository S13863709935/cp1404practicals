"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance with name and fuel."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add given amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if it has enough fuel.

        Returns the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return string representation of Car's name, fuel and odometer."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"