"""In this module there is a class to manage months and days numbering."""

# Import enum library to simplify the enumeration of months and days.
from enum import Enum

# Class to enumerate months. Inherits from enum.
class Month(Enum):
    """Definition of a class to enumerate months."""
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

# Class to enumerate days. Inherits from enum.
class Day(Enum):
    """Definition of a class to enumerate days."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
