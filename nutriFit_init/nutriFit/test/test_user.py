import unittest
from user import user
from sport import sport
from eating import eating
from food import food

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = user(1, "Alice", 25, 60000, 1.75)
        self.basketball = sport("basketball")
        self.basketball.play_basketball()

        self.food_item = food("apple")
        self.food_item.energy_gain = 500
        self.food_item.fat_gain = 10
        self.food_item.protein_gain = 5
        self.food_item.vitaminA_gain = 2
        self.food_item.vitaminB_gain = 1
        self.food_item.vitaminC_gain = 3

        self.eating_event = eating(self.food_item, 2)  

    def test_get_vitaminB_change(self):
        self.user.sport_schedule.append(self.basketball)
        self.user.eating_schedule.append(self.eating_event)
        self.assertEqual(self.user.get_vitaminA_change(), 2 - 6)

if __name__ == "__main__":
    unittest.main()
