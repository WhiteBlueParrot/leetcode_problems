from typing import List

'''
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
'''

# https://leetcode.com/problems/third-maximum-number

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

def third_max(nums: List[int]) -> int:
    negative_infinity = float('-inf')
    first = second = third = negative_infinity

    for i in range(len(nums)):
        if nums[i] in (first, second, third):
            continue

        if nums[i] > first:
            # third, second, first = second, first, nums[i]
            third = second
            second = first
            first = nums[i]
        elif nums[i] > second:
            third = second
            second = nums[i]
        elif nums[i] > third:
            third = nums[i]
        else:
            continue

    if third != negative_infinity:
        return third
    else:
        return first


def third_max_optimized(nums: List[int]) -> int:
    nums.sort(reverse=True)
    curr = nums[0]
    count = 1
    for num in nums:
        if num < curr:
            curr = num
            count += 1
            if count == 3:
                return curr
    return nums[0]


def nth_max(nums: List[int], n: int) -> int:
    nums = sorted(set(nums))  # O(n) + O(n log n) = O(n log n)
    if len(nums) < n:
        return nums[-1]
    return nums[-n-1]


numbers = [3, 2, 1]
print(third_max(numbers))
numbers = [1, 2]
print(third_max(numbers))
numbers = [2, 2, 3, 1]
print(third_max(numbers))
numbers = [2, 33, 33, 45, 45, 64, 1, 0, -2, -100, 1, 100]
print(third_max(numbers))
numbers = [2, 33, 33, 45, 45, 64, 1, 0, -2, -100, 1, 100]
print(nth_max(numbers, 2))
