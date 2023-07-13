#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve\
            exactly n 'H' characters in the file.

    Arguments:
    - n: An integer representing the desired number of 'H' characters.

    Returns:
    - An integer representing the minimum number of operations needed.

    If it is impossible to achieve the desired number of 'H'\
            characters, the function returns 0.
    """

    num = n

    if num < 2:
        return 0
    elif num < 6 or num % 2 != 0:
        return num
    else:
        x = num
        while x % 2 == 0 and x > 5:
            x = x // 2
        return (num // x) + x
