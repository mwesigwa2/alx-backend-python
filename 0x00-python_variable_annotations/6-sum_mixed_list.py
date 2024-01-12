#!/usr/bin/env python3
''' type-annotated function sum_mixed_list '''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        function which takes a list mxd_lst
        of integers and floats as argument and returns
        their sum as a float.
    '''
    total_sum = 0.0
    for x in mxd_lst:
        total_sum += x
    return total_sum
