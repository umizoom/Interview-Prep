from typing import List, Optional


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    :param nums:
    :param target:
    :return:
    >>> two_sum(nums=[2,7,11,15], target=9)
    [0, 1]
    >>> two_sum(nums= [3,2,4], target=6)
    [1, 2]
    """
    hash_map = {}
    for index in range(len(nums)):
        compliment = target - nums[index]
        if compliment in hash_map.keys():
            return [hash_map[compliment], index]
        hash_map[nums[index]] = index


def isValid(s: str) -> bool:
    """

    :param s:
    :return:
    >>> isValid("()")
    True
    >>> isValid("()[]{}")
    True
    >>> isValid("(]")
    False
    >>> isValid("(])")
    False
    """
    # base case. If odd number of elements, fail fast
    if len(s) % 2 != 0:
        return False
    # Create an empty stack to push open brackets to
    stack = []
    # create a dic of valid brackets
    valid_brackets = {'(': ')', '[': ']', '{': '}'}
    # loop through each bracket
    for bracket in s:
        # if bracket is in list of keys. IE open bracket push to stack
        if bracket in valid_brackets.keys():
            stack.append(bracket)
        else:
            # otherwise it must be a closed bracket
            if not stack:
                # if the stack is empty, that means there is no closing bracket, fail
                return False
            # Pop the last forward bracket
            forward_bracket = stack.pop()
            # check to see if the popped forward brackets value does not match the closing bracket
            # this means the forward bracket and the closing bracket are not matched. Fail
            if bracket != valid_brackets[forward_bracket]:
                return False
    if stack:
        # if the stack is not empty after the while loop, it means we did find pairs to all the brackets
        return False
    # Otherwise, it's a balanced stack
    return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """

    :param self:
    :param list1:
    :param list2:
    :return:

    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        tail = root
        # if list1 is None and list2 is None:
        #     return []

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return root.next


def maxProfit(prices: List[int]) -> int:
    """
    Problem: 121. Best Time to Buy and Sell Stock
    Time complexity: O(n)
    This problem uses a technique called 2 pointers, IE left and right
    :param prices:
    :return:
    >>> maxProfit([7,1,5,3,6,4])
    5
    >>> maxProfit([7,6,4,3,1])
    0
    """
    l, r = 0, 1
    max_p = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p


def isPalindrome(s: str) -> bool:
    """
    Problem 125: Valid Palindrome
    This problem uses a technique called 2 pointers, IE left and right
    :param s:
    :return:
    >>> isPalindrome(s="A man, a plan, a canal: Panama")
    True
    >>> isPalindrome(s="race a car")
    False
    """
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and s[l].isalnum() is False:
            l += 1
        while r > l and s[r].isalnum() is False:
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def isPalindrome_2(s: str) -> bool:
    """
    Problem 125: Valid Palindrome
    Lower solution
    :param s:
    :return:
    >>> isPalindrome(s="A man, a plan, a canal: Panama")
    True
    >>> isPalindrome(s="race a car")
    False
    """
    new_string = ''
    for c in s:
        if c.isalnum():
            new_string = new_string + c.lower()
    return new_string == new_string[::-1]


def is_anagram(s: str, t: str) -> bool:
    """
    Problem 242: Valid Anagram

    :param s:
    :param t:
    :return:
    >>> is_anagram(s = "anagram", t = "nagaram")
    True
    >>> is_anagram(s = "rat", t = "car")
    False
    """
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    for key in count_s.keys():
        try:
            if count_s[key] != count_t[key]:
                return False
        except KeyError:
            return False
    return True


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        if starting_pixel == color:
            return image
        self.dfs(image, sr, sc, color, starting_pixel)
        return image

    def dfs(self, image, sr, sc, color, starting_pixel):

        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] != starting_pixel:
            return

        image[sr][sc] = color
        self.dfs(image, sr + 1, sc, color, starting_pixel)
        self.dfs(image, sr - 1, sc, color, starting_pixel)

        self.dfs(image, sr, sc + 1, color, starting_pixel)

        self.dfs(image, sr, sc - 1, color, starting_pixel)


def sum(arr: list) -> int:
    """
    sums a array
    :param arr:
    :return:
    >>> sum([4,3,2])
    9
    >>> sum([5,10,10,20])
    45
    """
    if len(arr) == 0:
        return 0
    i = arr.pop()
    return i + sum(arr)

def count_arr(arr: list) -> int:
    """

    :param arr:
    :return:
    >>> count_arr([1,2,3,4,5])
    5
    >>> count_arr([1,2,3,4,5,6,7,8,9])
    9
    >>> count_arr([1,2,3,4,5,6,7,8,9, 10,11,12])
    12
    """
    count = 0
    if not arr:
        return 0
    count += 1
    arr.pop()
    return count + count_arr(arr)


def max_num(arr: list) -> int or None:
    """

    :param arr:
    :return:
    >>> max_num([1,2])
    3
    >>> max_num([1,2,3,4,5])
    15
    >>> max_num([2,4,6,8])
    20
    """
    if not arr:
        return 0
    max = 0
    ele = arr.pop()
    if max < ele:
        max = ele
    return max + max_num(arr)


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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
