import time

def find_smallest(arr: list) -> int:
    smallest_value = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    """
    Selection sort algo. O(n^2), very slow.

    :param arr:
    :return:
    >>> selection_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


def quick_sort(arr: list) -> list:
    """
    Quick sort algo, Worst case O(n^2). Average  O(n log n)
    :param arr:
    :return:
    >>> quick_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    if len(arr) < 2:
        return arr
    else:
        mid = (len(arr) -1) // 2
        pivot = arr[mid]
        arr.pop(mid)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def binary_search(arr: list, target: int) -> int or None:
    """
    Takes a sorted array, returns index of target. Returns None if target does not exist
    :param arr:
    :param target:
    :return:
    >>> binary_search([1,2,3,4,5], 5)
    4
    """
    if not arr:
        return None
    if len(arr) < 2:
        return 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        if target < arr[mid]:
            high = mid - 1


if __name__ ==  "__main__":
    import doctest
    doctest.testmod()
    # start = time.time()
    # selection_sort([5, 4, 3, 2, 1])
    # end = time.time()
    # print(f"Selection Sort took {end - start}")
    #
    # start = time.time()
    # quick_sort([5, 4, 3, 2, 1])
    # end = time.time()
    #
    # print(f"Quick Sort took {end - start}")
