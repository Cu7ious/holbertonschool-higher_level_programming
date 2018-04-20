#!/usr/bin/python3


def weight_average(my_list=[]):
    """Returns the weighted average of all integers
        inside tuple (<score>, <weight>)."""

    if len(my_list) is 0:
        return 0

    sum_of_mul = 0
    sum_of_sec = 0

    for tup in my_list:
        sum_of_mul += tup[0] * tup[1]
        sum_of_sec += tup[1]

    return sum_of_mul / sum_of_sec
