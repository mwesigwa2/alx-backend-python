#!/usr/bin/env python3
''' definitions with set values '''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
        function which takes a list input_list
        of floats as argument and returns
        their sum as a float.
    '''
    total_sum = 0
    for x in input_list:
        total_sum += x
    return total_sum
