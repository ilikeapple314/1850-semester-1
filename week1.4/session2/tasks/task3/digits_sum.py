# Week 4, Session 2: Task 4
import math
# Given incomplete recursive function digits_sum with a docstring,
# your task is to complete the function based on the description


def digits_sum(number, total = 0):
    """
    This recursive function calculates the sum of digits of a given positive
    integer. For example, sum of digits for 987 = 9 + 8 + 7 = 24.
    For simplisity, ignore the case when number is not an integer or
    not a positive integer.

    Args:
        number (int): The input is a positive integer.

    Returns:
        int: The sum of the digits of the input integer.
    """
    # complete your code here
    # base case
    if(number != 0):
        
    # recursive case
        tempNum = math.trunc(number/10) * 10
        currentDigit = number - tempNum
        total = total + currentDigit
        digits_sum(tempNum/10, total)

    else:
        return(total)

# check if correct output is produced
print(digits_sum(987))  # Output: 24
print(digits_sum(12345))  # Output: 15


# Once completed, your next task is to write an equivalent function that uses loops.
