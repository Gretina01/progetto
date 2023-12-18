"""This module contains the function to export data in .csv. """

# File Python that contains parking class.
from classes.parking_class import Parking

# File Python that contains a enumerate months class.
from constants.calendar import Month

from utils.validations import validate_name

# Function that export results.
def export_csv(avg_free_spaces_by_time_slot: list, output_name_file: str, parking: Parking, \
               month: int, delimiter: str = ";"):
    """Function that export results data in a .csv file."""
    with open(f"outputs/{output_name_file}.csv", "w", encoding = "utf-16") as csv_file:
        print("Saving file...")
        
        while True:
            try:
                title_parkname = input("Provide the title of the column for the parking name: ")
                validate_name(title_parkname)
                break
            except ValueError as value:
                print(value)
            except TypeError as value:
                print(value)
        while True:
            try:
                title_longitude = input("Provide the title of the column for the longitude: ")
                validate_name(title_longitude)
                break
            except ValueError as value:
                print(value)
            except TypeError as value:
                print(value)
        while True:
            try:
                title_latitude = input("Provide the title of the column for the latitude: ")
                validate_name(title_latitude)
                break
            except ValueError as value:
                print(value)
            except TypeError as value:
                print(value)
        while True:
            try:
                title_month = input("Provide the title of the column for the month: ")
                validate_name(title_month)
                break
            except ValueError as value:
                print(value)
            except TypeError as value:
                print(value)
        while True:
            try:
                title_hour = input("Provide the title of the column for the hour: ")
                validate_name(title_hour)
                break
            except ValueError as value:
                print(value)
            except TypeError as value:
                print(value)
        while True:
            try:
                title_free_spaces = input("Provide the title of the column for the free spaces: ")
                validate_name(title_free_spaces)
                break
            except ValueError as value:
                print(value)
            except TypeError as value:
                print(value)    

        csv_file.write(f"{title_parkname}{delimiter}{title_latitude}{delimiter}{title_longitude}{delimiter}{title_month}{delimiter}{title_hour}{delimiter}{title_free_spaces}\n")
        for hour, value in enumerate(avg_free_spaces_by_time_slot):
            csv_file.write(f"{parking.get_name()}{delimiter}{parking.get_longitude()}{delimiter}{parking.get_latitude()}{delimiter}{Month(month).name}{delimiter}{hour}{delimiter}{value:.2f}%\n")
        print("File saved successfully.")
