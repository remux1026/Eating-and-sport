import unittest
from Searcher import Searcher

class TestSearcher(unittest.TestCase):
    def setUp(self):
        self.searcher = Searcher()
        self.food_list = [
            ["Apple", 52, 0.2, 0.3, 54, 0.01, 4.6],
            ["Banana", 89, 0.3, 1.1, 64, 0.02, 8.7],
            ["Carrot", 41, 0.2, 0.9, 16706, 0.03, 5.9],
            ["Durian", 147, 5.3, 1.5, 44, 0.01, 19.7]
        ]

    def test_fname_search(self):
        self.assertEqual(self.searcher.fname_search(self.food_list, "Banana"), 1)
        self.assertEqual(self.searcher.fname_search(self.food_list, "Durian"), 3)
        self.assertIsNone(self.searcher.fname_search(self.food_list, "Orange"))


if __name__ == "__main__":
    unittest.main()
