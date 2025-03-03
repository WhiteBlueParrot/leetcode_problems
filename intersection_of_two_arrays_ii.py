from typing import List
from collections import Counter

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
'''


# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    intersection = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:  # nums1[i] = nums2[i]
            intersection.append(nums1[i])
            i += 1
            j += 1
    return intersection


def intersect_hash(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        # To optimize the space,
        # we ensure len(nums1) <= len(nums2) by swapping nums1 with nums2 if len(nums1) > len(nums2)
        return intersect_hash(nums2, nums1)

    count = Counter(nums1)
    # print(count)
    intersection = []
    for n in nums2:
        if count[n] > 0:
            intersection.append(n)
            count[n] -= 1
    return intersection


numbers1 = [1, 2, 2, 1]
numbers2 = [2, 2]
print(intersect(numbers1, numbers2))
print(intersect_hash(numbers1, numbers2))
