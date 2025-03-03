from typing import List

'''
Given an integer array *nums* sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''


# https://leetcode.com/problems/squares-of-a-sorted-array/

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


def sorted_squares(nums: List[int]) -> List[int]:
    squared = sorted([num ** 2 for num in nums])
    return squared


def sorted_squares_o_n(nums: List[int]) -> List[int]:  # my personal crazy solution O(n)
    if len(nums) == 1:
        return [nums[0] ** 2]
    elif nums[0] >= 0:
        return [num ** 2 for num in nums]
    elif nums[-1] <= 0:
        return [num ** 2 for num in nums[::-1]]

    squared_and_sorted = []
    first_non_negative_index = 0
    for index, num in enumerate(nums):
        if num >= 0:
            first_non_negative_index = index
            break

    if first_non_negative_index == len(nums) - 1:  # if the first non-negative number is the last element
        i = first_non_negative_index - 1
        j = first_non_negative_index
    elif abs(nums[first_non_negative_index - 1]) <= abs(nums[first_non_negative_index + 1]):
        i = first_non_negative_index - 1
        j = first_non_negative_index
    else:  # abs(nums[first_non_negative_index - 1]) > abs(nums[first_non_negative_index + 1])
        i = first_non_negative_index
        j = first_non_negative_index + 1

    while i >= 0 and j < len(nums):
        if abs(nums[i]) <= abs(nums[j]):
            squared_and_sorted.append(nums[i] ** 2)
            i -= 1
        else:  # abs(nums[i]) > abs(nums[j])
            squared_and_sorted.append(nums[j] ** 2)
            j += 1
    # adding the remaining elements
    if i < 0:
        squared_and_sorted.extend(num ** 2 for num in nums[j:])
    if j >= len(nums):
        squared_and_sorted.extend([num ** 2 for num in nums[:i+1][::-1]])

    return squared_and_sorted

    # i, j = len(nums) // 2, (len(nums) // 2) + 1
    # squared_and_sorted = []
    #
    # while i >= 0 and j < len(nums):
    #     if abs(nums[i]) <= abs(nums[j]):
    #         squared_and_sorted.append(nums[i] ** 2)
    #         i -= 1
    #     else:  # abs(nums[i]) > abs(nums[j])
    #         squared_and_sorted.append(nums[j] ** 2)
    #         j += 1
    #
    # return squared_and_sorted


numbers = [-4, -1, 0, 3, 10]
print(sorted_squares(numbers))  # [0, 1, 9, 16, 100]
print(sorted_squares_o_n(numbers))  # [0, 1, 9, 0, 1, 16]
numbers = [-3,-3,-2,1]
print(sorted_squares_o_n(numbers))

# nums = [-4,-1,0,3,10,11,12]
# first_non_negative_index = 0
# i = first_non_negative_index, j = first_non_negative_index + 1
# compare nums[i] and nums[j]: if abs(nums[i]) < abs(nums[j]): sorted_and_squared.append(nums[i] ** 2); i -= 1
# else sorted_and_squared.append(nums[j] ** 2); j += 1
# repeat (encase in a while loop: while i >= 0 and j < len(nums))
# 0,3 | -1, 3 | -4, 3 | -4, 10 =>
# abs(-4) < abs(10), so 10 is left and i < 0, so we append the rest of the array, which is nums[j:]
#
# if nums was [-12,-11,-10,-3,0,1,4] instead, then
# 0, 1 | -3, 1 | -3, 4 | -10, 4 => abs(-10) > abs(4), so 4 is left and j > len(nums),
# so we append the rest of the array BUT IN REVERSE nums[:i:-1]
