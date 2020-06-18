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
        self.assertEqual(vf.score_input("Python"), "Python:0")
    def test_score_input_score_valid(self):
        test_score = 77
        self.assertEqual(vf.score_input("Python", test_score), "Python:77")
    def test_score_input_below_range(self):
        test_score = -33
        self.assertEqual(vf.score_input("Python", test_score), "Python:-33, Please try again")
    def test_score_input_above_range(self):
        test_score = 999
        self.assertEqual(vf.score_input("Python", test_score), "Python:999, Please try again")
    def test_score_input_above_range(self):
        #above range
        test_score = 999
        self.assertEqual(vf.score_input("Python", test_score), "Python:999, Please try again")
    def test_score_input_invalid_message(self):
        #above range
        test_score = 888
        self.assertEqual(vf.score_input("Python", test_score, invalid_message="Please try again"), "Python:888, Please try again")

if __name__ == '__main__':
    unittest.main()
