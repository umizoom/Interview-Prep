

def is_odd_or_even(number: int)-> str:
    """
    Given a number, determine if its Odd or Even
    :param number: int
    :return: str

    >>> is_odd_or_even(10)
    'Even'
    >>> is_odd_or_even(3)
    'Odd'
    """
    if number % 2 == 0:
        return 'Even'
    return 'Odd'


def dic_look_up(dic_to_search: dict, word: str) -> int or None:
    """

    :param dic_to_search:
    :param word:
    :return: int
    >>> dic_look_up({'the': 22038615, 'be': 12545825, 'and': 10741073, 'of': 10343885, 'a': 10144200, 'in': 6996437, 'to': 6332195}, 'the')
    22038615
    >>> dic_look_up({'the': 22038615, 'be': 12545825, 'and': 10741073, 'of': 10343885, 'a': 10144200, 'in': 6996437, 'to': 6332195}, 'of')
    10343885
    """
    try:
        return dic_to_search[word]
    except KeyError:
        return None


def find_max(numbers: list) -> int:
    """
    Finds the largest number in an array
    :param numbers:
    :return:

    >>> find_max([3,9,6,5,66,12])
    6
    66
    >>> find_max([3,99,4,8,3,4,66,12])
    8
    99
    """
    max_num = 0
    counter = 0
    for i in range(len(numbers)):
        counter += 1
        if numbers[i] > max_num:
            max_num = numbers[i]
    print(counter)
    return max_num


def has_duplicates(array: list) -> list or None:
    """
    Checks for duplicate numbers. Returns duplicate numbers. Uses extra space

     Is O(n^2) time.
    :param array:
    :return:
    >>> has_duplicates([3,99,8,3,4,66,99])
    [3, 99]
    """
    dup_free = []
    dup = []
    for value in array:
        if value not in dup_free:
            dup_free.append(value)
        else:
            dup.append(value)
    return dup


def faster_has_duplicates(array: list) -> list:
    """
    Removes duplicates in linear time.
    :param array:
    :return:
    >>> faster_has_duplicates([3,99,8,3,4,66,99])
    [3, 99, 8, 4, 66]
    >>> faster_has_duplicates([3,99,8,8,4,3,99])
    [3, 99, 8, 4]

    """
    # Convert each element of array to dic
    return list(dict.fromkeys(array))


def binary_search(array: list, num_to_find ) -> bool:
    """
    This method implements the binary search algorithm. O(log n)
    :param num_to_find:
    :param array:
    :return:
    >>> binary_search([3, 7, 8, 9, 12, 15], 15)
    True
    >>> binary_search([3, 7, 8, 9, 12], 15)
    False
    >>> binary_search([3, 7, 8, 9, 12], 3)
    True
    >>> binary_search([3, 7, 8, 9, 12], 8)
    True
    """
    if len(array) == 2:
        if array[0] == num_to_find:
            return True
        elif array[1] == num_to_find:
            return True
        else:
            return False
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2

    if array[mid] == num_to_find:
        return True
    elif array[mid] > num_to_find:
        return binary_search(array[0:mid+1], num_to_find)
    elif array[mid] < num_to_find:
        return binary_search(array[mid:], num_to_find)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
