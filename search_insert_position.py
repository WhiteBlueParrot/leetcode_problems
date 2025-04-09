from typing import List

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''


# https://leetcode.com/problems/search-insert-position/

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# nums contains distinct values sorted in ascending order.

def search_insert(nums: List[int], target: int) -> int:  # this took me like 3 hours
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if low == high or low == high - 1:
            if target <= nums[low]:
                return low
            elif target == nums[high]:
                return high
            elif target > nums[high]:
                return high + 1
            else:  # nums[low] < target < nums[high]
                return high

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if nums[mid + 1] > target:
                return mid + 1
            low = mid + 1
        else:  # sequence[mid] > target:
            if nums[mid - 1] < target:
                return mid
            high = mid - 1


def search_insert_by_smart_people(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left  # <- the only difference from binary search is this line

# numbers = [1, 3, 5, 7, 9, 11, 13, 17, 19]
# target_value = 15
numbers = [1, 3, 5, 6]
target_value = 2
print(search_insert(numbers, target_value))
print(search_insert_by_smart_people(numbers, target_value))
numbers = [1, 3]
target_value = 2
print(search_insert(numbers, target_value))
print(search_insert_by_smart_people(numbers, target_value))
