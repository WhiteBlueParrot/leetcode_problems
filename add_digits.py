"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""


# https://leetcode.com/problems/add-digits/

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

# Input: num = 0
# Output: 0

# 0 <= num <= 231 - 1

def add_digits(num):
    result = 0
    for i in str(num):
        digit = int(i)
        result += digit
    if result <= 9:
        return result
    else:
        return add_digits(result)


def add_digits_o1(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


print(add_digits(38))
print(add_digits(0))
print('')
print(add_digits_o1(38))
print(add_digits_o1(0))
