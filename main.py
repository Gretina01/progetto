""""""

__author__ = "Greta Gasparini"

# The re built-in package can be used to check whether a string contains the
# specified search pattern.
import re
# Python file that contains functions that allows to store the dataset.
from utils.load_convert_function import get_data_from_url, get_data_from_local, \
    generate_parking_list
# Python file that contains function that allows to generate plot.
from utils.plot_function import generate_free_parks_in_hours, generate_figure
# Python file that contains function that allows to export results in a .csv file.
from utils.export_csv_function import export_csv
# Import a python file containing validations function.
from utils.validations import validate_file_name, validate_delimiter, validate_month

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
    while True:
        chosen_month = int(input("Indicate the month for which you want to see availability: "))
        try:
            validate_month(chosen_month)
            break
        except TypeError as typeerr:
            print(f"Is required a int value of month, \
                                    the error is: {typeerr}.")
        except ValueError as value:
            print(f"The error is: {value}.")

    # User choice of parking.
    print("Choose the desired parking lot: ")
    for i, parking in enumerate(parking_list):
        print(f"Write {i} for parking {parking.get_name()}")
    while True:
        try:
            parking_choice = int(input("The chosen parking lot is: "))
            break
        except TypeError as typeerr:
            print(f"Is required a int value of month, \
                                    the error is {typeerr}")
        except ValueError as value:
            print(f"The error is: {value}.")

    # Generate the plot.
    print("The required graph is: ")
    # User choice of image name.
    img_output_name_file = input("Choose the image file name: ")
    # User choice of image format name.
    img_format = input("Choose the image file format: ")
    free_parking = generate_free_parks_in_hours(chosen_month, parking_list[parking_choice])
    generate_figure(free_parking, chosen_month, img_output_name_file, img_format)

    # Save an image of plot.
    print("To save an image of graph, please choose the image name and format.")


    #show_plot(fig)
    #img_output_name_file = input("Scegli il nome del file immagine: ")
    #img_format = input("Scegli il formato del file immagine: ")
    #save_plot(fig, img_output_name_file, img_format)

    # Save a .csv file of results
    print("To save a .csv of results, please choose the file name and the delimiter.")

    # User choice of image name.
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
    export_csv(free_parking, csv_output_name_file, parking_list[parking_choice], \
               chosen_month, delimiter)

if __name__ == "__main__":
    main()
