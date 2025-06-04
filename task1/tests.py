import unittest

from solution import sum_two


class TestStrictDecorator(unittest.TestCase):

    def test_normal_working(self):
        self.assertEqual(sum_two(2, 3), 5)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            sum_two('1', [2], 3)

    def test_type_error_bool(self):
        with self.assertRaises(TypeError):
            sum_two(2, False)

    def test_type_error_str(self):
        with self.assertRaises(TypeError):
            sum_two('2', 1)

    def test_type_error_float(self):
        with self.assertRaises(TypeError):
            sum_two(3, 1.1)


if __name__ == '__main__':
    unittest.main()
