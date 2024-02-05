#!/usr/bin/env python3
'''
    tests for utils
'''
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
        various test cases for utils.access_nested_map
    '''
    def test_access_nested_map(self):
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)
