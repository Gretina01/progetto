""""""
import json
import requests

def get_data_from_url(url:str):
    out = requests.get(url)
    my_data = json.loads(out.text)
    return my_data

def get_data_from_local():
    my_path = input("Inserisci path")
    with open(my_path) as my_file:
        my_data = json.load(my_file)
        return my_data
