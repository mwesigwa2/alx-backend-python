#!/usr/bin/env python3
''' type-annotated function '''

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' returns list of tuples'''
    return [(i, len(i)) for i in lst]
