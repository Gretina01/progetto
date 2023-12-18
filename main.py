""""""

__author__ = "Greta Gasparini"

# The re built-in package can be used to check whether a string contains the
# specified search pattern.
import re
# Python file that contains functions that allows to store the dataset.
from utils.load_convert_function import get_data_from_url, get_data_from_local, \
    generate_parking_list
# Python file that contains function that allows to generate plot.
from utils.plot_function import generate_free_parks_in_hours_for_month, \
    generate_free_parks_in_hours_for_day, generate_figure_and_plot_for_month, \
        generate_figure_and_plot_for_day
# Python file that contains function that allows to export results in a .csv file.
from utils.export_csv_function import export_csv
# Import a python file containing validations function.
from utils.validations import validate_file_name, validate_delimiter, validate_month, validate_day,\
    validate_latitude, validate_longitude, validate_hour, validate_parking_choice, validate_format_image
#Import file that contains Point class.
from classes.point_class import Point

def main():
    """Function that provides information on parking in Bologna"""
    print("This code is used to get informations about parking lots in Bologna.")
    # Load dataset.
    dictionary = None
    while dictionary is None:
        user_choice = input("Do you want to open the dataset from online or local? ")
        # Code to open dataset from url (online).
        if user_choice.lower() == 'online' or user_choice.lower() =="o":
            print("You have chosen to open an online dataset.")
            try:
                dictionary = get_data_from_url(input("Input url: "))
            except ValueError as value:
                print (f"There is an error: {value}")
            except ConnectionError as conn:
                print (f"There is an error: {conn}")
        # Code to open dataset from file (local).
        elif user_choice.lower() == 'local' or user_choice.lower() =="l":
            print("You have chosen to open an offline dataset.")
            try:
                dictionary = get_data_from_local(input("Input file path: "))
            except ValueError as value:
                print (f"There is an error: {value}")
        # If the user choice is not valid, an error is raised.
        else:
            print("Invalid choice. Please enter 'online' or 'local'.")
    print("Dictionary loaded successfully.")

    # Convert dataset into a list.
    parking_list = generate_parking_list(dictionary)
    print(f"The number of parking lots considered in Bologna are {len(parking_list)}.")

    # User choices to display the desired graph.
    # A graph will be plotted according to the month and the chosen parking lot.
    # User choice of month.
    chosen_month_int = None
    while chosen_month_int is None:
        try:
            chosen_month_str = input("Indicate the month for which you want to see availability: ")
            chosen_month_int = validate_month(chosen_month_str)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")

    # User choice of parking.
    print("Choose the desired parking lot: ")
    for i, parking in enumerate(parking_list):
        print(f"Write {i} for parking {parking.get_name()}")
    chosen_parking_int = None
    while chosen_parking_int is None:
        try:
            chosen_parking_str = input("The chosen parking lot is: ")
            chosen_parking_int = validate_parking_choice(chosen_parking_str)
            break
        except TypeError as typeerr:
            print(f"The error is {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")

    # Save an image of plot.
    print("Before viewing the graph, please choose image name and format for saving.")

    # User choice of image name.
    while True:
        try:
            img_output_name_file = input("Choose the image file name: ")
            validate_file_name(img_output_name_file)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # User choice of image format name.
    while True:
        try:
            img_format = input("Choose the image file format: ")
            validate_format_image(img_format)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # Generate the plot.
    print("The required graph is: ")
    free_parking_for_month = generate_free_parks_in_hours_for_month\
        (chosen_month_int, parking_list[chosen_parking_int])
    generate_figure_and_plot_for_month(free_parking_for_month, chosen_month_int, \
                                       img_output_name_file, img_format)

    # Save a .csv file of results
    print("To save a .csv of results, please choose the file name and the delimiter.")

    # User choice of .csv file name.
    while True:
        csv_output_name_file = input("Choose the name of the CSV file:")
        delimiter = input("Choose the CSV file delimiter: ")
        try:
            validate_file_name(csv_output_name_file)
            validate_delimiter(delimiter)
            break
        except re.error as e:
            print(f"The error is: {e}")
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # Save a .csv file.
    export_csv(free_parking_for_month, csv_output_name_file, parking_list[chosen_parking_int], \
               chosen_month_int, delimiter)

    # User choices to display the desired graph.
    # A graph will be plotted according to the week day and the chosen parking lot.
    # User choice of day.
    chosen_day_int = None
    while chosen_day_int is None:
        try:
            chosen_day_str = input("Indicate the day for which you want to see availability: ")
            chosen_day_int = validate_day(chosen_day_str)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}.")
        except ValueError as value:
            print(f"The error is: {value}.")

    # User choice of parking.
    print("Choose the desired parking lot: ")
    for i, parking in enumerate(parking_list):
        print(f"Write {i} for parking {parking.get_name()}")
    while True:
        try:
            parking_choice = input("The chosen parking lot is: ")
            validate_parking_choice(parking_choice)
            break
        except TypeError as typeerr:
            print(f"The error is {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")

    # Save an image of plot.
    print("Before viewing the graph, please choose image name and format for saving.")

    # User choice of image name.
    while True:
        try:
            img_output_name_file = input("Choose the image file name: ")
            validate_file_name(img_output_name_file)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # User choice of image format name.
    while True:
        try:
            img_format = input("Choose the image file format: ")
            validate_format_image(img_format)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # Generate the plot.
    print("The required graph is: ")
    free_parking_for_day = generate_free_parks_in_hours_for_day(chosen_day_int, \
                                                                parking_list[parking_choice])
    generate_figure_and_plot_for_day(free_parking_for_day, chosen_day_int, \
                                     img_output_name_file, img_format)

    # Save a .csv file of results
    print("To save a .csv of results, please choose the file name and the delimiter.")

    # User choice of .csv file name.
    while True:
        csv_output_name_file = input("Choose the name of the CSV file:")
        delimiter = input("Choose the CSV file delimiter: ")
        try:
            validate_file_name(csv_output_name_file)
            validate_delimiter(delimiter)
            break
        except re.error as e:
            print(f"The error is: {e}")
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # Save a .csv file.
    export_csv(free_parking_for_day, csv_output_name_file, parking_list[parking_choice], \
               chosen_day_int, delimiter)

    # Have the user enter their location, in terms of latitude and longitude.
    print("Please insert your latitude and longitude, to calculate the best parking.")
    while True:
        user_latitude = float(input("Insert your latitude: "))
        user_longitude = float(input("Insert your longitude: "))
        try:
            validate_latitude(user_latitude)
            validate_longitude(user_longitude)
            break
        except TypeError as typeerr:
            print(f"Is required a float value of latitude and longitude, \
                                    the error is {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")

    # Ask the user to enter the month and time slot they want to go to.
    print("Please insert the month and time slot you want to go. ")
    while True:
        chosen_month_str = input("Indicate the month: ")
        chosen_hour_str = input("Indicate the hour: ")
        try:
            chosen_month_int = validate_month(chosen_month_str)
            chosen_hour_int = validate_hour(chosen_hour_str)
            break
        except TypeError as typeerr:
            print(f"Is required a int value of month, \
                                    the error is: {typeerr}.")
        except ValueError as value:
            print(f"The error is: {value}.")

    # Find the percentage of free parking spaces in the chosen month and hour for all parking lots.
    best_park = None
    for park in parking_list:
        if best_park is None:
            best_park = park
        else:
            if generate_free_parks_in_hours_for_month(chosen_month_int, park)[chosen_hour_int] > \
                generate_free_parks_in_hours_for_month(chosen_month_int, best_park)[chosen_hour_int]:
                best_park = park

    # Calculate the distance between the user and the best parking lot.
    distance = best_park.get_distance_from_this_parking(Point(user_latitude, user_longitude))
    print(f"The best parking lot is {best_park.get_name()} with \
          {generate_free_parks_in_hours_for_month(chosen_month_int, best_park)[chosen_hour_int]}%  \
            of free parking spaces that is {distance} m from you.")

if __name__ == "__main__":
    main()
