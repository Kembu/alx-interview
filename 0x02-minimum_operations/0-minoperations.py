#!/usr/bin/python3


def minOperations(n):
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
