import unittest

from triangle_func import IncorrectTriangleSides, get_triangle_type

class TestGetTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(6, 6, 6), 'equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(10, 10, 6), 'isosceles')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(12, 7, 15), 'nonequilateral')

    def test_negative_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 13, 4)

    def test_impossible_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(21, -1, 8)

    def test_zero_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 1, 2)

if __name__ == '__main__':
    unittest.main()