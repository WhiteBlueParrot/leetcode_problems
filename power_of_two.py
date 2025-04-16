"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
import math


# https://leetcode.com/problems/power-of-two/

# -2^31 <= n <= 2^31 - 1

def is_power_of_two(n: int) -> bool:
    if n == 1:
        return True
    elif n % 2 != 0 or n < 1:
        return False
    return is_power_of_two(n / 2)


def is_power_of_two_range(n: int) -> bool:
    for i in range(31):
        if 2 ** i == n:
            return True
    return False


def is_power_of_two_while(n: int) -> bool:
    if n == 0:
        return False

    while n > 0:
        if n == 1:
            return True
        if n % 2 != 0:
            break
        n //= 2
    return False


def is_power_of_two_math(n: int) -> bool:  # no loop or recursion solution
    # In case of number multiple of 2 ceil and floor will always be equal
    if n == 0:
        return False
    return math.floor(math.log2(n)) == math.ceil(math.log2(n))


def is_power_of_two_and(n: int) -> bool:
    """
    And operation between multiple of 2 and next lower number will always give 0 and other wise it will never be 0.

    example 1: 8 & 7
    1000(8) & 0111(7) => 0000(0)

    example 1: = 10 & 9
    1010(10) & 1001(9) => 1000(8)
    """
    return n > 0 and (n & (n - 1)) == 0


print(is_power_of_two(1),
      is_power_of_two(16),
      is_power_of_two(3),
      is_power_of_two(0),
      sep=', ')
print(is_power_of_two_range(1),
      is_power_of_two_range(16),
      is_power_of_two_range(3),
      is_power_of_two_range(0),
      sep=', ')
print(is_power_of_two_while(1),
      is_power_of_two_while(16),
      is_power_of_two_while(3),
      is_power_of_two_while(0),
      sep=', ')

print(is_power_of_two_math(1),
      is_power_of_two_math(16),
      is_power_of_two_math(3),
      is_power_of_two_math(0),
      sep=', ')

print(is_power_of_two_and(1),
      is_power_of_two_and(16),
      is_power_of_two_and(3),
      is_power_of_two_and(0),
      sep=', ')
