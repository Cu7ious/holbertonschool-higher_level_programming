#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""

    if len(matrix[0]) is 0:
        print("");

    for row in matrix:
        for el in row:
            if row[len(row) - 1] is el:
                print("{:d}".format(el))
            else:
                print("{:d} ".format(el), end="")
