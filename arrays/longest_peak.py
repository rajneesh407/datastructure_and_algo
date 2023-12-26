"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output
6 // 0, 10, 6, 5, -1, -3

"""


def longestPeak(array):
    max_peak = 0
    current_length = 0
    idx = 1
    while idx < len(array) - 1:
        is_current_peak = (
            True
            if array[idx - 1] < array[idx] and array[idx] > array[idx + 1]
            else False
        )
        if not is_current_peak:
            idx += 1
            continue
        left, right = idx - 2, idx + 2
        while left >= 0 and array[left] < array[left + 1]:
            left = left - 1
        while right <= len(array) - 1 and array[right] < array[right - 1]:
            right = right + 1
        current_length = right - left - 1
        max_peak = max(max_peak, current_length)
        idx = right
    return max_peak
