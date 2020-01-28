import os
import sys
import unittest

from task import *

class Tests(unittest.TestCase):

    def test_subtract_first_from_second(self):
        func = subtract_first_from_second
        self.assertTrue(func(15, 10) == 5)


if __name__ == "__main__":
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    unittest.main(verbosity=5)