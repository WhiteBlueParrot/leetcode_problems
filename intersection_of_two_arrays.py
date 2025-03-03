from typing import List

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
'''

# https://leetcode.com/problems/intersection-of-two-arrays/

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
