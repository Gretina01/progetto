""""In this module there is a class that manages the parking lots in Bologna: 
defining the name, spaces and coordinates"""

from classes.point_class import Point
from utils.validations import validate_name, validate_spaces

class Parking(Point):
    """Definition of a class to manage name, spaces, latitude and longitude of a parking."""
    # The __init__ method initializes the attributes of an object.
    def __init__(self, latitude: (float, int) = "", longitude: (float, int) = "", \
                 parking_name: str = "", parking_spaces: int = ""):
        """Constructor for point class"""
        super().__init__(latitude, longitude)
        self.set_name(parking_name)
        self.set_spaces(parking_spaces)
    # The set method allows to set the name of parking attribute.
    def set_name(self, parking_name):
        """"Setting parking name private field."""
        self._name = validate_name(parking_name)
    # The set method allows to set the spaces of parking attribute.
    def set_spaces(self, parking_spaces):
        """"Setting parking spaces private field."""
        self._spaces = validate_spaces(parking_spaces)
    # The get method return the name attribute
    def get_name(self):
        """Getter for parking name private field."""
        return self._name
    # The get method return the value of the parking spaces attribute
    def get_spaces(self):
        """Getter for parking spaces private field."""
        return self._spaces
    # The __str__ method is responsible for returning a string representation of the object.
    def __str__(self):
        """It returns the conversation into string."""
        return f"Parking name ={self.get_name()} | Parking spaces = {self.get_spaces()} \
            | Latitude={self.get_latitude()} | Longitude={self.get_longitude()}"
    # The repr function returns a printable representation of the given object, while debubbing.
    def __repr__(self):
        """Representation of the object."""
        return f"[Parking name ={self.get_name()} | Parking spaces = {self.get_spaces()} \
            | Latitude={self.get_latitude()} | Longitude={self.get_longitude()}]"
