"""This module is used to test validation functions."""

import unittest             # Library used to test functions.
                            # It provides a rich set of tools for constructing and running tests.
from utils.validations import validate_latitude, validate_longitude   # Python file from which import the classes to test

class ValidationTest(unittest.TestCase):
    """validation test"""
    def test_lat(self):
        """validate lat"""
        self.assertTrue(validate_latitude(43.1))
        self.assertFalse(validate_latitude("pippo"))
        self.assertFalse(validate_latitude(1000.0))
    def test_lon(self):
        """validate lon"""
        self.assertTrue(validate_longitude(55.1))
        self.assertFalse(validate_longitude("ciao"))
        self.assertFalse(validate_longitude(1000.0))

if __name__ == "__main__":
    unittest.main(verbosity=2)