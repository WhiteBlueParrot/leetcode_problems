'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''


# https://leetcode.com/problems/valid-palindrome/description/

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def is_palindrome(s: str) -> bool:  # my solution
    only_alnum = ''.join(ch for ch in s if ch.isalnum())
    only_alnum = only_alnum.lower()
    return only_alnum == only_alnum[::-1]


def is_palindrome_two_pointers(s: str) -> bool:
    only_alnum = ''.join(ch for ch in s if ch.isalnum())
    only_alnum = only_alnum.lower()

    left, right = 0, len(only_alnum) - 1
    for i in range(len(s) // 2):
        if only_alnum[left+i] != only_alnum[right-i]:
            return False
    return True

    # Others did a while loop, which probably makes more sense...
    #
    # while left < right:
    #     if only_alnum[left] != only_alnum[right]:
    #         return False
    #     left += 1
    #     right -= 1


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))

print('')

print(is_palindrome_two_pointers("A man, a plan, a canal: Panama"))
print(is_palindrome_two_pointers("race a car"))
print(is_palindrome_two_pointers(" "))
