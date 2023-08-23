#!usr/bin/python3

"""
Function that returns pascals triangle
"""


def pascal_triangle(M):
    """Returns a list of lists of integers representing the Pascal's triangle
    of n
    returns an empty list if n <= 0
    """
    a = [[] for i in range(M)]  # Initialize a list of empty lists
    for i in range(M):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][j] + a[i - 1][j - 1])
            elif j == i:
                a[i].append(1)
    return a
