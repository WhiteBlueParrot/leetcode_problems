from typing import List

# https://leetcode.com/problems/missing-number/

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
# 2 is the missing number in the range since it does not appear in nums.


def missing_number(nums: List[int]) -> int:
    start = 0

    while start < len(nums):
        num = nums[start]
        if num != start and num < len(nums):  # if num != its own index and != biggest element
            # num < len(nums) ~ num != len(nums)
            nums[num], nums[start] = nums[start], nums[num]
        else:
            start += 1
        # print(nums)

    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)


numbers = [9, 6, 4, 2, 3, 5, 7, 0, 1]   # len(numbers) = 9
print(missing_number(numbers))  # 8
# [9, 6, 4, 2, 3, 5, 7, 0, 1]
# [9, 7, 4, 2, 3, 5, 6, 0, 1]
# [9, 0, 4, 2, 3, 5, 6, 7, 1]
# [0, 9, 4, 2, 3, 5, 6, 7, 1]
# [0, 9, 3, 2, 4, 5, 6, 7, 1]
# ...
