import unittest

from .solution import appearance
from .exceptions import ValidationError
from .constants import (
    test_lesson_len, test_without_key, test_odd_values, test_int_values,
    test_negative_interval)


class TestAppearanceValidate(unittest.TestCase):

    def test_without_key(self):
        with self.assertRaises(ValidationError):
            appearance(test_without_key)

    def test_lesson_len(self):
        with self.assertRaises(ValidationError):
            appearance(test_lesson_len)

    def test_odd_values(self):
        with self.assertRaises(ValidationError):
            appearance(test_odd_values)

    def test_int_values(self):
        with self.assertRaises(ValidationError):
            appearance(test_int_values)

    def test_negative_interval(self):
        with self.assertRaises(ValidationError):
            appearance(test_negative_interval)


if __name__ == '__main__':
    unittest.main()
