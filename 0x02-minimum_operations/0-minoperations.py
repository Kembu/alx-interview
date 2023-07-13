#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
      """
    Calculates the fewest number of operations \
        needed to achieve exactly n 'H' characters in the file.

    Arguments:
    - n: An integer representing the desired number of 'H' characters.

    Returns:
    - An integer representing the minimum number of operations needed.

    If it is impossible to achieve the desired number\
        of 'H' characters, the function returns 0.
    """

    n = n

    if (n < 2):
        return 0
    elif (n < 6 or n % 2 != 0):
        return n
    else:
        x = n
        while (x % 2 == 0 and x > 5):
            x = x // 2
        return ((n // x) + x)
