#!/usr/bin/python3
def uniq_add(my_list=[]):
    element = set(my_list)
    num = 0

    for i in element:
        num += i

    return (num)
