from sum_intervals import sum_of_intervals
import unittest

class TestKatas(unittest.TestCase):

    def test_sum_intervals(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

        # large numbers
        self.assertEqual(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
        self.assertEqual(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)
        self.assertEqual(sum_of_intervals([(-467, -264), (21, 302), (-89, 241), (-385, 129), (-399, -62), (-210, 39), (-23, 495), (-16, 301), (-89, 235), (446, 453), (375, 489), (-246, 140), (224, 287), (-366, 394), (-155, 326), (216, 225)]), 962)

    