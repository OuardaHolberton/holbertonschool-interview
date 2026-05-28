#!/usr/bin/python3
"""Module for Minimum Operations problem."""


def minOperations(n):
    """Calculate the fewest operations to get n H characters.

    Args:
        n: target number of H characters

    Returns:
        minimum number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
