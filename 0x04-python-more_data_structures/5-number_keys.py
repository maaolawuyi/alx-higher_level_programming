#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    new_list = list(a_dictionary.keys())

    for i in new_list:
        num += 1

    return (num)
