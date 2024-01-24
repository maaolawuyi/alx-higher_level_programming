#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    num1 = 0

    for ave in my_list:
        num += ave[0] * ave[1]
        num1 += ave[1]

    return (num / num1)
