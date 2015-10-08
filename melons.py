"""Ubermelon melon types.

This provides a Melon class, helper methods to get all melons, find a
melon by id.

It reads melon data in from a text file.
"""


class Melon(object):
    """An Ubermelon Melon type."""

    def __init__(self,
                 id,
                 melon_type,
                 common_name,
                 price,
                 image_url,
                 color,
                 seedless,
                 ):
        self.id = id
        self.melon_type = melon_type
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    def price_str(self):
        """Return price formatted as string $x.xx"""

        return "$%.2f" % self.price

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<Melon: %s, %s, %s>" % (
            self.id, self.common_name, self.price_str())


def read_melon_types_from_file(filepath):
    """Read melon type data and populate dictionary of melon types.

    Dictionary will be {id: Melon object}
    """

    melon_types = {}

    for line in open(filepath):
        (id,
         melon_type,
         common_name,
         price,
         img_url,
         color,
         seedless) = line.strip().split("|")

        id = int(id)
        price = float(price)

        # For seedless, we want to turn "1" => True, otherwise False
        seedless = (seedless == "1")

        melon_types[id] = Melon(id,
                                melon_type,
                                common_name,
                                price,
                                img_url,
                                color,
                                seedless)

    return melon_types


def get_all():
    """Return list of melons."""

    # This relies on access to the global dictionary `melon_types`

    return melon_types.values()


def get_by_id(id):
    """Return a melon, given its ID."""

    # This relies on access to the global dictionary `melon_types`

    return melon_types[id]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

melon_types = read_melon_types_from_file("melons.txt")