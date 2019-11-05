import unittest

from task import *

class TestObjectsComparison(unittest.TestCase):

    def test_is_two_objects_same_value(self):
        self.assertTrue(have_objects_same_value(10, 10))

    def test_is_two_objects_same_type(self):
        self.assertTrue(is_objects_same_type(5, 5))
        self.assertFalse(is_objects_same_type(2, ''))
        self.assertTrue(is_objects_same_type([10, 10], [10, 10]))
        self.assertTrue(is_objects_same_type([10, 10], ['', 10.0]))

    def test_is_two_objects_the_same(self):
        a = 10
        b = a
        self.assertTrue(is_objects_the_same(a, b))

    def test_multiple_ints(self):
        self.assertTrue(multiple_ints(5, 5) == 25)

    def test_multiple_ints_with_conversion(self):
        self.assertTrue(multiple_ints_with_conversion(5, 5.0) == 25)
        self.assertTrue(multiple_ints_with_conversion(5, '5') == 25)
        self.assertTrue(multiple_ints_with_conversion(5, False) == 0)

    def test_is_word_in_text(self):
        self.assertTrue(is_word_in_text('zhopa', 'zhopa ogromennaya'))
        self.assertFalse(is_word_in_text('ololo', 'zhopa ogromennaya'))

    def test_some_loop_exercise(self):
        self.assertTrue(some_loop_exercise() == [0, 1, 2, 3, 4, 5, 8, 9, 10, 11])

    def test_remove_from_list_all_negative_numbers(self):
        test_data = [0, 15, 16, 17, -5, -3, 1, -7, 8]
        self.assertTrue(remove_from_list_all_negative_numbers(data=test_data) == [0, 15, 16, 17, 1, 8])

    def test_alphabet(self):
        data = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
                20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
        self.assertTrue(alphabet() == data)

    def test_simple_sort(self):
        data = [3, 1, 4, 8, 7, 12, 10, 6]
        self.assertTrue(simple_sort(data) == sorted(data))

if __name__ == "__main__":
    unittest.main()