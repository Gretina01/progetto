"""This module contains all the functions that must be validated. 
The functions in which the user enters the value are validated"""

# The re built-in package can be used to check whether a string contains the
# specified search pattern.
import re
# The datetime module supplies classes to work with date and time. These classes provide a number
# of functions to deal with dates, times, and time intervals.
from datetime import datetime, timezone
# Python file from which import the custom exception for test the image format.
from utils.custom_exception import InvalidFormatImage

# The validate_latitude function checks whether the latitude value inserted
# is within the range -90 and +90 degrees and whether it is a float or int.
# Also handles the empty string or None value condition.
def validate_latitude(latitude):
    """Function that validates the latitude. 
    The value entered must be a float or int and must be within the range.
    Otherwise, including if no value is provided, an exception is raised."""
    if latitude != "" and latitude is not None:
        if not isinstance(latitude, (int, float)):
            raise TypeError(f"Is required a float or int value of latitude \
                            it's provided {type(latitude)}")
        if not abs(latitude) <= 90.0:
            raise ValueError(f"The latitude value is not within a valid range. \
                                Valid values are between -90 and +90 degrees. \
                                The value provided is {latitude}")
    # If the latitude value is not provided, an exception is raised.
    else:
        raise ValueError("No value was provided.")

# The validate_longitude function checks whether the longitude value inserted
# is within the range -180 and +180 degrees and whether it is a float or int.
# Also handles the empty string or None value condition.
def validate_longitude(longitude):
    """Function that validates the longitude. 
    The value entered must be a float or int and must be within the range.
    Otherwise, including if no value is provided, an exception is raised."""

    # If the longitude value is provided, check whether it is a float or int
    # and that it is within range.
    if longitude != "" and longitude is not None:
        if not isinstance(longitude, (int, float)):
            raise TypeError(f"Is required a float or int value of longitude \
                            it's provided {type(longitude)}")
        if not abs(longitude) <= 180.0:
            raise ValueError(f"The longitude value is not within a valid range. \
                                Valid values are between -180 and +180 degrees. \
                                The value provided is {longitude}")
    # If the longitude value is not provided, an exception is raised.
    else:
        raise ValueError("No value was provided.")

# The validate_name function validates whether the name entered is a string.
def validate_name(name):
    """Function that validates the name.
    The name entered must be a string.
    Otherwise, including if no value is provided, an exception is raised."""
    if name != "" and name is not None:
        if not isinstance(name, str):
            raise TypeError(f"Is required a string \
                                    it's provided {type(name)}")
    else:
        raise ValueError("No value was provided.")

# The validate_spaces function validates whether the spaces entered is a int or float.
# Also validates if the spaces entered are consistent with the total spaces of a parking.
# The validate_spaces function validates whether the spaces entered is a int.
def validate_spaces(spaces, total_spaces):
    """Function that validates the spaces. 
    The value entered must be a float or int, and the value entered
    must be between 0 and the value of total spaces of a parking.
    Otherwise, including if no value is provided, an exception is raised."""
    if spaces != "" and spaces is not None:
        if not isinstance(spaces, (int,float)):
            raise TypeError(f"Is required a int or float value of parking spaces \
                                    it's provided {type(spaces)}")
        if not 0 <= spaces  and spaces <= total_spaces:
            raise ValueError("""Invalid value of spaces compared to total spaces. \
                                    The value of occuped spaces must be between 0 and \
                                    the maximum capacity of the parking.""")
    else:
        raise ValueError("No value was provided.")

# The validate_total_spaces function validates whether the total spaces is a int.
def validate_total_spaces(total_spaces):
    """Function that validates the total spaces. 
    The value entered must be a int.
    Otherwise, including if no value is provided, an exception is raised."""
    if total_spaces != "" and total_spaces is not None:
        if not isinstance(total_spaces, int):
            raise TypeError(f"Is required a int value of total parking spaces \
                                    it's provided {type(total_spaces)}")
    else:
        raise ValueError("No value was provided.")

# The validate_parking_guid function validates whether the parking guid is a string.
def validate_parking_guid(parkig_guid):
    """Function that validates the parking guid. 
    The value entered must be a string.
    Otherwise, including if no value is provided, an exception is raised."""
    if parkig_guid != "" and parkig_guid is not None:
        if not isinstance(parkig_guid, str):
            raise TypeError(f"Is required a int value of parking guid \
                                    it's provided {type(parkig_guid)}")
    else:
        raise ValueError("No value was provided.")


"""tzinfo=ZoneInfo("America/Los_Angeles")

def astimezone(self, tz):
    if self.tzinfo is tz:
        return self
    # Convert self to UTC, and attach the new time zone object.
    utc = (self - self.utcoffset()).replace(tzinfo=tz)
    # Convert from UTC to tz's local time.
    return tz.fromutc(utc)"""

