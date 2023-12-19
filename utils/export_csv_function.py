"""This module contains the function to export data in .csv. """

# File Python that contains parking class.
from classes.parking_class import Parking
# File Python that contains a enumerate months class.
from constants.calendar import Month
# Import a python file containing validations function.
from utils.validations import validate_name

# Function that export results in .csv file.
def export_csv(avg_free_spaces_by_time_slot: list, output_name_file: str, parking: Parking, \
               month: int, delimiter: str = ";"):
    """Function that export results data in a .csv file."""
    with open(f"outputs/{output_name_file}.csv", "w", encoding = "utf-16") as csv_file:
        print("Saving file...")

        # Let the user choose the column names.
        while True:
            try:
                title_parkname = input("Provide the title of the column for the parking name: ")
                validate_name(title_parkname)
                break
            except ValueError as value:
                print(f"The error is: {value}")
            except TypeError as typeerr:
                print(f"The error is: {typeerr}")
        while True:
            try:
                title_longitude = input("Provide the title of the column for the longitude: ")
                validate_name(title_longitude)
                break
            except ValueError as value:
                print(f"The error is: {value}")
            except TypeError as typeerr:
                print(f"The error is: {typeerr}")
        while True:
            try:
                title_latitude = input("Provide the title of the column for the latitude: ")
                validate_name(title_latitude)
                break
            except ValueError as value:
                print(f"The error is: {value}")
            except TypeError as typeerr:
                print(f"The error is: {typeerr}")
        while True:
            try:
                title_month = input("Provide the title of the column for the month: ")
                validate_name(title_month)
                break
            except ValueError as value:
                print(f"The error is: {value}")
            except TypeError as typeerr:
                print(f"The error is: {typeerr}")
        while True:
            try:
                title_hour = input("Provide the title of the column for the hour: ")
                validate_name(title_hour)
                break
            except ValueError as value:
                print(f"The error is: {value}")
            except TypeError as typeerr:
                print(f"The error is: {typeerr}")
        while True:
            try:
                title_free_spaces = input("Provide the title of the column for the free spaces: ")
                validate_name(title_free_spaces)
                break
            except ValueError as value:
                print(f"The error is: {value}")
            except TypeError as typeerr:
                print(f"The error is: {typeerr}")

        # Write all results in the .csv file
        csv_file.write(f"{title_parkname}{delimiter}{title_latitude}{delimiter}{title_longitude}"
                       f"{delimiter}{title_month}{delimiter}{title_hour}{delimiter}"
                       f"{title_free_spaces}\n")
        for hour, value in enumerate(avg_free_spaces_by_time_slot):
            csv_file.write(f"{parking.get_name()}{delimiter}{parking.get_longitude()}"
                           f"{delimiter}{parking.get_latitude()}{delimiter}{Month(month).name}"
                           f"{delimiter}{hour}{delimiter}{value:.2f}%\n")
        print("File saved successfully.")
