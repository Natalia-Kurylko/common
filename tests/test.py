import unittest
from homework import *


class TestHomework(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle(4, 4)
        self.rec_wrong = Rectangle(5, 6)

    def tearDown(self):
        pass

    def test_get_rectangle_perimeter(self):
        result = self.rec.get_rectangle_perimeter()
        self.assertEqual(result, 16)

    def test_get_rectangle_square(self):
        ex_result = self.rec.get_rectangle_square()
        self.assertEqual(ex_result, 16)

    def test_get_sum_of_corners(self, number_of_corners=5):
        number_of_corners=4
        number_of_corners_wrong = 5
        with self.assertRaises(ValueError):
            self.rec.get_sum_of_corners(number_of_corners_wrong)
        self.assertEqual(self.rec.get_sum_of_corners(number_of_corners), 360)

    def test_get_rectangle_diagonal(self):
        ex_result = self.rec.get_rectangle_diagonal()
        self.assertEqual(round(ex_result, 2), 5.66)

    def test_get_radius_of_circumscribed_circle(self):
        ex_radius = round(self.rec.get_radius_of_circumscribed_circle(), 2)
        self.assertEqual(ex_radius, 2.83)

    def test_get_radius_of_inscribed_circle(self):
        with self.assertRaises(ValueError):
            self.rec_wrong.get_radius_of_inscribed_circle()
        self.assertEqual(self.rec.get_radius_of_inscribed_circle(),2)


if __name__ == '__main__':
    unittest.main()
