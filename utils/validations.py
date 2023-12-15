"""This module contains all the functions that must be validated. 
The functions in which the user enters the value are validated"""

from datetime import datetime
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
            raise TypeError(f"Is required a int value of parking spaces \
                                    it's provided {type(spaces)}")
        if 0 > spaces > total_spaces:
            raise ValueError("""Invalid value of spaces compared to total spaces. \
                                    The value of occuped spaces must be between 0 and \
                                    the maximum capacity of the parking.""")
    else:
        raise ValueError("No value was provided.")

# The validate_datetime function validates if the format of the date and time entered is correct.
def validate_datetime(datetime_string, format_datetime = "%Y-%m-%d %H:%M:%S"):
    """Function that validates the date and time.
    The value entered must respect the format.
    Otherwise, including if no value is provided, an exception is raised."""
    if datetime_string != "" and datetime_string is not None:
        """# Try to convert the string to a datetime object using the specified format.
        datetime_string_input = datetime.fromtimestamp(datetime_string)
        if datetime_string_input != datetime_string_input.strftime(format_datetime):
            raise ValueError("Non ci sto capendo un cazzo")"""
        """# Presumendo che datetime_string sia nel formato di una stringa di timestamp
        timestamp = float(datetime_string)
        datetime_string_input = datetime.fromtimestamp(timestamp)
        
        # Formatta datetime_string_input usando il formato specificato
        formatted_datetime_string_input = datetime_string_input.strftime(format_datetime)

        # Confronta la stringa originale con la sua versione formattata
        if datetime_string != formatted_datetime_string_input:
            raise ValueError("Non ci sto capendo un cazzo")"""
         # Converti la stringa in un oggetto datetime
        datetime_input = datetime.fromtimestamp(float(datetime_string))

        # Formatta l'oggetto datetime usando il formato specificato
        formatted_datetime_input = datetime_input.strftime(format_datetime)

        # Confronta la stringa originale con la sua versione formattata
        if datetime_string != formatted_datetime_input:
            raise ValueError("La stringa non corrisponde al formato desiderato")
        
    else:
        raise ValueError("No value was provided.")
    """  # Check if the input string has the same format.
        if datetime_string_input.strftime(format_datetime) != datetime_string:
            raise ValueError("The string entered does not respect the format.")
        

        dt_object = datetime.fromtimestamp(timestamp)
        # Formatta l'oggetto datetime come una stringa nel formato desiderato
        stringa_formattata = dt_object.strftime(formato)
        return stringa_formattata
    

        # Check if the year is within range 0001 and 9999.
        if 1 > datetime_string_input.year > 9999:
            raise ValueError("The year value is not within range.")
        # Check if the month is within range 01 and 12.
        if 1 > datetime_string_input.month > 12:
            raise ValueError("The month value is not within range.")
        # Check if the day is within range 01 and 31.
        if 1 > datetime_string_input.day > 31:
            raise ValueError("The day value is not within range.")
        # Check if the hour is within range 00 and 23.
        if 00 > datetime_string_input.hour > 23:
            raise ValueError("The hour value is not within range.")
        # Check if the minute is within range 00 and 59.
        if 00 > datetime_string_input.minute > 59:
            raise ValueError("The minute value is not within range.")
        # Check if the second is within range 00 and 59.
        if 00 > datetime_string_input.second > 59:
            raise ValueError("The second value is not within range.")"""

# The validate_format_image function validated if the chosen format is within the supported formats.
def validate_format_image(file_name, format_image, image):
    """Function that validates the format of an image.
    The format supported are jpg, jpeg, png, svg, pdf."""
    supported_format_image = ['jpg', 'jpeg', 'png', 'svg', 'pdf']
    if format_image.lower() not in supported_format_image:
        raise InvalidFormatImage(f"{format_image} is an unsupported format. The formats allowed \
                        are: jpg, jpeg, png, svg, pdf.")
    if format_image.lower() == 'jpg' or format_image.lower() == 'jpeg':
        image.save(f"{file_name}.jpg", "JPEG")
    elif format_image.lower() == 'png':
        image.save(f"{file_name}.png", "PNG")
    elif format_image.lower() == 'svg':
        with open(f"{file_name}.svg", "w") as f:
            f.write(image.tostring())
    elif format_image.lower() == 'pdf':
        image.save(f"{file_name}.pdf", "PDF", resolution=100.0)
