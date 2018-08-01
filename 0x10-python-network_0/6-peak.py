#!/usr/bin/python3
def find_peak(list_of_integers):
    """
        Finds a peak in a list of unsorted integers
    """
    if list_of_integers is None or list_of_integers == []:
        return

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2

    if len(list_of_integers) != mid + 1:
        if list_of_integers[mid - 1] <= list_of_integers[mid] and \
                list_of_integers[mid + 1] <= list_of_integers[mid]:
            return list_of_integers[mid]
    else:
        if list_of_integers[mid - 1] <= list_of_integers[mid]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid - 1]

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return find_peak(list_of_integers[:mid])
