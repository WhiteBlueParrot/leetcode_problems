from typing import List


def f7(seq):
    """
    The supa optimized solution
    """
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]
    # seen.add(x) is just there because if not() is a convenient way to execute the function inline.
    # the .add method always returns None, so it doesn't change anything


def func(seq):
    """
    My personal solution
    """
    seen = set()
    new_list = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            new_list.append(x)
    return new_list


def remove_duplicates_generator(nums: List[int]) -> int:
    """
    Slightly more memory efficient solution that uses a generator *new_nums* instead of a list *new_nums*
    """
    seen = set()
    k = 0
    new_nums = (x for x in nums if not (x in seen or seen.add(x)))
    for i, num in enumerate(new_nums):
        nums[i] = num
        k += 1

    return k


def remove_duplicates_gorgeous(nums: List[int]) -> int:
    """
    The truly gorgeous in-place solution with O(1) extra memory
    """
    if not nums:  # Handle empty array case
        return 0
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:  # if element is unique
            nums[left] = nums[right]  # move it to the left
            left += 1  # increment left
    print(nums)
    return left


print(f7([3, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 3, 3, 8, 9, 10, 3]))
print(func([3, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 3, 3, 8, 9, 10, 3]))
# print(remove_duplicates_gorgeous([3, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 3, 3, 8, 9, 10, 3]))
print(remove_duplicates_generator([3, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 3, 3, 8, 9, 10, 3]))  # non-sorted array
print(remove_duplicates_gorgeous([1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]))  # sorted array
print(remove_duplicates_generator([1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]))
