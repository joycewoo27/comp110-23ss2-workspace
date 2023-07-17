"""EX04 - 'list' Utility Functions."""

__author__ = "730199211"


# 1. Declaring function: all
def all(list: list[int], number: int) -> bool:
    """Return True iff all the numbers in the list match the given integer, False otherwise or if list is empty."""
    if len(list) == 0:
        return False
    for integer in list:
        if integer != number:
            return False
    return True


# 2. Declaring function: max
def max(input: list[int]) -> int:
    """Return the largest number in the list."""
    max: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    for number in input:
        if max < number:
            max = number
    return max     


# 3. Declaring function: is_equal
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return True iff every element at every index is equal in both lists."""
    if len(list_1) != len(list_2):
        return False
    i: int = 0
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True