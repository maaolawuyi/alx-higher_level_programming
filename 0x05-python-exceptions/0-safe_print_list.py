#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0;
    for i in my_list[:x]:
        try:
            print("{}".format(i), end="")
            count += 1
        except IndexError:
            print()
    print()
    return count
