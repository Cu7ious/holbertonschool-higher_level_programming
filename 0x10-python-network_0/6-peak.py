#!/usr/bin/env python3


def find_peak(list_of_integers):
    """
        Finds a peak in a list of unsorted integers
    """
    if not len(list_of_integers):
        return

    for idx, val in enumerate(list_of_integers):
        if idx > 0:
            if val < list_of_integers[idx-1]:
                if list_of_integers[idx-2] < list_of_integers[idx-1]:
                        return list_of_integers[idx-1]

    return max(list_of_integers)
