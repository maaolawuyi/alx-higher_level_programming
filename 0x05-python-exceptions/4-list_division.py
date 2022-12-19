#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = [0] * list_length
    for i in range(list_length):
        try:
            list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("Division by 0")
        except TypeError:
            print("Wrong type")
        except IndexError:
            print("Out of range")
        finally:
            pass
    return list
