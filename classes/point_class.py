"""In this module there is a class that manages the coordinates of the parking lots in Bologna."""

class Point():
    """Definition of a class to manages latitude and longitude"""
    # The __init__ method initializes the attributes of an object.
    def __init__(self, latitude = "", longitude = ""):
        """Constructor for point class"""
        self.set_latitude(latitude)
        self.set_longitude(longitude)
    # The set method allows to set the value of the latitude attribute.
    def set_latitude(self, latitude):
        """Setting latitude private field."""
        if not isinstance(latitude, (int, float)):
            raise TypeError(f"Is required a flot or int value of latitude \
                            it's provided {type(latitude)}")
        self._lat = latitude
    # The set method allows to set the value of the longitude attribute.
    def set_longitude(self, longitude):
        """Setting longitude private field."""
        if not isinstance(longitude, (int, float)):
            raise TypeError(f"Is required a flot or int value of latitude \
                            it's provided {type(longitude)}")
        self._lon = longitude
    # The get method return the value of the latitude attribute
    def get_latitude(self):
        """"""
        return self._lat
    # The get method return the value of the longitude attribute
    def get_longitude(self):
        """"""
        return self._lon
