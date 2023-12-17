"""This module is used to test class.
To run the tests put in debug configuration: module. The module name is test.class_test."""

import unittest # Library used to test functions.
                # It provides a rich set of tools for constructing and running tests.
from classes.point_class import Point # Python file from which import the point class to test
from classes.parking_class import Parking # Python file from which import the parking class to test

# Class that test point class.
class PointTestClass(unittest.TestCase):
    """Test class for point class"""
    # Define the setup for the test.
    def setUp(self):
        """Setup of test."""
        self._point = Point(43.0, 13.0)

    # Define a function for test the latitude getter.
    def test_get_latitude(self):
        """Test function for latitude getter."""
        self.assertEqual(self._point.get_latitude(), 43.0)

    # Define a function for test the longitude getter.
    def test_get_longitude(self):
        """Test function for longitude getter."""
        self.assertEqual(self._point.get_longitude(), 13.0)

# Class that test parking class.
class ParkingTestClass(unittest.TestCase):
    """Test class for parking class"""
    # Define the setup for the test.
    def setUp(self):
        """Setup of test."""
        self._point = Parking(50.5, 29.0, "Riva Reno", "87e4078d-36d2-4f1a-b088-92483e0cbf90", 470)

    # Define a function for test the name getter.
    def test_get_name(self):
        """Test function for name getter."""
        self.assertEqual(self._point.get_name(), "Riva Reno")

    # Define a funtion for test the parking guid getter.
    def test_get_parking_guid(self):
        """Test function for parking guid getter."""
        self.assertEqual(self._point.get_parking_guid(), "87e4078d-36d2-4f1a-b088-92483e0cbf90")

    # Define a function for test the total spaces getter.
    def test_get_total_spaces(self):
        """Test function for total spaces getter."""
        self.assertEqual(self._point.get_total_spaces(), 470)

    print("All tests passed.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
