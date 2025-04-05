'''
Given a string s, return true if the s can be palindrome
after deleting at most one character from it.
'''


# https://leetcode.com/problems/valid-palindrome-ii/description/

# Input: s = "aba"
# Output: true

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Input: s = "abc"
# Output: false

# s consists of lowercase English letters.

# def valid_palindrome(s: str) -> bool:  # I tried
#     only_alnum = ''.join(ch for ch in s if ch.isalnum())
#     only_alnum = only_alnum.lower()
#
#     left, right = 0, len(only_alnum) - 1
#     tried_deleting = False
#     while left <= right:
#         if only_alnum[left] != only_alnum[right]:
#             if tried_deleting:
#                 return False
#
#             if left + 1 >= right - 1 and len(only_alnum) % 2 == 0:
#                 return True
#             elif only_alnum[left + 1] == only_alnum[right]:
#                 tried_deleting = True
#                 left += 1
#             elif only_alnum[left] == only_alnum[right - 1]:
#                 tried_deleting = True
#                 right -= 1
#
#         left += 1
#         right -= 1
#
#     return True

def valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            string1 = s[:left] + s[left + 1:]
            string2 = s[:right] + s[right + 1:]
            # print(string1, string2)
            return string1 == string1[::-1] or string2 == string2[::-1]
        left += 1
        right -= 1
    return True


print(valid_palindrome("aba"))
print(valid_palindrome("abca"))
print(valid_palindrome("abc"))
