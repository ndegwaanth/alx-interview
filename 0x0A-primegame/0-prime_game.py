#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """
    Prime number game
    params:
        x: this is the number of rounds a player plays.
        nums: This is the array of numbers.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i**i, max_n + 1, i):
                primes[j] = False

    primes_moves = [0] * (max_n + 1)
    for k in range(1, max_n + 1):
        primes_moves[k] = primes_moves[k - 1] + (1 if primes[k] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_moves[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
