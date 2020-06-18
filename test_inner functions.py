"""
Program: test_valid_input_in_functions.py
Author: Ondrea Li
Date: 6/17/20
The purpose of this program is to test validate_input_in_functions.py
"""
import unittest
import unittest.mock as mock
from more_functions import inner_functions_assignment as ifa


class MyTestCase(unittest.TestCase):

    def test_measurements_rectangle(self):
        self.assertEqual(ifa.measurements([6.2, 5.6]), "Perimeter = 24.80 Area = 38.44")

    def test_measurements_square(self):
        self.assertEqual(ifa.measurements([1.5]), "Perimeter = 6.00 Area = 2.25")


if __name__ == '__main__':
    unittest.main()
