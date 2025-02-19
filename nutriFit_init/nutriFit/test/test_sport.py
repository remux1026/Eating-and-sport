import unittest
from sport import sport

class TestSport(unittest.TestCase):
    def setUp(self):
        self.s = sport("test_sport")

    def test_initial_values(self):
        self.assertEqual(self.s.sport_name, "test_sport")
        self.assertEqual(self.s.energy_lost, 0)
        self.assertEqual(self.s.fat_lost, 0)
        self.assertEqual(self.s.protein_lost, 0)
        self.assertEqual(self.s.vitaminA_lost, 0)
        self.assertEqual(self.s.vitaminB_lost, 0)
        self.assertEqual(self.s.vitaminC_lost, 0)

    def test_play_basketball(self):
        self.s.play_basketball()
        self.assertEqual(self.s.sport_name, "play_basketball")
        self.assertEqual(self.s.energy_lost, 1000)
        self.assertEqual(self.s.fat_lost, 28)
        self.assertEqual(self.s.protein_lost, 17)
        self.assertEqual(self.s.vitaminA_lost, 5)
        self.assertEqual(self.s.vitaminB_lost, 6)
        self.assertEqual(self.s.vitaminC_lost, 0)

    def test_play_soccer(self):
        self.s.play_soccer()
        self.assertEqual(self.s.sport_name, "play_soccer")
        self.assertEqual(self.s.energy_lost, 1200)
        self.assertEqual(self.s.fat_lost, 30)
        self.assertEqual(self.s.protein_lost, 18)
        self.assertEqual(self.s.vitaminA_lost, 5)
        self.assertEqual(self.s.vitaminB_lost, 7)
        self.assertEqual(self.s.vitaminC_lost, 0)

    def test_swim_freestyle(self):
        self.s.swim_freestyle()
        self.assertEqual(self.s.sport_name, "swim_freestyle")
        self.assertEqual(self.s.energy_lost, 1500)
        self.assertEqual(self.s.fat_lost, 40)
        self.assertEqual(self.s.protein_lost, 22)
        self.assertEqual(self.s.vitaminA_lost, 6)
        self.assertEqual(self.s.vitaminB_lost, 8)
        self.assertEqual(self.s.vitaminC_lost, 0)

    def test_cycle_road(self):
        self.s.cycle_road()
        self.assertEqual(self.s.sport_name, "cycle_road")
        self.assertEqual(self.s.energy_lost, 1800)
        self.assertEqual(self.s.fat_lost, 55)
        self.assertEqual(self.s.protein_lost, 30)
        self.assertEqual(self.s.vitaminA_lost, 7)
        self.assertEqual(self.s.vitaminB_lost, 10)
        self.assertEqual(self.s.vitaminC_lost, 0)

    def test_lift_weights(self):
        self.s.lift_weights()
        self.assertEqual(self.s.sport_name, "lift_weights")
        self.assertEqual(self.s.energy_lost, 800)
        self.assertEqual(self.s.fat_lost, 20)
        self.assertEqual(self.s.protein_lost, 35)
        self.assertEqual(self.s.vitaminA_lost, 4)
        self.assertEqual(self.s.vitaminB_lost, 5)
        self.assertEqual(self.s.vitaminC_lost, 0)

    def test_abandoned_methods(self):
        self.s.sporta()
        self.assertEqual(self.s.sport_name, "kayaking")
        self.s.sportb()
        self.assertEqual(self.s.sport_name, "kayaking")
        self.s.sportc()
        self.assertEqual(self.s.sport_name, "kayaking")
        self.s.sportd()
        self.assertEqual(self.s.sport_name, "kayaking")
        self.s.sporte()
        self.assertEqual(self.s.sport_name, "kayaking")

if __name__ == '__main__':
    unittest.main()
