import core
import eating
import event
import food
import schedule
import sport
import user
class ToString:
    def __str__(self):
        class_name = self.__class__.__name__
        attributes = [f"{key}={repr(value)}" for key, value in self.__dict__.items()]
        return f"{class_name}({', '.join(attributes)})"

# Example usage in existing classes:

class Food(ToString):
    def __init__(self, food_name):
        self.food_name = food_name
        self.energy_gain = 0
        self.fat_gain = 0
        self.protein_gain = 0
        self.vitaminA_gain = 0
        self.vitaminB_gain = 0
        self.vitaminC_gain = 0

class Schedule(ToString):
    def __init__(self, start_date, end_date, event_list=None):
        self.start_date = start_date
        self.end_date = end_date
        self.event_list = event_list if event_list is not None else []

class Sport(ToString):
    def __init__(self, sport_name):
        self.sport_name = sport_name
        self.energy_lost = 0
        self.fat_lost = 0
        self.protein_lost = 0
        self.vitaminA_lost = 0
        self.vitaminB_lost = 0
        self.vitaminC_lost = 0

# Testing the ToString functionality
if __name__ == "__main__":
    f = Food("Apple")
    s = Schedule("2024-01-01", "2024-12-31", ["Event1", "Event2"])
    sp = Sport("Basketball")

    print(f)
    print(s)
    print(sp)