# The validate_datetime function validates if the format of the date and time entered is correct.
def validate_datetime(datetime_obj, format_datetime = "%Y-%m-%d %H:%M:%S"):
    """Function that validates the date and time.
    The value entered must respect the format.
    Otherwise, including if no value is provided, an exception is raised."""
    # Convert datetime_obj from int to datetime object
    if isinstance(datetime_obj, int):
        datetime_obj = datetime.fromtimestamp(datetime_obj)
    # Convert the datetime object to a string.
    datetime_string = datetime_obj.strftime(format_datetime)
    if datetime_string != "" and datetime_string is not None:
        if not datetime.strptime(datetime_string, format_datetime):
            raise ValueError(f"Invalid datetime format. It should be in the format '{format_datetime}'")
        if 1 > datetime_obj.year > 9999:
            raise ValueError("The year value is not within range.")
        # Check if the month is within range 01 and 12.
        if 1 > datetime_obj.month > 12:
            raise ValueError("The month value is not within range.")
        # Check if the day is within range 01 and 31.
        if 1 > datetime_obj.day > 31:
            raise ValueError("The day value is not within range.")
        # Check if the hour is within range 00 and 23.
        if 00 > datetime_obj.hour > 23:
            raise ValueError("The hour value is not within range.")
        # Check if the minute is within range 00 and 59.
        if 00 > datetime_obj.minute > 59:
            raise ValueError("The minute value is not within range.")
        # Check if the second is within range 00 and 59.
        if 00 > datetime_obj.second > 59:
            raise ValueError("The second value is not within range.")
    else:
        raise ValueError("No value was provided.")

# The validate_month function validates if month entered is within the range.
def validate_month(month):
    """Function that validates the month.
    The value entered must be within range.
    Otherwise, including if no value is provided, an exception is raised."""
    if month != "" and month is not None:
        if not isinstance(month, (int)):
            raise TypeError(f"Is required a int value of month \
                                it's provided {type(month)}")
        if not 0 <= month <= 12:
            raise ValueError("The month entered must be within the range 0 - 12.")
    else:
        raise ValueError("No value was provided.")

# The validate_time function validates if hour and minutes entered is within the range.
def validate_hour(hour):
    """Function that validates the time.
    The value entered must be within range.
    Otherwise, including if no value is provided, an exception is raised."""
    if hour != "" and hour is not None:
        if not isinstance(hour, (int)):
            raise TypeError(f"Is required a int value of hour \
                                it's provided {type(hour)}")
        if not 0 <= hour <= 24:
            raise ValueError("The hour entered must be within the range 0 - 24.")
    else:
        raise ValueError("No value was provided.")

# The validate_format_image function validates if the chosen format is within the supported formats.
def validate_format_image(format_image):
    """Function that validates the format of an image.
    The format supported are jpg, jpeg, png, svg, pdf."""
    supported_format_image = ['jpg', 'jpeg', 'png', 'svg', 'pdf']
    if format_image.lower() not in supported_format_image:
        raise InvalidFormatImage(f"{format_image} is an unsupported format. The formats allowed \
                        are: jpg, jpeg, png, svg, pdf.")

# The validate_delimiter function validates if the chosen delimiter is allowed.
def validate_delimiter(delimiter):
    """Function that validates the delimiter for .csv file.
    The supported delimiter are ',', ';', '\t', ' '."""
    valid_delimiters = [',', ';', '\t', ' ']
    if delimiter is not None:
        if delimiter not in valid_delimiters:
            raise ValueError("The chosen delimiter is not allowed. \
                             The supported delimiter are ',', ';', '\t', ' '")
    else:
        raise ValueError("No value provided.")

# The validate_file_name function validates if the chosen file name is allowed.
def validate_file_name(name):
    """Function that validates the name.
    The name entered must be a string, and must not contain certain symbols.
    Otherwise, including if no value is provided, an exception is raised."""
    # Define a regex that matches a list of unwanted symbols.
    pattern = r'[^~"#%&*:<>?/\{|}]'
    if name != "" and name is not None:
        if not isinstance(name, str):
            raise TypeError(f"Is required a string \
                                    it's provided {type(name)}")
        # Check the file name for unwanted symbols.
        if not re.search(pattern, name):
            raise re.error(f"The name {name} contains unwanted symbols.", r'[^~"#%&*:<>?/\{|}]')
    else:
        raise ValueError("No value was provided.")

# The validate_free_spaces_by_time_slot validates if there is any detection of free spaces by time slot.
def validate_free_spaces_by_time_slot(avg_free_spaces_by_time_slot):
    """Function that validates if there are free spaces in time slot."""
    if not isinstance(avg_free_spaces_by_time_slot, list) or len(avg_free_spaces_by_time_slot) != 24:
        raise ValueError("Input must be a list of 24 elements")
    else:
        count_zero = 0
        for i in range(24):
            if avg_free_spaces_by_time_slot[i] == 0 or avg_free_spaces_by_time_slot[i] == 0.0:
                count_zero += 1
            if not isinstance(avg_free_spaces_by_time_slot[i], (float)):
                raise TypeError(f"Invalid type at index {i}")
            if not 0 <= avg_free_spaces_by_time_slot[i] <= 100:
                raise ValueError(f"Invalid value at index {i}")
        if count_zero == 24:
            raise ValueError("Ci sono troppe fasce orarie con mancanza di dati")
