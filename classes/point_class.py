"""In this module there is a class that manages the coordinates of the parking lots in Bologna."""

from utils.validations import validate_latitude, validate_longitude

class Point():
    """Definition of a class to manage latitude and longitude"""
    # The __init__ method initializes the attributes of an object.
    def __init__(self, latitude: (float, int) = "", longitude: (float, int) = ""):
        """Constructor for point class"""
        # Verify that both values ​​are given: latitude and longitude.
        try:
            if latitude == "" or latitude == None or longitude == "" or longitude == None:
                raise ValueError("Only one coordinate is given. To define a point, \
                                 both latitude and longitude are needed")
        except ValueError as value:
            print(value)
        self.set_latitude(latitude)
        self.set_longitude(longitude)
    # The set method allows to set the value of the latitude attribute.
    def set_latitude(self, latitude):
        """Setting latitude private field."""
        try:
            validate_latitude(latitude)
        except Exception as e:
            print(f"Cannot setted the latidue because there was an error {e}")
        else:
            self._lat = latitude
            print(f"The latitude was ok and successfully setted")
        
    # The set method allows to set the value of the longitude attribute.
    def set_longitude(self, longitude):
        """Setting longitude private field."""
        try:
            validate_longitude(longitude)
        except Exception as e:
            print(f"Cannot setted the longitude because there was an error {e}")
        else:
            self._lon = longitude
            print(f"The longitude was ok and successfully setted")

    # The get method return the value of the latitude attribute
    def get_latitude(self):
        """Getter for latitude private field."""
        return self._lat
    # The get method return the value of the longitude attribute
    def get_longitude(self):
        """Getter for longitude private field."""
        return self._lon
    # The __str__ method is responsible for returning a string representation of the object.
    def __str__(self):
        """It returns the conversation into string."""
        return f"Latitude={self.get_latitude()} | Longitude={self.get_longitude()}"
    # The repr function returns a printable representation of the given object, while debubbing.
    def __repr__(self):
        """Representation of the object."""
        return f"[Latitude={self.get_latitude()} | Longitude={self.get_longitude()}]"
