#!/usr/bin/python3
class Square:
    """A class that define the square by its size
    """
    def __init__(self, size=0):
        '''A method to initialise the square object
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''A method that return the square root of the object
        '''
        return (self.__size ** 2)

    @property
    def size(self):
        '''Method to set the size valu of the square object
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
