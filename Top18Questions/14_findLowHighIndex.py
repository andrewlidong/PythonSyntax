'''
14. Find Low/High Index
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1]. See the example below.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Scanning the array in a linear fashion would be highly inefficient because the array size could be in the millions. Instead, we will use binary search twice: once to find the low index and once to find the high index.

Here’s the algorithm to find the low index:

At each step, consider the array between low and high indices and calculate the mid index.

If the element at mid is greater or equal to the key, the high becomes mid - 1. Index at low remains the same.

If the element at mid is less than the key, low becomes mid + 1.

When low is greater than high, low would be pointing to the first occurrence of the key. If the element at low does not match the key, return -1.

For high index, we can use a similar algorithm with slight changes.

Switch the low index to mid + 1 when element at mid index is less than or equal to the key.

Switch the high index to mid - 1 when the element at mid is greater than the key.


Time: O(logN)
Space: O(1)
'''


def find_low_index(arr, key):
    low, high = 0, len(arr) - 1
    mid = (low + (high - low)) // 2

    while low <= high:
        mid_el = arr[mid]

        if mid_el < key:
            low = mid + 1
        else:
            high = mid - 1

        mid = (low + (high - low)) // 2

    if low < len(arr) and arr[low] == key:
        return low

    return -1


def find_high_index(arr, key):
    low, high = 0, len(arr) - 1
    mid = (low + (high - low)) // 2

    while low <= high:
        mid_el = arr[mid]

        if mid_el <= key:
            low = mid + 1
        else:
            high = mid - 1

        mid = (low + (high - low)) // 2

    if high == -1:
        return high

    if high < len(arr) and arr[high] == key:
        return high

    return -1


array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3,
         4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))

key = -2
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))
