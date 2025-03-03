"""
Python3 program to find number
of rotations in a sorted and
rotated array with unique elements
"""


def count_rotations(arr):  # basically, we just find the index of min elem
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid - 1
    return low


rotated_sorted_list = [5, 6, 9, 10, 2, 3, 4]
print(count_rotations(rotated_sorted_list))

rotated_sorted_list = [4, 5, 6, 1, 2, 3]
rotations = count_rotations(rotated_sorted_list)
print(rotations)  # Output: 3


