#!/usr/bin/python3
"""
Module that determines the fewest number of coins needed
to meet a given total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins (list): list of the values of the coins available
        total (int): the amount to reach

    Returns:
        int: the fewest number of coins needed to meet total,
             0 if total <= 0, or -1 if total cannot be met
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
