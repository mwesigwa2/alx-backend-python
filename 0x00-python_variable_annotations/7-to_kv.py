#!/usr/bin/env python3
''' type-annotated function to_kv '''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
        function that takes a string and an int OR float
        returns a tuple.
    '''

    return (k, v**2.0)
