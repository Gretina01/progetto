import datetime

class Detection():
    def __init__(self, timestamp: (int) = "", free_spaces: (int, float) = "", busy_spaces: (int, float) = "", total_spaces: (int) = "", occupation: (float) = ""):
        self.set_datetime(timestamp)
        self.set_free_spaces(free_spaces)
        self.set_busy_spaces(busy_spaces)
        self.set_total_spaces(total_spaces)
        self.set_occupation(occupation)

    def set_datetime(self, timestamp):
        self._datetime = datetime.datetime.fromtimestamp(timestamp)

    def set_free_spaces(self, free_spaces):
        self._free_spaces = free_spaces
    
    def set_busy_spaces(self, busy_spaces):
        self._busy_spaces = busy_spaces
    
    def set_total_spaces(self, total_spaces):
        self._total_spaces = total_spaces

    def set_occupation(self, occupation):
        self._occupation = occupation

    def get_datetime(self):
        return self._datetime

    def get_free_spaces(self):
        return self._free_spaces
