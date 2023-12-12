""""In this module there is a class that manages the parking lots in Bologna: 
defining the name, spaces and coordinates"""

from classes.point_class import Point
from utils.validations import validate_name, validate_spaces
from classes.detection_class import Detection
import matplotlib.pyplot as plt

class Parking(Point):
    """Definition of a class to manage name, spaces, latitude and longitude of a parking."""
    # The __init__ method initializes the attributes of an object.
    def __init__(self, latitude: (float, int) = "", longitude: (float, int) = "", \
                 parking_name: str = "", parking_guid: str = ""):
        """Constructor for point class"""
        super().__init__(latitude, longitude)
        self.set_name(parking_name)
        self.set_parking_guid(parking_guid)
        self._detections_list = []
    # The set method allows to set the name of parking attribute.
    def set_name(self, parking_name):
        """"Setting parking name private field."""
        try:
            validate_name(parking_name)
        except ValueError as e:
            print(f"Cannot setted the name because there was an error {e}")
        except TypeError as e:
            print(f"Cannot setted the name because there was an error {e}")
        else:
            self._name = parking_name
    # The set method allows to set the spaces of parking attribute.
    def set_spaces(self, parking_spaces):
        """"Setting parking spaces private field."""
        try:
            validate_spaces(parking_spaces)
        except ValueError as e:
            print(f"Cannot setted the name because there was an error {e}")
        except TypeError as e:
            print(f"Cannot setted the name because there was an error {e}")
        else:
            self._spaces = parking_spaces
    def set_parking_guid(self, parking_guid):
        self._parking_guid = parking_guid
    # The get method return the name attribute
    def get_name(self):
        """Getter for parking name private field."""
        return self._name
    def get_parking_guid(self):
        return self._parking_guid
    # Add a new Detection to this parking
    def add_detection(self, detection : Detection):
        self._detections_list.append(detection)
    # Get the list of all detectons for this parking:
    def get_detections_list(self):
        return self._detections_list
    def plot_free_places(self):
        detections = []
        free_spaces = []
        for detection in self._detections_list:
            detections.append(detection.get_datetime())
            free_spaces.append(detection.get_free_spaces())
        
        fig = plt.figure(figsize = (10, 5))
        
        # creating the bar plot
        plt.bar(detections, free_spaces, color ='maroon', 
                width = 0.4)
        
        plt.title("Parcheggi liberi in ogni rilevazione")
        plt.ylabel("Numero di parcheggi liberi")
        plt.xlabel("Singole rilevazioni")
        plt.show()
    # The __str__ method is responsible for returning a string representation of the object.
    def __str__(self):
        """It returns the conversation into string."""
        return f"Parking name ={self.get_name()} | Parking guid = {self.get_parking_guid()} \
            | Latitude={self.get_latitude()} | Longitude={self.get_longitude()} | Number of detections={len(self.get_detections_list())} ]"
    # The repr function returns a printable representation of the given object, while debubbing.
    def __repr__(self):
        """Representation of the object."""
        return f"[Parking name ={self.get_name()} | Parking guid = {self.get_parking_guid()}\
            | Latitude={self.get_latitude()} | Longitude={self.get_longitude()} | Number of detections={len(self.get_detections_list())} ]"
