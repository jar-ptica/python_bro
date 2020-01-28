import os
import sys
import unittest

from task import *

class TestNumericTasks(unittest.TestCase):

    def test_sum_of_two_numbers(self):
        self.assertTrue(sum_of_two_numbers(10, 10) == 20)
        self.assertTrue(sum_of_two_numbers(10, 10.0) == 20)
        self.assertFalse(sum_of_two_numbers(10, 1.0) == 10)
        self.assertTrue(sum_of_two_numbers(10, False) == 10)
        self.assertEqual(sum_of_two_numbers(10, 15), 25)

    def test_absolute_numeric_value(self):
        self.assertTrue(absolute_numeric_value(10) == 10)
        self.assertEqual(absolute_numeric_value(-5), 5)
        self.assertEqual(absolute_numeric_value(-5.1), 5.1)
        self.assertRaises(ValueError, absolute_numeric_value, [])
        self.assertRaises(ValueError, absolute_numeric_value, 'ololo')
        self.assertRaises(ValueError, absolute_numeric_value, {'trololo': 5})

    def test_sum_of_two_integer_numbers_with_conversion(self):
        func = sum_of_two_integer_numbers_with_conversion
        self.assertEqual(func(10, 10), 20)
        self.assertEqual(func(10, 10.4), 20)
        self.assertEqual(func(10, True), 11)
        self.assertFalse(func(10, 10.1) == 50)
        self.assertRaises(TypeError, func, 10, [1])
        self.assertRaises(TypeError, func, 10, 'sdf')
        self.assertRaises(TypeError, func, 10, {})

    def test_sum_of_two_absolute_numbers(self):
        func = sum_of_two_absolute_numbers
        self.assertTrue(func(1.1, 1.2) == 2.3)
        self.assertTrue(func(5.1, -3.1) == 8.2)
        self.assertTrue(func(2, 0) == 2)
        self.assertFalse(func(5.1, 2.1) == 8.2)
        self.assertTrue(func(5.1, False) == 5.1)
        self.assertTrue(func(-5.1, False) == 5.1)
        self.assertRaises(TypeError, func, 10, [1])
        self.assertRaises(TypeError, func, 10, 'sdf')
        self.assertRaises(TypeError, func, 10, {})

class TestStringTasks(unittest.TestCase):

    def test_sum_of_two_strings_with_conversion(self):
        func = sum_of_two_strings_with_conversion
        self.assertTrue(func('tro', 'lolo') == 'trololo')
        self.assertTrue(func('tro', '1010') == 'tro1010')
        self.assertTrue(func('tro', 1010) == 'tro1010')
        self.assertTrue(func('tro', [1, 0, 1, 0]) == 'tro[1, 0, 1, 0]')
        self.assertTrue(func('tro', {1: 0}) == 'tro{1: 0}')

if __name__ == "__main__":
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    unittest.main(verbosity=5)