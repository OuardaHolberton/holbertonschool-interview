#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: "Maria", "Ben", or None.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes
    prime = [True] * (max_n + 1)

    if max_n >= 0:
        prime[0] = False
    if max_n >= 1:
        prime[1] = False

    p = 2
    while p * p <= max_n:
        if prime[p]:
            multiple = p * p
            while multiple <= max_n:
                prime[multiple] = False
                multiple += p
        p += 1

    # Count primes up to each number
    prime_count = [0] * (max_n + 1)
    count = 0

    for i in range(max_n + 1):
        if prime[i]:
            count += 1
        prime_count[i] = count

    maria = 0
    ben = 0

    for i in range(x):
        if prime_count[nums[i]] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"

    return None
