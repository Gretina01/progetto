from classes.parking_class import Parking
from constants.months import Month

def export_csv(avg_free_spaces_by_time_slot: list, output_name_file: str, park: Parking, month: int, delimeter: str = ";"):

    with open(f"outputs/{output_name_file}.csv", "w") as csv_file:
        print("Saving file...")
        csv_file.write(f"park_name{delimeter}park_longitude{delimeter}park_latidude{delimeter}month{delimeter}hour{delimeter}free_parks_in_perc\n")
        for hour, value in enumerate(avg_free_spaces_by_time_slot):
            csv_file.write(f"{park.get_name()}{delimeter}{park.get_longitude()}{delimeter}{park.get_latitude()}{delimeter}{Month(month).name}{delimeter}{hour}{delimeter}{value:.2f}%\n")
        print("File saved successfully.")