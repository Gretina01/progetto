"""This module contains graphic functions."""

# The datetime module supplies classes to work with date and time. These classes provide a number
# of functions to deal with dates, times, and time intervals.
from datetime import datetime
# Library used to create plot.
import matplotlib.pyplot as plt
# File Python that contains parking class.
from classes.parking_class import Parking
# Import a python file containing validations function.
from utils.validations import validate_free_spaces_by_time_slot, \
                        validate_file_name, validate_format_image
# File python that contains month and day classes.
from constants.calendar import Month, Day

# Define a function that creates a bar graph based on the average number of free spaces
# in % and the time slots in a month of your choice.
def generate_free_parks_in_hours_for_month(month: int, parking: Parking):
    """Function that creates a plot based on the chosen month."""
    # Extrapolate the months.
    months = [data.month for data in [datetime.strptime(couple[0], "%Y-%m-%d %H:%M:%S%z") \
                                      for couple in parking.get_detections_list()]]

    # Select the pairs for the chosen month.
    month_couples = [couple for couple, choose_month in zip(parking.get_detections_list(), \
                                                  months) if choose_month == month]

    # Extrapolate the time slots.
    hours = [data.hour for data in [datetime.strptime(couple[0], "%Y-%m-%d %H:%M:%S%z") \
                                    for couple in month_couples]]

    # Initialize a list to store occupied spaces for each time slot.
    occupied_spaces_by_time_slots = [[] for _ in range(24)]

    # Populate the list with occupied spaces for each time slot.
    for couple, hour in zip(month_couples, hours):
        occupied_spaces_by_time_slots[hour].append(couple)

    # Calculate the average free spaces for each time slot.
    avg_free_spaces_by_time_slot = []
    for hour in range(24):
        count = 0
        sum_parking = 0
        for detection in occupied_spaces_by_time_slots[hour]:
            sum_parking += (parking.get_total_spaces() - detection[1])
            count += 1
        if count == 0:
            avg = 0
        else:
            avg = sum_parking / count
        avg_free_spaces_by_time_slot.append((avg/parking.get_total_spaces())*100)

    return avg_free_spaces_by_time_slot

# Define a function that creates a bar graph based on the average number of free spaces
# in % and the time slots in a week day of your choice.
def generate_free_parks_in_hours_for_day(day: int, parking: Parking):
    """Function that creates a plot based on the chosen month."""
    # Extrapolate the days.
    days = [data.day for data in [datetime.strptime(couple[0], "%Y-%m-%d %H:%M:%S%z")\
                                  for couple in parking.get_detections_list()]]

    # Select the pairs for the chosen day.
    day_couples = [couple for couple, choose_day in zip(parking.get_detections_list(), days) \
                   if choose_day == day]

    # Extrapolate the time slots.
    hours = [data.hour for data in [datetime.strptime(couple[0], "%Y-%m-%d %H:%M:%S%z") \
                                    for couple in day_couples]]

    # Initialize a list to store occupied spaces for each time slot.
    occupied_spaces_by_time_slots = [[] for _ in range(24)]

    # Populate the list with occupied spaces for each time slot.
    for couple, hour in zip(day_couples, hours):
        occupied_spaces_by_time_slots[hour].append(couple)

    # Calculate the average free spaces for each time slot.
    avg_free_spaces_by_time_slot = []
    for hour in range(24):
        count = 0
        sum_parking = 0
        for detection in occupied_spaces_by_time_slots[hour]:
            sum_parking += (parking.get_total_spaces() - detection[1])
            count += 1
        if count == 0:
            avg = 0
        else:
            avg = sum_parking / count
        avg_free_spaces_by_time_slot.append((avg/parking.get_total_spaces())*100)

    return avg_free_spaces_by_time_slot

# This function generate the figure and plot for the chosen month.
def generate_figure_and_plot_for_month(avg_free_spaces_by_time_slot: list, month: int, \
                                       output_name_file: str, format_image: str):
    """Function that creates a plot based on the chosen month."""
    try:
        validate_free_spaces_by_time_slot(avg_free_spaces_by_time_slot)
    except ValueError as value:
        print(f"The error is: {value}.")
    except TypeError as typeerr:
        print(f"The error is: {typeerr}.")
    else:
        plt.figure(figsize = (15, 10))
        plt.bar(range(24), avg_free_spaces_by_time_slot, color ='maroon',
                width = 0.4)

        # Annotate each bar with its value.
        for i, value in enumerate(avg_free_spaces_by_time_slot):
            plt.text(i, value, f"{value:.2f}%", ha='center', va='bottom')
            plt.title(f"Number of free parking spaces per time slot in the "
                      f"month of {Month(month).name}")
            plt.ylabel("Number of free spaces")
            plt.xlabel("Time slots")
            plt.xticks(range(24))
        try:
            validate_file_name(output_name_file)
            validate_format_image(format_image)
        except ValueError as value:
            print(value)
        except TypeError as value:
            print(value)
        else:
            plt.savefig(f"outputs/{output_name_file}.{format_image}", format=format_image)
        plt.show()

# This function generate the figure and plot for the chosen day.
def generate_figure_and_plot_for_day(avg_free_spaces_by_time_slot: list, day: int, \
                                     output_name_file: str, format_image: str):
    """Function that creates a plot based on the chosen day."""
    try:
        validate_free_spaces_by_time_slot(avg_free_spaces_by_time_slot)
    except ValueError as value:
        print(f"The error is: {value}.")
    except TypeError as typeerr:
        print(f"The error is: {typeerr}.")
    else:
        plt.figure(figsize = (15, 10))
        plt.bar(range(24), avg_free_spaces_by_time_slot, color ='maroon',
            width = 0.4)

        for i, value in enumerate(avg_free_spaces_by_time_slot):
            plt.text(i, value, f"{value:.2f}%", ha='center', va='bottom')
            plt.title(f"Number of free parking spaces per time slot in "
                      f"the day of {Day(day).name}")
            plt.ylabel("Number of free spaces")
            plt.xlabel("Time slots")
            plt.xticks(range(24))

        try:
            validate_file_name(output_name_file)
            validate_format_image(format_image)
        except ValueError as value:
            print(value)
        except TypeError as value:
            print(value)
        else:
            plt.savefig(f"outputs/{output_name_file}.{format_image}", format=format_image)
        plt.show()
        