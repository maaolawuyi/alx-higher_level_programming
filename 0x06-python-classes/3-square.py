#!/usr/bin/python3
class Square:
    """ A class that defines a square by its size

    """
    def __init__(self, size=0):
        """ A method o initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A method that retur the square root of the oject
        """
        return (self.__size ** 2)
