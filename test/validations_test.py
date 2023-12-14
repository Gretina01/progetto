"""This module is used to test validation functions."""

import unittest             # Library used to test functions.
                            # It provides a rich set of tools for constructing and running tests.
from utils.validations import validate_latitude, validate_longitude, validate_name, validate_spaces, validate_datetime, validate_format_image   # Python file from which import the classes to test

# Class that test validations function.
class ValidationTest(unittest.TestCase):
    """Define a test class for validations function. """
    # Define a function that tesy the validate_latitude function.
    def test_validate_latitude(self):
        """Test function for validate latitude."""
        self.assertTrue(validate_latitude(43.1))
        self.assertFalse(validate_latitude("nonumber"))
        self.assertFalse(validate_latitude(1000.0))
        with self.assertRaises(ValueError):
            validate_latitude("")
        with self.assertRaises(ValueError):
            validate_latitude(None)

    # Define a function that test the validate_longitude function.
    def test_validate_longitude(self):
        """Test function for validate longitude."""
        self.assertTrue(validate_longitude(55.1))
        self.assertFalse(validate_longitude("hello"))
        self.assertFalse(validate_longitude(-1000.0))
        with self.assertRaises(ValueError):
            validate_longitude(None)
        with self.assertRaises(ValueError):
            validate_longitude("")

    # Define a function that test the validate_name function.
    def test_validate_name(self):
        """Test function for validate name."""
        self.assertTrue(validate_name("hello python"))
        self.assertFalse(validate_longitude(-20.0))
        with self.assertRaises(ValueError):
            validate_name(None)
        with self.assertRaises(ValueError):
            validate_name("")

    # Define a function that test the validate_spaces function.
    def test_validate_spaces(self):
        """Test function for validate spaces."""
        self.assertFalse(validate_spaces("hello world", 200))
        self.assertFalse(validate_spaces(-20.0, 200))
        self.assertTrue(validate_spaces(35, 200))
        self.assertFalse(validate_spaces(400, 200))
        with self.assertRaises(ValueError):
            validate_spaces(None, 200)
        with self.assertRaises(ValueError):
            validate_spaces("", 200)

    # Define a function that test the validate_datetime function.
    def test_validate_datetime(self):
        """Test function for validate datetime."""
        actual_value = "2023-10-25 14:15:23+00:00"
        self.assertTrue(validate_datetime(actual_value, "%Y-%m-%d %H:%M:%S+%z"))
        actual_value_1 = "23-10-25 14:15:23+00:00"
        self.assertFalse(validate_datetime(actual_value_1, "%Y-%m-%d %H:%M:%S+%z"))
        with self.assertRaises(ValueError):
            validate_datetime("")
        with self.assertRaises(ValueError):
            validate_datetime(None)
    
    def test_validate_format_image(self):
        """Test function for validate format image"""
        self.assertTrue(validate_format_image("image", "jpeg", "image"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
