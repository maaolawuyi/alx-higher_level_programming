#!/usr/bin/python3
""" Module that contains a function that returns the number of lines
    of a text file
"""


def number_of_lines(filename=""):
    """ Function that reads from a file and prints its number of lines

    Args:
        
        filename: filename

    Raises
        Exception: when the file can be opene
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        n_lines = 0
        for i in range(len(data)):
            if data[i] == "\n":
                n_lines += 1
        return n_lines
