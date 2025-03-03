from typing import List

'''
Given a non-empty array of integers *nums*, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''


# https://leetcode.com/problems/single-number/

# Input: nums = [4,1,2,1,2]
# Output: 4


# def single_number(nums: List[int]) -> int:
#     first_appearances = []
#     for n in nums:
#         if n in first_appearances:
#             first_appearances.remove(n)
#         else:
#             first_appearances.append(n)
#     return first_appearances[0]

def single_number(nums: List[int]) -> int:  # <-- literally coolest thing ever
    result = 0
    for n in nums:
        result ^= n  # XOR operator
    return result


numbers = [4, 1, 2, 1, 2]
print(single_number(numbers))
