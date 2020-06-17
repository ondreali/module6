"""
Program: test_valid_input_in_functions.py
Author: Ondrea Li
Date: 6/17/20
The purpose of this program is to test validate_input_in_functions.py
"""
import unittest
import unittest.mock as mock
from more_functions import validate_input_in_functions as vf


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        #only mandatory argument
        self.assertEqual(vf.score_input("English"), "English:0")
    def test_score_input_score_valid(self):
        test_score = 77
        self.assertEqual(vf.score_input("English"), "English:77")


if __name__ == '__main__':
    unittest.main()
