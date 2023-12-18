"""This module contains the functions to load the dataset and to convert it into list."""

# Json is a library that allows you to work with json and geojson files in Python.
import json
# The os module provides a portable way of using operating system dependent functionality.
import os
# The datetime module supplies classes to work with date and time. These classes provide a number
# of functions to deal with dates, times, and time intervals.
from datetime import datetime
# The requests module allows to send HTTP requests using Python.
import requests
# File Python that contains parking class.
from classes.parking_class import Parking
# Import a python file containing validations function.
from utils.validations import validate_spaces, validate_datetime

# Definition of a function that manages the import of the dataset from url
def get_data_from_url(url:str):
    """Get dataset online, from url"""
    out = requests.get(url, timeout=10)
    if out.status_code == 200:
        my_data = json.loads(out.text)
        return my_data
    raise ConnectionError("Error during requests")

# Definition of a function that manages the import of the dataset from file
def get_data_from_local(my_path):
    """Get dataset offline, from file"""

    if os.path.exists(my_path) is False:
        raise ValueError("File not found")

    with open(my_path, encoding = "utf-8") as my_file:
        my_data = json.load(my_file)
        return my_data

# Definition of a function that converts a dictionary into a list.
def generate_parking_list(dictionary: dict):
    """Function that converts the dataset(dictionary) into a list, without repetitions."""
    parking_list = []
    surveyed_guids = []

    for parking in dictionary['features']:
        guid = parking["properties"]["guid"]
        if guid not in surveyed_guids: #se non ho ancora scoperto qiel parcheggio ci creo la lista, in modo univocp
            surveyed_guids.append(guid)
            lat = parking["geometry"]["coordinates"][0]
            lon = parking["geometry"]["coordinates"][1]
            name = parking["properties"]["parcheggio"]
            total_spaces = parking["properties"]["posti_totali"]
            parking_list.append(Parking(lat, lon, name, guid, total_spaces))
    # per ogni parcheggio univoco cerco le sue rilevazioni e le aggiungo al parcheggio considerato
    for parking in parking_list:
        for elem in dictionary['features']:
            if elem["properties"]["guid"] == parking.get_parking_guid():
                try:
                    validate_spaces(elem["properties"]["posti_occupati"], parking.get_total_spaces)
                    validate_datetime(elem["properties"]["data"])
                except ValueError as value:
                    print(value)
                else:
                    parking.add_detection((datetime.fromtimestamp(elem["properties"]["data"])\
                                           .strftime("%Y-%m-%d %H:%M:%S"), elem\
                                            ["properties"]["posti_occupati"]))
    return parking_list
