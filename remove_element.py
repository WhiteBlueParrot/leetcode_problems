from typing import List


# https://leetcode.com/problems/remove-element/


def remove_element(nums: List[int], val: int) -> int:
    # Remove all occurrences of val in nums in-place. Order doesn't matter
    # return number of elements in nums which != val (return length of new array)

    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Ok then, so we don't actually have to 'remove' the elements...


def remove_element2(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


def remove_element_filter(nums: List[int], val: int) -> int:
    new_nums = list(filter(lambda x: x != val, nums))
    for i in range(len(new_nums)):
        nums[i] = new_nums[i]
    return len(new_nums)


numbers = [1, 6, 6, 7, 4, 12, 6, 0, 100, 6]
value = 6
print(remove_element(numbers, value))

numbers = [1, 6, 6, 7, 4, 12, 6, 0, 100, 6]
value = 6
print(remove_element2(numbers, value))

numbers = [1, 6, 6, 7, 4, 12, 6, 0, 100, 6]
value = 6
print(remove_element_filter(numbers, value))

numbers = [1, 6, 7, 0]
value = 6
print(remove_element(numbers, value))
