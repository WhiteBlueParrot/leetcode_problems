from typing import List

'''
Given an array of integers *nums* and an integer *target*, 
return indices of the two numbers such that they add up to *target*.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


# https://leetcode.com/problems/two-sum/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]


def two_sum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i, num in enumerate(nums):
        hash_table[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table and hash_table[complement] != i:
            # hash_table[complement] != i is to prevent self-matching
            # if complement in hash_table checks keys, not values
            return [i, hash_table[complement]]


def two_sum_one_pass(nums: List[int], target: int) -> List[int]:
    hash_table = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[num] = i

    return []  # No solution found


numbers = [2, 7, 11, 15]
target_value = 26
print(two_sum(numbers, target_value))

numbers = [2, 7, 11, 15]
target_value = 9
print(two_sum(numbers, target_value))

numbers = [3, 2, 4]  # why we need hash_table[complement] != i
target_value = 6
print(two_sum(numbers, target_value))

numbers = [2, 7, 11, 15]
target_value = 26
print(two_sum_one_pass(numbers, target_value))
