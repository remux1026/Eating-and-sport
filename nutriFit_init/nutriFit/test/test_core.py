import unittest
from core import core
from user import user

class TestCore(unittest.TestCase):
    def setUp(self):
        self.core_instance = core(id=1)

    def test_set_user(self):
        new_user = self.core_instance.set_user(
            user_id=101,
            name="Alice",
            age=25,
            weight=60000,
            height=1.75,
            schedule=["Gym"],
            plan=["Lose weight"],
            menu=["Salad"]
        )

        self.assertIsInstance(new_user, user)
        self.assertEqual(new_user.id, 101)
        self.assertEqual(new_user.name, "Alice")
        self.assertEqual(new_user.age, 25)
        self.assertEqual(new_user.weight, 60000)
        self.assertEqual(new_user.height, 1.75)
        self.assertEqual(new_user.schedule, ["Gym"])
        self.assertEqual(new_user.plan, ["Lose weight"])
        self.assertEqual(new_user.menu, ["Salad"])

        self.assertIs(self.core_instance.user, new_user)

if __name__ == "__main__":
    unittest.main()
