from typing import List

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
'''


# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)


def strStrManual(haystack: str, needle: str) -> int:  # sliding window approach
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


print(strStr('sadbutsad', 'sad'))
print(strStr('leetcode', 'leeto'))

print(strStrManual('sadbutsad', 'sad'))
print(strStrManual('leetcode', 'leeto'))
