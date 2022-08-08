## What is time Complexity

Estimates how an algorithm performs regardless of the kind of machine is runs on. 
You can get the time complexity by "counting" the number of operations performed by your code. 

Time complexity is defined as a function of the input size `n` using Big-O notation. `n` indicates the input size 
while `O` is thw worst-case scenario.  

| Big O Notation | Mathematical Definition | Description                                                                                                                                                                  | Examples                                                                                                                                                                     |
|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `O(1)`         | Constant                | O(1) describes algorithms that take the same amount of time to compute regardless of the input size                                                                          | Odd or Even, Hash-map look up (sometimes)                                                                                                                                    |
| `O(log n)`     | Logarithmic             | Logarithmic time complexities usually apply to algorithms that divide problems in half every time.                                                                           | Binary search                                                                                                                                                               |                |                         |                                                                                                                                                                              |                                                                                                                                                                              |
| `O(n)`         | Linear                  | O(n) means that the algorithms take proportionally longer to complete as the input grows. These algorithms imply that the program visits every element from the input.       | Get min/max value in an array, Find a given element in a collection, Print all the values in a list, `faster_has_duplicates`                                                 |
| `O(n log n)`   | Linearithmic            |                                                                                                                                                                              | Merge sort, quicksort                                                                                                                                                        |
| `O(n^2)`       | Quadratic               | A function with a quadratic time complexity has a growth rate of n2. If the input is size 2, it will do four operations. If the input is size 8, it will take 64, and so on. | Check if a collection has duplicated values, Sorting items in a collection using bubble sort, insertion sort, or selection sort, Find all possible ordered pairs in an array |
| `O(n^3)`       | Cubic                   | If you have 3 nested loops that visit all the elements.                                                                                                                      |                                                                                                                                                                              |
| `O(2^n)`       | Exponential             |                                                                                                                                                                              |                                                                                                                                                                              |
| `O(n!)`        | Factorial               |                                                                                                                                                                              |                                                                                                                                                                              |


## Examples

### Odd or Even

Find if a number is odd or even

```python
def is_odd_or_even(number: int)-> str:
    """
    Given a number, determine if its Odd or Even. 
    Constant, IE: O(1)
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

```

### Hash-map look up

```python
def dic_look_up(dic_to_search: dict, word: str) -> int or None:
    """
    Constant, IE: O(1)
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

```

### Get min/max value in an array

```python
def find_max(numbers: list) -> int:
    """
    Finds the largest number in an array
    Linear, IE: O(n)
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
```

### Find duplicates in array

```python

def has_duplicates(array: list) -> list or None:
    """
    Checks for duplicate numbers. Returns duplicate numbers. Uses extra space 
    Quadratic, IE O(n^2) 
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

```


### Remove all duplicates from list

```python
def faster_has_duplicates(array: list) -> list:
    """
    Removes duplicates in linear time, IE: O(n)
    :param array:
    :return:
    >>> faster_has_duplicates(([3,99,8,3,4,66,99]))
    [3, 99, 8, 4, 66]
    >>> faster_has_duplicates(([3,99,8,8,4,3,99]))
    [3, 99, 8, 4]

    """
    # Convert each element of array to dic
    return list(dict.fromkeys(array))
```

### Binary Search 

```python
def binary_search(array: list, num_to_find ) -> bool:
    """
    This method implements the binary search algorithm. 
    Logarithmic, IE: O(log n)
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
    >>> binary_search([33, 7, 18, 29, 1], 8)
    True


    """
    # Base case. If we have an array of 2, we can determine if the num_to_find is there.
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
```