'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''


# https://leetcode.com/problems/roman-to-integer/

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
# It is guaranteed that s is a valid roman numeral in the range [1, 3999]

def roman_to_int(s: str) -> int:  # hey I'm finally starting to solve some of these by myself
    integer = 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    i = len(s) - 1
    while i > 0:
        if roman_numerals[s[i]] > roman_numerals[s[i - 1]]:
            integer += roman_numerals[s[i]] - roman_numerals[s[i - 1]]
            i -= 1
        else:  # roman_numerals[s[i]] <= roman_numerals[s[i-1]]:
            integer += roman_numerals[s[i]]
        i -= 1
    if i == 0:
        integer += roman_numerals[s[0]]

    return integer


def roman_to_int_by_some1else(s: str) -> int:
    res = 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for a, b in zip(s, s[1:]):
        # 'MCMXCIV' ->
        # (('M', 'C'), ('C', 'M'), ('M', 'X'), ('X', 'C'), ('C', 'I'), ('I', 'V'))
        if roman[a] < roman[b]:
            res -= roman[a]
        else:
            res += roman[a]

    return res + roman[s[-1]]


print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))

print(roman_to_int_by_some1else("III"))
print(roman_to_int_by_some1else("LVIII"))
print(roman_to_int_by_some1else("MCMXCIV"))
