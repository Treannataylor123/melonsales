"""Classes for melon orders."""


class abstract_melonOrder():
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        base_price = 5
        if self.species == 'Christmas':
            base_price *= 1.5
        if self.qty < 10 and self.order_type == "international":
            base_price += 3

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipp(self):
        self.shipped = True


class DomesticMelonOrder(abstract_melonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

class InternationalMelonOrder(abstract_melonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
 
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
