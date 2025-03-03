# https://leetcode.com/problems/sort-array-by-parity/
def sort_array_by_parity(array):
    j = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[j], array[i] = array[i], array[j]
            j += 1

    return array


print(sort_array_by_parity([3, 1, 2, 4, 13, 42, 189, 13, 22, 44, 45, 46, 0, 1]))
