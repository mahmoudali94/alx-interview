#!/usr/bin/python3
"""
Change making module.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    the given total
    """

    if total <= 0:
        return 0

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total-current_total)//coin
        current_total += r*coin
        coin_used += r
        if current_total == total:
            return coin_used
    return -1