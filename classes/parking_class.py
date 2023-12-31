""""In this module there is a class that manages the parking lots in Bologna: 
defining the name, spaces and coordinates of a parking."""

# Import a python file containing a point class.
from classes.point_class import Point
# Import a python file containing function validation.
from utils.validations import validate_name, validate_parking_guid, validate_total_spaces

# Class to define a parking. Inherits from the point class.
class Parking(Point):
    """Definition of a class to manage name, spaces, latitude and longitude of a parking."""
    # The __init__ method initializes the attributes of an object.
    def __init__(self, latitude: (float, int) = "", longitude: (float, int) = "", \
                 parking_name: str = "", parking_guid: str = "", total_spaces: int = ""):
        """Constructor for point class"""
        super().__init__(latitude, longitude)
        self.set_name(parking_name)
        self.set_parking_guid(parking_guid)
        self.set_total_spaces(total_spaces)
        self._detections_list = []

    # The set method allows to set the name of parking attribute.
    def set_name(self, parking_name):
        """"Setting parking name private field."""
        try:
            validate_name(parking_name)
        except ValueError as value:
            print(f"Cannot setted the name because there was an error: {value}.")
        except TypeError as typeerr:
            print(f"Cannot setted the name because there was an error: {typeerr}.")
        else:
            self._name = parking_name

    # The set method allows to set the guid of parking attribute.
    def set_parking_guid(self, parking_guid):
        """Setting parking guid private field."""
        try:
            validate_parking_guid(parking_guid)
        except ValueError as value:
            print(f"Cannot setted the parking guid because there was an error: {value}.")
        except TypeError as typeerr:
            print(f"Cannot setted the parking guid because there was an error: {typeerr}.")
        else:
            self._parking_guid = parking_guid

    # The set method allows to set the total spaces of parking attribute.
    def set_total_spaces(self, total_spaces):
        """"Setting total parking spaces private field."""
        try:
            validate_total_spaces(total_spaces)
        except ValueError as value:
            print(f"Cannot setted the total spaces because there was an error: {value}.")
        except TypeError as typeerr:
            print(f"Cannot setted the total spaces because there was an error: {typeerr}.")
        else:
            self._total_spaces = total_spaces

    # The get method return the name attribute.
    def get_name(self):
        """Getter for parking name private field."""
        return self._name

    # The get method return the parking guid attribute.
    def get_parking_guid(self):
        """Getter for parking guid private field."""
        return self._parking_guid

    # The get method return the total spaces attribute.
    def get_total_spaces(self):
        """Getter for parking total spaces private field."""
        return self._total_spaces

    # Add a new detection to this parking.
    def add_detection(self, detection):
        """Class helper method, it adds detections to this parking."""
        self._detections_list.append(detection)

    # Get the list of all detectons for this parking.
    def get_detections_list(self):
        """Class helper method, returns the list of detections of this parking."""
        return self._detections_list

    # Get the coordinates of this parking.
    def get_point(self):
        """Class helper method, returns the point of this parking."""
        return Point(self.get_latitude(), self.get_longitude())

    # The __str__ method is responsible for returning a string representation of the object.
    def __str__(self):
        """It returns the conversation into string."""
        return f"Parking name ={self.get_name()} | Parking guid = {self.get_parking_guid()} \
            | Latitude={self.get_latitude()} | Longitude={self.get_longitude()} \
                | Number of detections={len(self.get_detections_list())} ]"

    # The repr function returns a printable representation of the given object, while debubbing.
    def __repr__(self):
        """Representation of the object."""
        return f"[Parking name ={self.get_name()} | Parking guid = {self.get_parking_guid()}\
           | Latitude={self.get_latitude()} | Longitude={self.get_longitude()} \
            | Number of detections={len(self.get_detections_list())}]"
