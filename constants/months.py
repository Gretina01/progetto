"""In this module there is a class to manage months numbering"""

# Import enum library to simplify the enumeration of months.
from enum import Enum

# Class to enumerate months. Inherits from enum.
class Month(Enum):
    """Definition of a class to enumerate months."""
    GENNAIO = 1
    FEBBRAIO = 2
    MARZO = 3
    APRILE = 4
    MAGGIO = 5
    GIUGNO = 6
    LUGLIO = 7
    AGOSTO = 8
    SETTEMBRE = 9
    OTTOBRE = 10
    NOVEMBRE = 11
    DICEMBRE = 12
