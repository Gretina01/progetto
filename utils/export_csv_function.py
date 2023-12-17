"""This module contains the function to export data in .csv. """

# File Python that contains parking class.
from classes.parking_class import Parking

# File Python that contains a enumerate months class.
from constants.months import Month

# Function that export results.
def export_csv(avg_free_spaces_by_time_slot: list, output_name_file: str, parking: Parking, \
               month: int, delimiter: str = ";"):
    """Function that export results data in a .csv file."""
    with open(f"outputs/{output_name_file}.csv", "w", encoding = "utf-16") as csv_file:
        print("Saving file...")
        csv_file.write(f"parking_name{delimiter}parking_longitude{delimiter}parking_latidude\
                       {delimiter}month{delimiter}hour{delimiter}free_parks_in_%\n")
        for hour, value in enumerate(avg_free_spaces_by_time_slot):
            csv_file.write(f"{parking.get_name()}{delimiter}{parking.get_longitude()}{delimiter}\
                           {parking.get_latitude()}{delimiter}{Month(month).name}{delimiter}{hour}{delimiter}\
                            {value:.2f}%\n")
        print("File saved successfully.")
