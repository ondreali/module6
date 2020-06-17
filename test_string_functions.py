"""
program: Function_return_value.pry
Author: Ondrea Li
Last date modfied: 06/16/20

The purpose of this program is to test string_functions.py
"""

import unittest
import unittest.mock as mock
from more_functions import string_functions as sf

class MyTestCase(unittest.TestCase):
    def test_multiple_string_Ayah(self):
        message = "Ayah"
        n = 4
        self.assertEqual("AyahAyahAyahAyah", sf.multiple_string(4, "Ayah"))




if __name__ == '__main__':
    unittest.main()

