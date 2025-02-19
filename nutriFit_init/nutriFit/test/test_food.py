import unittest
from food import food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.apple = food("apple")
        self.apple.energy_gain = 500
        self.apple.fat_gain = 10
        self.apple.protein_gain = 5
        self.apple.vitaminA_gain = 2
        self.apple.vitaminB_gain = 1
        self.apple.vitaminC_gain = 3

    def test_attribute_access(self):
        self.assertEqual(self.apple.food_name, "apple")
        self.assertEqual(self.apple.energy_gain, 500)
        self.assertEqual(self.apple.fat_gain, 10)
        self.assertEqual(self.apple.protein_gain, 5)
        self.assertEqual(self.apple.vitaminA_gain, 2)
        self.assertEqual(self.apple.vitaminB_gain, 1)
        self.assertEqual(self.apple.vitaminC_gain, 3)

if __name__ == "__main__":
    unittest.main()
