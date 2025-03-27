from typing import List

"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
"""


# https://leetcode.com/problems/maximum-average-subarray-i/

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


def max_avg_subarray(nums: List[int], k: int) -> float:
    n = len(nums)
    max_avg = float('-inf')

    for i in range(n - k + 1):
        avg = sum(nums[i:i + k]) / k
        if avg > max_avg:
            max_avg = avg

    return max_avg


def max_avg_subarray_optimized(nums: List[int], k: int) -> float:
    n = len(nums)
    sum_of_k_elems = sum(nums[:k])
    max_avg = sum_of_k_elems / k

    for i in range(n - k):
        sum_of_k_elems = sum_of_k_elems - nums[i] + nums[i + k]  # subtract first element and add the next one
        avg = sum_of_k_elems / k
        if avg > max_avg:
            max_avg = avg

    return max_avg


result = max_avg_subarray([1, 12, -5, -6, 50, 3], 4)
print(f"{result:.5f}")
result = max_avg_subarray_optimized([1, 12, -5, -6, 50, 3], 4)
print(f"{result:.5f}")

result = max_avg_subarray([5], 1)
print(f"{result:.5f}")
result = max_avg_subarray_optimized([5], 1)
print(f"{result:.5f}")

result = max_avg_subarray([-1], 1)
print(f"{result:.5f}")
result = max_avg_subarray_optimized([-1], 1)
print(f"{result:.5f}")

result = max_avg_subarray([0, 1, 1, 3, 3], 4)
print(f"{result:.5f}")
result = max_avg_subarray_optimized([0, 1, 1, 3, 3], 4)
print(f"{result:.5f}")
