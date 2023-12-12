"""This module is used to test validation functions."""

import unittest             # Library used to test functions.
                            # It provides a rich set of tools for constructing and running tests.
from utils.validations import validate_latitude, validate_longitude, validate_name, validate_spaces   # Python file from which import the classes to test

class ValidationTest(unittest.TestCase):
    """?????"""
    #
    def test_latitude(self):
        """?????"""
        self.assertTrue(validate_latitude(43.1))
        self.assertFalse(validate_latitude("nonumber"))
        self.assertFalse(validate_latitude(1000.0))
        self.assertRaises(TypeError)
    #
    def test_lon(self):
        """validate lon"""
        self.assertTrue(validate_longitude(55.1))
        self.assertFalse(validate_longitude("ciao"))
        self.assertFalse(validate_longitude(1000.0))

if __name__ == "__main__":
    unittest.main(verbosity=2)