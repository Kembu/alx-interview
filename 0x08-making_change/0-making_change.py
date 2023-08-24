#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0
    final_value = 0
    while total > 0:
        if not coins:
            return -1
        max_number = max(coins)
        # print(f"max_number is {max_number}")
        division = total//max_number
        # print(f"division is {division}")
        total = total - (division * max_number)
        # print(f'total is {total}')
        final_value += division
        coins.remove(max_number)
    return final_value
