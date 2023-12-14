"""This module contains the functions to load the dataset and to convert it into list."""
import json
import datetime
import requests
from classes.parking_class import Parking
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
    with open(my_path) as my_file:
        my_data = json.load(my_file)
        return my_data

# Definition of a function that converts a dictionary into list
def generate_parks_list(dictionary:dict):
    """Function that converts the dataset(dictionary) into a list, without repetitions."""
    parks_list = []
    surveyed_guids = []

    for park in dictionary['features']:
        guid = park["properties"]["guid"]
        if guid not in surveyed_guids:
            surveyed_guids.append(guid)
            lat = park["geometry"]["coordinates"][0]
            lon = park["geometry"]["coordinates"][1]
            name = park["properties"]["parcheggio"]
            total_spaces = park["properties"]["posti_totali"]
            parks_list.append(Parking(lat, lon, name, guid, total_spaces))

    for park in parks_list:
        for elem in dictionary['features']:
            if elem["properties"]["guid"] == park.get_parking_guid():
                try:
                    validate_spaces(elem["properties"]["posti_occupati"], park.get_total_spaces)
                    validate_datetime(elem["properties"]["data"])
                except ValueError as value:
                    print(value)
                else:
                    park.add_detection((datetime.datetime.fromtimestamp(elem["properties"]\
                                                                        ["data"]).strftime("%Y-%m-%d %H:%M:%S"),
                                                                        elem["properties"]["posti_occupati"]))
    return parks_list
