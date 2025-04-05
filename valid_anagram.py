'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''


# https://leetcode.com/problems/valid-anagram/

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

def is_anagram(s: str, t: str) -> bool:  # my solution
    s_letters, t_letters = {}, {}

    for letter in s:
        if letter in s_letters:
            s_letters[letter] += 1
        else:
            s_letters[letter] = 1

    for letter in t:
        if letter in t_letters:
            t_letters[letter] += 1
        else:
            t_letters[letter] = 1

    return s_letters == t_letters


def is_anagram_using_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(is_anagram('anagram', 'nagaram'))
print(is_anagram('rat', 'car'))

print(is_anagram_using_sort('anagram', 'nagaram'))
print(is_anagram_using_sort('rat', 'car'))
