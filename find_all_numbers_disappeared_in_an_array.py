from typing import List

'''
Given an array *nums* of n integers where *nums[i]* is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in *nums*.
'''


# n == len(nums) and 1 <= nums[i] <= n, therefore 1 <= nums[i] <= len(nums)

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


def find_all_numbers_disappeared_in_an_array(nums: List[int]) -> List[int]:
    length_orig = len(nums)
    nums = set(nums)
    disappeared = []
    for i in range(1, length_orig + 1):
        if i not in nums:
            disappeared.append(i)
    return disappeared


def find_all_numbers_disappeared_in_an_array_wo_set(nums: List[int]) -> List[int]:  # takes too long
    length_orig = len(nums)
    # nums = set(nums)
    disappeared = []
    for i in range(1, length_orig + 1):
        if i not in nums:
            disappeared.append(i)
    return disappeared


def find_all_numbers_disappeared_in_an_array_cycle_sort(nums: List[int]) -> List[int]:
    for n in nums:
        a = abs(n) - 1
        if nums[a] > 0:
            nums[a] *= -1
        print(nums)
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


numbers = [4, 3, 2, 7, 8, 2, 3, 1]  # len = 8
#  disappeared = [5, 6]
print(find_all_numbers_disappeared_in_an_array(numbers))
numbers = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_all_numbers_disappeared_in_an_array_cycle_sort(numbers))

# [4, 3, 2, 7, 8, 2, 3, 1]
# [4, 3, 2, -7, 8, 2, 3, 1]
# [4, 3, -2, -7, 8, 2, 3, 1]
# [4, -3, -2, -7, 8, 2, 3, 1]
# [4, -3, -2, -7, 8, 2, -3, 1]
# [4, -3, -2, -7, 8, 2, -3, -1]
# [4, -3, -2, -7, 8, 2, -3, -1] # value at index abs(2)-1 is -3 - already negative, so it doesn't change
# [4, -3, -2, -7, 8, 2, -3, -1] # value at index abs(-3)-1 is -2 - already negative, so it doesn't change
# [-4, -3, -2, -7, 8, 2, -3, -1] # value at index abs(-1)-1 is 4 - is positive, so it does change
# 4+1 and 5+1 are the disappeared numbers because values at indexes 4 and 5 are positive
# result = [5, 6]
