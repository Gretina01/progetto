"""This module contains all the functions that must be validated. 
The functions in which the user enters the value are validated"""

# The validate_latitude function checks whether the latitude value inserted 
# is within the range -90 and +90 degrees and whether it is a float or int. 
# Also handles the empty string or None value condition.
def validate_latitude(latitude):
    """Function that validates the latitude. 
    The value entered must be a float or int and must be within the range.
    Otherwise, including if no value is provided, an exception is raised."""
    if latitude != "" and latitude != None:
        if not isinstance(latitude, (int, float)):
            raise TypeError(f"Is required a float or int value of latitude \
                            it's provided {type(latitude)}")
        if not abs(latitude) <= 90.0:
            raise ValueError(f"The latitude value is not within a valid range. \
                             Valid values are between -90 and +90 degrees. The value provided is {latitude}")
    # If the latitude value is not provided, an exception is raised.
    else:
        if latitude == "" or latitude == None:
            raise TypeError(f"No value was provided.")
    
# The validate_longitude function checks whether the longitude value inserted 
# is within the range -180 and +180 degrees and whether it is a float or int. 
# Also handles the empty string or None value condition.
def validate_longitude(longitude):
    """Function that validates the longitude. 
    The value entered must be a float or int and must be within the range.
    Otherwise, including if no value is provided, an exception is raised."""
    
    # If the longitude value is provided, check whether it is a float or int and that it is within range.
    if longitude != "" and longitude != None:
        if not isinstance(longitude, (int, float)):
            raise TypeError(f"Is required a float or int value of longitude \
                            it's provided {type(longitude)}")
        if not abs(longitude) <= 180.0:
            raise ValueError(f"The longitude value is not within a valid range. \
                             Valid values are between -180 and +180 degrees. The value provided is {longitude}")
    # If the longitude value is not provided, an exception is raised.
    else:
        if longitude == "" or longitude == None:
            raise TypeError(f"No value was provided.")

# The validate_name function validates whether the name entered is a string.
def validate_name(name):
    if not isinstance(name, str):
        raise TypeError(f"Is required a string \
                                it's provided {type(name)}")

# The validate_spaces function validates whether the spaces entered is a int.
def validate_spaces(spaces):
    if not isinstance(spaces, int):
        raise TypeError(f"Is required a int value of parking spaces \
                                it's provided {type(spaces)}")
