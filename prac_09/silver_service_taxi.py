from taxi import Taxi

FLAGFALL = 4.50  # Additional charge for silver service


class SilverServiceTaxi(Taxi):
    """Represent a premium taxi with additional charges."""

    def __init__(self, name, fuel, fanciness):
        """Initialize a silver service taxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = FLAGFALL

    def __str__(self):
        """Return string representation of silver service taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate and return the current fare including flagfall."""
        return super().get_fare() + self.flagfall