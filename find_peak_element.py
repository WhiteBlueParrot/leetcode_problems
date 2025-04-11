from typing import List

'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''


# https://leetcode.com/problems/find-peak-element/

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.

# nums[i] != nums[i + 1] for all valid i.

def find_peak_element(nums: List[int]) -> int:
    # wow I solved my first Medium problem without looking at the code solution, just the NeetCode explanation
    # feels good
    low, high = 0, len(nums) - 1

    if len(nums) == 1:
        return 0

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 and nums[mid] > nums[mid + 1]) or (mid == len(nums) - 1 and nums[mid] > nums[mid - 1]):
            return mid
        elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        else:
            if nums[mid - 1] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1


def find_peak_element_by_smart_people(nums: List[int]) -> int:  # the actual solution is super simple,
    # idk how people figure this out
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low


print(find_peak_element([1, 2, 3, 1]))
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))
print(find_peak_element([6, 5, 4, 1]))
print(find_peak_element([1]))
