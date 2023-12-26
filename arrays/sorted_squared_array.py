"""
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output
[1, 4, 9, 25, 36, 64, 81]

"""


def sortedSquaredArray(array):
    array_size = len(array)
    sorted_squared_array = [0] * array_size
    min_index = 0
    max_index = array_size - 1
    for idx in range(len(array)):
        if abs(array[min_index]) < abs(array[max_index]):
            sorted_squared_array[len(array) - 1 - idx] = (
                array[max_index] * array[max_index]
            )
            max_index = max_index - 1
        else:
            sorted_squared_array[len(array) - 1 - idx] = (
                array[min_index] * array[min_index]
            )
            min_index = min_index + 1

    return sorted_squared_array
