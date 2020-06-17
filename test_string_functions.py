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
    def test_multiple_string_hello(self):
        message = "hello"
        n = 8
        self.assertEqual("hellohellohellohellohellohellohellohello", sf.multiple_string(8, "hello"))



if __name__ == '__main__':
    unittest.main()

