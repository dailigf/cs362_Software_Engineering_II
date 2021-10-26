#!/bin/env/python

def avgList(list):
    """
    Averages the elements in a list
    :arg list: list of numbers
    :returns: the average of the list
    """

    sum = 0
    for num in list:
        sum = sum + num
    return int(sum) / len(list)

