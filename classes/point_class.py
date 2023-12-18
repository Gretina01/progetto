"""In this module there is a class that manages the coordinates of the parking lots in Bologna."""

# Import a python file containing validations function.
from utils.validations import validate_latitude, validate_longitude
# Import math library to use radians, cos, sin, asin
from math import radians, cos, sin, asin, sqrt

# The constant of earth radius in meters is defined to be used in the distance between two points.
EARTH_RADIUS = 6371000.0

# Class to define a point.
class Point():
    """Definition of a class to manage latitude and longitude"""
    # The __init__ method initializes the attributes of an object.
    def __init__(self, latitude: (float, int) = "", longitude: (float, int) = ""):
        """Constructor for point class"""
        # Verify that both values are given: latitude and longitude.
        try:
            if latitude == "" or latitude is None or longitude == "" or longitude is None:
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
        except ValueError as e:
            print(f"Cannot setted the latitude because there was an error {e}")
        except TypeError as e:
            print(f"Cannot setted the latitude because there was an error {e}")
        else:
            self._lat = latitude

    # The set method allows to set the value of the longitude attribute.
    def set_longitude(self, longitude):
        """Setting longitude private field."""
        try:
            validate_longitude(longitude)
        except ValueError as e:
            print(f"Cannot setted the latidue because there was an error {e}")
        except TypeError as e:
            print(f"Cannot setted the latidue because there was an error {e}")
        else:
            self._lon = longitude

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

    # Define a function that returns the value of the distance between two points
    # using the Haversine formula.
    def get_distance_from_this_point(self, obj):
        """Class helper method, returns the distance between two points."""
        if isinstance(obj, Point):
            lat_user = self.get_latitude()
            lon_user = self.get_longitude()
            lat_parking = obj.get_latitude()
            lon_parking = obj.get_longitude()
            print(f"lat_user={lat_user} | lon_user={lon_user} | lat_parking={lat_parking} | lon_parking={lon_parking}")
            # Convert latitude and longitude from degrees to radians.
            lat_parking, lon_parking, lat_user, lon_user = map(radians, [lat_parking, lon_parking, \
                                                                        lat_user, lon_user])
            # Calculate the difference of latitude and longitude.
            delta_lat = lat_user - lat_parking
            delta_lon = lon_user - lon_parking
            # Calculate the difference with Haversine formula.
            a = sin(delta_lat/2)**2 + cos(lat_parking) * cos(lat_user) * sin(delta_lon/2)**2
            c = 2 * asin(sqrt(a))
            return EARTH_RADIUS * c
        raise TypeError("The lat_user and lon_user pair are not type Point")