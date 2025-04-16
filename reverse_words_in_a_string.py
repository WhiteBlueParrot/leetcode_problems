"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


# https://leetcode.com/problems/reverse-words-in-a-string/

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

def reverse_words(s: str) -> str:
    words = s.split()
    return ' '.join(words[::-1])


def reverse_words_manual(s: str) -> str:
    def custom_split(text):
        words = []
        word = ""

        for char in text:
            if char.isspace():
                if word:
                    words.append(word)
                    word = ""
            else:
                word += char

        if word:  # append the last word if exists
            words.append(word)

        return words

    words_list = custom_split(s)
    left, right = 0, len(words_list) - 1

    while left < right:
        words_list[left], words_list[right] = words_list[right], words_list[left]
        left += 1
        right -= 1

    return ' '.join(words_list)


print(reverse_words("the sky is blue"),
      reverse_words("  hello world  "),
      reverse_words("a good   example"),
      sep=', ')

print(reverse_words_manual("the sky is blue"),
      reverse_words_manual("  hello world  "),
      reverse_words_manual("a good   example"),
      sep=', ')
