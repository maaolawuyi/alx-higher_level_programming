#!/usr/bin/python3
""" Module that contains a function that reads n lines of a text file
"""

def read_lines(filename="", nb_lines=0):
    """ Function that reads from a file and prints its number of lines

    Args:
        filename: filename
        nb_lines: number of lines to print

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for i in range(nb_lines):
                print(file.readline(), end="")

