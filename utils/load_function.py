import json
import requests
from classes.parking_class import Parking
from classes.detection_class import Detection
from utils.validations import *


def load_dict_from_url(url:str):
    try:
        out = requests.get(url)
        if out.status_code == 200:
            dictionary = json.loads(out.text)
            return dictionary
        else:
            raise Exception("error during requests")
    except Exception as ex:
        raise Exception (f"we got an error {ex}")
    
def load_dict_from_file(path:str):
    with open(path) as my_file:
        dictionary = json.load(my_file)
        return dictionary
    

"""def load_parks_dict(url:str):
    data = get_file_from_url(url)
    dictionary = json.loads(data)
    return dictionary"""



def generate_parks_list(dictionary:dict):
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
                except ValueError as e:
                    print(e)
                else:
                    park.add_detection((datetime.datetime.fromtimestamp(elem["properties"]["data"]).strftime("%Y-%m-%d %H:%M:%S%z"), elem["properties"]["posti_occupati"]))
    return parks_list

"""my_list_of_parks = []
for park in my_data:
    my_list_of_parks.append(Park(park["geo_point_2d"]["lat"], park["geo_point_2d"]["lon"], 0.0, park["nome"], park["tipologia"], park["indirizzo"], park["quartiere"]))"""