"""This program allows you to obtain information on the availability of parking in Bologna.
The car parks considered are VIII Agosto, Riva Reno, Autostazione.
First you need to store the dataset, it can be imported both locally and online.
To work on the data you need to convert the dataset, which is initially a dictionary, 
into a list of objects compliant with the Parking object.
To define the Parking lot object, create a class that models a parking lot considering the name, 
total spaces and coordinates. It inherits the coordinates from a class that allows you to model 
a point as a function of latitude and longitude.
For each Parking object created, the findings present in the dataset are added to it.
Once this is done, it is possible to obtain graphs based on the time slot and the average 
number of free places in %, letting the user choose the month and day of the week.
It is possible to save graphs as an image file, with the possibility of choosing the format, 
and as a csv file, with the possibility of choosing the name of the columns and the delimiter.
Furthermore, it is possible to have the user enter their position, in terms of latitude and 
longitude, the month and the time in which they would like to go to a car park in Bologna.
The program is able to define which car park has statically more availability and calculate 
the distance of the car park from the position entered by the user.
All functions used have been validated and tested, and handled with exceptions.
Furthermore, the program is divided into modules to make the entire code more understandable."""

__author__ = "Greta Gasparini"

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
    validate_latitude, validate_longitude, validate_hour, validate_parking_choice, \
        validate_format_image
#Import file that contains Point class.
from classes.point_class import Point

def main():
    """Function that provides information on parking in Bologna."""
    print("This code is used to get informations about parking lots in Bologna.")
    # Load dataset.
    dictionary = None
    while dictionary is None:
        user_choice = input("Do you want to open the dataset from online or local? ")
        # Code to open dataset from url (online).
        if user_choice.lower() == 'online' or user_choice.lower() == "o":
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
    print("The graph has been closed.")

    # Save a .csv file of results
    print("To save a .csv of results, please choose the file name and the delimiter.")

    # User choice of .csv file name.
    while True:
        csv_output_name_file = input("Choose the name of the CSV file:")
        try:
            validate_file_name(csv_output_name_file)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # User choice of .csv delimiter
    while True:
        delimiter = input("Choose the CSV file delimiter: ")
        try:
            validate_delimiter(delimiter)
            break
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
        except TypeError as typeerr:
            print(f"The error is: {typeerr}.")
        except ValueError as value:
            print(f"The error is: {value}.")

    # User choice of parking.
    print("Choose the desired parking lot: ")
    for i, parking in enumerate(parking_list):
        print(f"Write {i} for parking {parking.get_name()}")
    parking_choice_int = None
    while parking_choice_int is None:
        try:
            parking_choice_str = input("The chosen parking lot is: ")
            parking_choice_int = validate_parking_choice(parking_choice_str)
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
                                                                parking_list[parking_choice_int])
    generate_figure_and_plot_for_day(free_parking_for_day, chosen_day_int, \
                                     img_output_name_file, img_format)
    print("The graph has been closed.")

    # Save a .csv file of results
    print("To save a .csv of results, please choose the file name and the delimiter.")

    # User choice of .csv file name.
    while True:
        csv_output_name_file = input("Choose the name of the CSV file: ")
        try:
            validate_file_name(csv_output_name_file)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # User choice of .csv delimiter
    while True:
        delimiter = input("Choose the CSV file delimiter: ")
        try:
            validate_delimiter(delimiter)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}")

    # Save a .csv file.
    export_csv(free_parking_for_day, csv_output_name_file, parking_list[parking_choice_int], \
               chosen_day_int, delimiter)

    # Have the user enter their location, in terms of latitude and longitude.
    print("Please insert your latitude and longitude, to calculate the best parking.")

    # User choice of latitude.
    while True:
        user_latitude_str = input("Insert your latitude: ")
        try:
            user_latitude_float = validate_latitude(user_latitude_str)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")

    # User choice of longitude.
    while True:
        user_longitude_str = input("Insert your longitude: ")
        try:
            user_longitude_float = validate_longitude(user_longitude_str)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")
    user_point = Point(user_latitude_float, user_longitude_float)

    # Ask the user to enter the month and time slot they want to go to.
    print("Please insert the month and time slot you want to go. ")

    # User choice of month.
    while True:
        chosen_month_str = input("Indicate the month: ")
        try:
            chosen_month_int = validate_month(chosen_month_str)
            break
        except TypeError as typeerr:
            print(f"Is required a int value of month, "
                  f"the error is: {typeerr}.")
        except ValueError as value:
            print(f"The error is: {value}.")

    # User choice of hour.
    while True:
        chosen_hour_str = input("Indicate the hour: ")
        try:
            chosen_hour_int = validate_hour(chosen_hour_str)
            break
        except TypeError as typeerr:
            print(f"The error is: {typeerr}.")
        except ValueError as value:
            print(f"The error is: {value}.")

    # Find the percentage of free parking spaces in the chosen month and hour for all parking lots.
    best_park = None
    for park in parking_list:
        if best_park is None:
            best_park = park
        else:
            if generate_free_parks_in_hours_for_month(chosen_month_int, park)[chosen_hour_int] > \
                generate_free_parks_in_hours_for_month(chosen_month_int,best_park)[chosen_hour_int]:
                best_park = park

    # Calculate the distance between the user and the best parking lot.
    distance = user_point.get_distance_from_this_point(best_park.get_point())
    print(f"The best parking lot is {best_park.get_name()} with "
          f"{generate_free_parks_in_hours_for_month(chosen_month_int,best_park)[chosen_hour_int]}% "
          f"of free parking spaces that is {distance} m from you.")

if __name__ == "__main__":
    main()
