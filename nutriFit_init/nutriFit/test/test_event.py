import unittest
from event import event

class TestEvent(unittest.TestCase):
    def test_event_initialization(self):

        e = event("sport", "2025-02-18")


        self.assertEqual(e.type, "sport")
        self.assertEqual(e.date, "2025-02-18")

    def test_attribute_access(self):

        e = event("eating", "2025-03-01")

        self.assertEqual(e.type, "eating")
        self.assertEqual(e.date, "2025-03-01")

if __name__ == "__main__":
    unittest.main()
