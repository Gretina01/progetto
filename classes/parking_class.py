from point_class import Point

class Parking(Point):
    """"""
    def __init__(self, latitude = "", longitude = "", parking_name = "", parking_spaces = ""):
        """"""
        super().__init__(latitude, longitude)
        self.set_name(parking_name)
        self.set_spaces(parking_spaces)
    def set_name(self, parking_name):
        """"""
        if not isinstance(parking_name, str):
            raise TypeError(f"")
        self._name = parking_name
    def set_spaces(self, parking_spaces):
        """"""
        if not isinstance(parking_spaces, int):
            raise TypeError(f"")
        self._spaces = parking_spaces
 