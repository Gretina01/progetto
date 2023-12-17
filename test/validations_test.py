"""This module is used to test validation functions.
To run the tests put in debug configuration: module. The module name is test.validations_test."""

# The datetime module supplies classes to work with date and time. These classes provide a number
# of functions to deal with dates, times, and time intervals.
from datetime import datetime
# The re built-in package can be used to check whether a string contains the
# specified search pattern.
import re
import unittest             # Library used to test functions.
                            # It provides a rich set of tools for constructing and running tests.
# Python file from which import the classes to test.
from utils.validations import validate_latitude, validate_longitude, validate_name, \
                                validate_spaces, validate_total_spaces, validate_parking_guid, \
                                validate_datetime, validate_month, validate_hour, \
                                validate_format_image, validate_delimiter, validate_file_name
# Python file from which import the custom exception for test the image format.
from utils.custom_exception import InvalidFormatImage

# Class that test validations function.
class ValidationTest(unittest.TestCase):
    """Define a test class for validations function. """
    # Define a function that test the validate_latitude function.
    def test_validate_latitude(self):
        """Test function for validate latitude."""
        with self.assertRaises(ValueError):
            validate_latitude("")
        with self.assertRaises(ValueError):
            validate_latitude(None)
        with self.assertRaises(TypeError):
            validate_latitude("nonumber")
        with self.assertRaises(ValueError):
            validate_latitude(1000.0)

    # Define a function that test the validate_longitude function.
    def test_validate_longitude(self):
        """Test function for validate longitude."""
        with self.assertRaises(ValueError):
            validate_longitude(None)
        with self.assertRaises(ValueError):
            validate_longitude("")
        with self.assertRaises(TypeError):
            validate_longitude("nonumber")
        with self.assertRaises(ValueError):
            validate_longitude(-1000.0)

    # Define a function that test the validate_name function.
    def test_validate_name(self):
        """Test function for validate name."""
        with self.assertRaises(ValueError):
            validate_name(None)
        with self.assertRaises(ValueError):
            validate_name("")
        with self.assertRaises(TypeError):
            validate_name(-20.0)

    # Define a function that test the validate_file_name function.
    def test_validate_file_name_function(self):
        """Test function for validate file name."""
        with self.assertRaises(re.error):
            validate_file_name("hello?")

    # Define a function that test the validate_spaces function.
    def test_validate_spaces(self):
        """Test function for validate spaces."""
        with self.assertRaises(ValueError):
            validate_spaces(None, 200)
        with self.assertRaises(ValueError):
            validate_spaces("", 200)
        with self.assertRaises(TypeError):
            validate_spaces("hello world", 200)
        with self.assertRaises(ValueError):
            validate_spaces(-20.0, 200)

    # Define a function that test the validate_total_space function.
    def test_validate_total_spaces(self):
        """Test function for validate total spaces."""
        with self.assertRaises(ValueError):
            validate_total_spaces(None)
        with self.assertRaises(ValueError):
            validate_total_spaces("")
        with self.assertRaises(TypeError):
            validate_total_spaces("hello world")

    # Define a funtion that test the validate_parking_guid function.
    def test_validate_parking_guid(self):
        """Test function for validates parking guid."""
        with self.assertRaises(ValueError):
            validate_parking_guid(None)
        with self.assertRaises(ValueError):
            validate_parking_guid("")
        with self.assertRaises(TypeError):
            validate_parking_guid(123)

    # Define a function that test the validate_datetime function.
    def test_validate_datetime(self):
        """Test function for validate datetime."""
        with self.assertRaises(ValueError):
            validate_datetime(datetime(10000, 13, 32, 24, 60, 60))
        with self.assertRaises(ValueError):
            validate_datetime(datetime.strptime("2023-12-17 12:30:45X", "%Y-%m-%d %H:%M:%S"))
        with self.assertRaises(ValueError):
            validate_datetime(datetime.strptime("", "%Y-%m-%d %H:%M:%S"))

    # Define a function that test the validate_month function.
    def test_validate_month(self):
        """Test function for validate month."""
        with self.assertRaises(ValueError):
            validate_month(None)
        with self.assertRaises(ValueError):
            validate_month("")
        with self.assertRaises(TypeError):
            validate_month("hello")
        with self.assertRaises(ValueError):
            validate_month(25)

    # Define a function that test the validate_hour function.
    def test_validate_hour(self):
        """Test function for validate hour."""
        with self.assertRaises(ValueError):
            validate_hour(None)
        with self.assertRaises(ValueError):
            validate_hour("")
        with self.assertRaises(TypeError):
            validate_hour("hello")
        with self.assertRaises(ValueError):
            validate_hour(30)

    # Define a function that test the validate_format_image function.
    def test_validate_format_image(self):
        """Test function for validate format image"""
        with self.assertRaises(InvalidFormatImage):
            validate_format_image("csv")

    # Define a function that test the validate_delimiter function.
    def test_validate_delimiter(self):
        """Test function for validate delimiter."""
        with self.assertRaises(ValueError):
            validate_delimiter(".")
        with self.assertRaises(ValueError):
            validate_delimiter(None)

    print("All tests passed.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
