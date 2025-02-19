import unittest
from database import database

class TestDatabase(unittest.TestCase):
    def setUp(self):

        self.db = database(id=1)

    def test_initialization(self):

        self.assertEqual(self.db.id, 1)
        self.assertEqual(self.db.food_database, [])
        self.assertEqual(self.db.sport_database, [])
        
if __name__ == "__main__":
    unittest.main()
