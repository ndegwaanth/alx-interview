#!/usr/bin/python3
"""minimum operations module"""


def getPrime(start: int) -> int:
    """returns next prime  number from start"""
    while True:
        if (start % 2 == 0) or (start % 3 == 0) or \
                (start % 5 == 0) or (start % 7 == 0):
            if start not in [2, 3, 5, 7]:
                start += 1
            else:
                return start
                break
        else:
            return start
            break


def minOperations(n: float) -> int:
    """finds minimum operations to attain h"""
    if (n < 1):
        return 0
    val: int = 0
    prime: int = 2
    temp: float = n
    while n > 1:
        while (n % prime != 0):
            prime = getPrime(prime + 1)
        if temp < prime:
            return 0
        n /= prime
        if (n == 1) and (prime == temp):
            return 1
        val += prime
    return val
