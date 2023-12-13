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
from utils.load_function import *

def main():
   #dictionary = load_parks_dict("https://s3.amazonaws.com/vrai.univpm/FI/2023/12/disponibilita-parcheggi-storico.geojson")
    my_path = input("fornisci il percorso...")
    while True:
        try:
            load_parking_dict(my_path)
            break
        except Exception as ex:
            print (f"we got an error: {ex}")
    
    #parks_list = generate_parks_list(dictionary)

    #parks_list[0].plot_free_places()



if __name__ == "__main__":
    main()
