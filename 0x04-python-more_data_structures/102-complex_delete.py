#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = list(a_dictionary.keys())

    for value_dic in new_list:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
