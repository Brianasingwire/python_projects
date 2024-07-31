'''Binary Search Project'''


def binary_search(arr: list[int], target: int) -> int:
    """
    Binary search for a target value in an array.

    Args:
        arr (list[int]): Array for numbers to be searched into.
        target (int): Target value to be searched for.

    Returns:
        int: Index of the value being searched for.
    """
    low, high = 0, len(arr)-1

    while low <= high:
        mid_index = (low + high) // 2
        mid_value = arr[mid_index]

        if mid_value == target:
            return mid_index
        if mid_value < target:
            low = mid_index + 1
        else:
            high = mid_index - 1

    return -1
