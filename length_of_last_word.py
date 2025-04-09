'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''


# https://leetcode.com/problems/length-of-last-word/

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# s consists of only English letters and spaces ' '

def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])  # ezzzzz


def length_of_last_word_but_boring(s: str):
    end = len(s) - 1
    while s[end] == ' ':
        end -= 1

    start = end

    while start >= 0 and s[start] != ' ':
        start -= 1

    return end - start


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))

print(length_of_last_word_but_boring("Hello World"))
print(length_of_last_word_but_boring("   fly me   to   the moon  "))
print(length_of_last_word_but_boring("luffy is still joyboy"))
