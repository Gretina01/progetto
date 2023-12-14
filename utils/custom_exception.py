"""In this module there is a class to manage a custom exception."""

# Class that define the custom exception regarding the not allowed format of an image.
class InvalidFormatImage(ValueError):
    """Class that raise an exception if the chosen format is unsupported. """
    def __init__(self, msg = "The chosen is not allowed."):
        """Constructor for exception class"""
        super().__init__(msg)
