import time

def find_smallest(arr: list) -> int:
    # set the first element in the list as smallest.
    smallest_value = arr[0]
    # keep track of the index
    smallest_index = 0
    # loop through the indexes minus the 0th, IE first value
    for i in range(1, len(arr)):
        # check if the element i is less than the current smallest value
        if arr[i] < smallest_value:
            # Set the smallest value and index if the statement above is true
            smallest_value = arr[i]
            smallest_index = i
    # return index of smallest value.
    return smallest_index


def selection_sort(arr: list) -> list:
    """
    Selection sort algo. O(n^2), very slow.

    :param arr:
    :return:
    >>> selection_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    # create an empty list
    sorted_arr = []
    # loop through  the index of each element
    for i in range(len(arr)):
        # call method that finds the smallest value in the arr, returns index
        smallest = find_smallest(arr)
        # Pop the smallest element from the original array, append to the new sorted list
        sorted_arr.append(arr.pop(smallest))
    # return the new list when there are no more elements
    return sorted_arr


def quick_sort(arr: list) -> list:
    """
    Quick sort algo, Worst case O(n^2). Average  O(n log n)
    :param arr:
    :return:
    >>> quick_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> quick_sort([5])
    [5]
    """
    # handles the case when the arr is empty or just 1 element
    # base case
    if len(arr) < 2:
        return arr
    else:
        # find the mid-point index of the arr
        mid = (len(arr) - 1) // 2
        # set the value at the mid as our pivot
        pivot = arr[mid]
        # remove mid value from the arr
        arr.pop(mid)
        # create a list of all elements less than or equal to the pivot
        less = [i for i in arr if i <= pivot]
        # create a list of all the elements greater the pivot
        greater = [i for i in arr if i > pivot]
        # use recursion to call the quick_sort method on the 2 new lists.
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
    # handle case when arr is empty, return None
    if not arr:
        return None
    # handle case when arr has one element, return 0
    if len(arr) < 2:
        return 0
    # set the low and high index.
    low = 0
    high = len(arr) - 1
    # Loop as long as low is less than or equal too high.
    while low <= high:
        # find the mid-index
        mid = (high + low) // 2
        # if the mid-index is the target return the mid-index
        if arr[mid] == target:
            return mid
        # if the target is greater than the mid-value, move the low to the mid +1.
        # This removes/drops the left side of the arr
        elif target > arr[mid]:
            low = mid + 1
        # if the target is less than the mid-value, move the high to the mid -1.
        # this removes/drops the right side if the arr
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
