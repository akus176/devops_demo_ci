import unittest
from main import calculate_sum_and_average, calculate_subtraction, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

    def test_subtraction_valid_numbers(self):
        self.assertEqual(calculate_subtraction([10, 2, 3]), 5)

    def test_subtraction_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_subtraction([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_subtraction_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_subtraction([10, -2, 3])

    def test_subtraction_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_subtraction([10, "b", 3])

if __name__ == '__main__':
    unittest.main()
