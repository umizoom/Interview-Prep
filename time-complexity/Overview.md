## What is time Complexity

Estimates how an algorithm performs regardless of the kind of machine is runs on. 
You can get the time complexity by "counting" the number of operations performed by your code. 

Time complexity is defined as a function of the input size `n` using Big-O notation. `n` indicates the input size 
while `O` is thw worst-case scenario.  

| Big O Notation | Big O Notation | Description                                                                                                                                                                  | Examples                                  |
|----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `O(1)`         | Constant       | O(1) describes algorithms that take the same amount of time to compute regardless of the input size                                                                          | Odd or Even, Hash-map look up (sometimes) |
| `O(n)`         | Linear         | O(n) means that the algorithms take proportionally longer to complete as the input grows. These algorithms imply that the program visits every element from the input.       | Get min/max value in an array             |
| `O(log n)`     | Logarithmic    |                                                                                                                                                                              |                                           |
| `O(n log n)`   | Linearithmic   |                                                                                                                                                                              |                                           |
| `O(n^2)`       | Quadratic      | A function with a quadratic time complexity has a growth rate of n2. If the input is size 2, it will do four operations. If the input is size 8, it will take 64, and so on. |                                           |
| `O(n^3)`       | Cubic          |                                                                                                                                                                              |                                           |
| `O(2^n)`       | Exponential    |                                                                                                                                                                              |                                           |
| `O(n!)`        | Factorial      |                                                                                                                                                                              |                                           |


## Examples

### Odd or Even

Find if a number is odd or even

```python
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

```

### Hash-map look up

```python
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

```

### Get min/max value in an array

```python
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
```