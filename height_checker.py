from typing import List

'''A school is trying to take an annual photo of all the students. 
The students are asked to stand in a single file line in non-decreasing order by
height. Let this ordering be represented by the integer array *expected* where
*expected[i]* is the expected height of the ith student in line.

You are given an integer array *heights* representing the current order that the
students are standing in. Each *heights[i]* is the height of the ith student in
line (0-indexed).

Return the number of indices where heights[i] != expected[i].'''


# https://leetcode.com/problems/height-checker/

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.


def height_checker(heights: List[int]) -> int:
    if len(heights) == 1:
        return 1

    expected = sorted(heights)
    # print(heights, expected, sep='\n')

    number_of_indices = 0
    for i in range(len(heights)):
        if expected[i] != heights[i]:
            number_of_indices += 1
    return number_of_indices


heights_list = [1, 1, 4, 2, 1, 3]
print(height_checker(heights_list))
heights_list = [5, 1, 2, 3, 4]
print(height_checker(heights_list))
heights_list = [1, 2, 3, 4, 5]
print(height_checker(heights_list))
