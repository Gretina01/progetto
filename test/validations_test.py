"""This module is used to test validation functions."""

import unittest             # Library used to test functions.
                            # It provides a rich set of tools for constructing and running tests.
# Python file from which import the classes to test
from utils.validations import validate_latitude, validate_longitude, validate_name, \
                                validate_spaces, validate_datetime, validate_format_image
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
        with self.assertRaises(ValueError):
            validate_spaces(201, 200)

    # Define a function that test the validate_datetime function.
    def test_validate_datetime(self):
        """Test function for validate datetime."""
        """actual_value = "pippo"
        with self.assertRaises(ValueError):
            validate_datetime(actual_value, "%Y-%m-%d %H:%M:%S")"""
        """ actual_value_1 = "23-10-25 14:15:23"
        with self.assertRaises(ValueError):
            validate_datetime(actual_value_1, "%Y-%m-%d %H:%M:%S")"""
        with self.assertRaises(ValueError):
            validate_datetime("")
        with self.assertRaises(ValueError):
            validate_datetime(None)

    # Define a function that test the validate_format_image function.
    def test_validate_format_image(self):
        """Test function for validate format image"""
        with self.assertRaises(InvalidFormatImage):
            validate_format_image("csv")

    print("All tests passed.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
