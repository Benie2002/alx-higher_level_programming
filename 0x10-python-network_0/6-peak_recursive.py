#!/usr/bin/python3

"""function finds the peak of the list
This approach has a case that it cannot handle 'maximum recursion depth exceed in comparison error'
"""


def find_peak_recursive(list_of_integers, low, high):
    """finds peak recursively

    args:
        list_of_integers (list): list containing unsorted int
        low (int): starting point of list
        high (int): ending point of list

    returns: the value
    """
    if low == high:
        return list_of_integers[low]

    mid = (low + high) // 2

    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak_recursive(list_of_integers, low, mid)

    else:
        return find_peak_recursive(list_of_integers, mid, high)


def find_peak(list_of_integers):
    """Finds peak in an unsorted list
    """

    if not list_of_integers:
        return None

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
