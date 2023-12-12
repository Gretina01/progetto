"""""""""
import json
import datetime

def main():
    """"""
    while True:
        bologna_parking = input("percorso ????")
        try:
            with open(bologna_parking) as my_file:
                my_data = json.load(my_file)
                break
        except Exception as ex:
            print(f"we got an error. {ex}")

    
if __name__ == "__main__":
    main()"""
from utils.validations import validate_latitude
from classes.point_class import Point
def main():
    """entry-point"""
    """chiedere lat e lon fino a quando i valori non sono validi
    poi salvare i dati di lan e lon in un dizionario
    e poi salvare come json su file"""
    my_point = Point(input("fornisci point"))
    return my_point

    while True:
        try:
            my_lat = float(input("fornisci lat: "))
            if not isinstance(my_lat, (float,int)):
                raise TypeError(f"The latitude value must be float or int. It was provided {type(my_lat)}")
            if validate_latitude(my_lat):
                break
        except ValueError as ex:
            print (f"tou provided: {ex}")

if __name__ == "__main__":
    main()
