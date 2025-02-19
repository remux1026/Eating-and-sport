import sys
import os
import logging

# Importing dependent modules when needed inside functions to avoid circular imports.
# For example, user, food, sport, eating, event modules will be imported dynamically.

class ui:
    """
    A text-based user interface class for Nutiron and Fit.
    Provides methods to interact with the user, log activities,
    display summaries, and manage schedule and nutritional data.
    """

    def __init__(self):
        self.user = None
        self.food_records = []
        self.sport_records = []
        self.schedule_events = []
        logging.basicConfig(level=logging.INFO)
        logging.info("UI initialized.")
    def print_welcome_page(self):
        print("=" * 60)
        print("Welcome to Nutiron and Fit")
        print("=" * 60)
        print("This software can help you achieve the following goals:")
        print("1. Calculating Nutritional Intake:")
        print("   This app has built-in detailed nutritional data for more than 500 common foods.")
        print("   It can help you calculate how many calories, fat, and vitamins you have consumed based on your food records.")
        print("2. Calculating Consumption:")
        print("   The app records the nutritional expenditure of more than 200 common sports/activities.")
        print("   It can calculate your consumption based on your exercise records.")
        print("3. Giving Prediction and Advice:")
        print("   The app predicts your body changes and gives you suggestions based on your intake and consumption records.")
        print("=" * 60)
        print("\n")

    def display_main_menu(self):
        print("Main Menu:")
        print("1. Input User Information")
        print("2. Record Food Consumption")
        print("3. Record Sport Activity")
        print("4. Add Schedule Event")
        print("5. View Schedule")
        print("6. Show Nutritional Summary")
        print("7. Update User Weight")
        print("8. Help")
        print("9. Exit")
        print("-" * 60)

    def get_user_choice(self, prompt="Please enter your choice: "):
        choice = input(prompt)
        return choice.strip()

    def input_user_info(self):
        print("\n--- Input User Information ---")
        user_id = input("User ID: ").strip()
        name = input("Name: ").strip()
        age_input = input("Age: ").strip()
        weight_input = input("Weight (in grams): ").strip()
        height_input = input("Height (in centimeters): ").strip()

        try:
            age = int(age_input)
        except ValueError:
            print("Invalid age input. Setting age to 0.")
            age = 0

        try:
            weight = float(weight_input)
        except ValueError:
            print("Invalid weight input. Setting weight to 0.0.")
            weight = 0.0

        try:
            height = float(height_input)
        except ValueError:
            print("Invalid height input. Setting height to 0.0.")
            height = 0.0

        from user import User  # Dynamic import to avoid circular dependencies
        self.user = User(user_id, name, age, weight, height)
        print("User information recorded successfully!\n")

    def record_food_consumption(self):
        print("\n--- Record Food Consumption ---")
        food_name = input("Enter food name: ").strip()
        weight_input = input("Enter weight consumed (in grams): ").strip()
        try:
            weight = float(weight_input)
        except ValueError:
            print("Invalid weight. Setting to 0.0.")
            weight = 0.0

        # Create a food object and input nutritional details
        from food import food as Food
        food_item = Food(food_name)
        try:
            food_item.energy_gain = float(input("Enter energy gain (in kj): ").strip())
            food_item.fat_gain = float(input("Enter fat gain (in mg): ").strip())
            food_item.protein_gain = float(input("Enter protein gain (in mg): ").strip())
            food_item.vitaminA_gain = float(input("Enter vitamin A gain (in mg): ").strip())
            food_item.vitaminB_gain = float(input("Enter vitamin B gain (in mg): ").strip())
            food_item.vitaminC_gain = float(input("Enter vitamin C gain (in mg): ").strip())
        except ValueError:
            print("One or more nutritional values are invalid. Setting them to 0.")
            food_item.energy_gain = 0
            food_item.fat_gain = 0
            food_item.protein_gain = 0
            food_item.vitaminA_gain = 0
            food_item.vitaminB_gain = 0
            food_item.vitaminC_gain = 0

        from eating import eating
        try:
            food_event = eating(food_item, weight)
        except Exception as e:
            print("Error recording food consumption:", e)
            return

        if self.user is not None:
            if not hasattr(self.user, "eating_schedule"):
                self.user.eating_schedule = []
            self.user.eating_schedule.append(food_event)
            self.food_records.append(food_event)
            print("Food consumption recorded successfully!\n")
        else:
            print("No user information available. Please input user information first.\n")

    def record_sport_activity(self):
        print("\n--- Record Sport Activity ---")
        sport_name = input("Enter sport name (e.g., play_basketball, swim_freestyle): ").strip()

        from sport import sport as Sport
        sport_activity = Sport(sport_name)
        print("Do you want to use a predefined activity? (yes/no)")
        use_predefined = input().strip().lower()
        if use_predefined == "yes":
            print("Available predefined activities:")
            print("1. play_basketball")
            print("2. play_soccer")
            print("3. swim_freestyle")
            print("4. cycle_road")
            print("5. lift_weights")
            predefined_choice = input("Enter the number of the activity: ").strip()
            if predefined_choice == "1":
                sport_activity.play_basketball()
            elif predefined_choice == "2":
                sport_activity.play_soccer()
            elif predefined_choice == "3":
                sport_activity.swim_freestyle()
            elif predefined_choice == "4":
                sport_activity.cycle_road()
            elif predefined_choice == "5":
                sport_activity.lift_weights()
            else:
                print("Invalid choice, using custom values.")
        else:
            try:
                sport_activity.energy_lost = float(input("Enter energy lost (in kj): ").strip())
                sport_activity.fat_lost = float(input("Enter fat lost (in mg): ").strip())
                sport_activity.protein_lost = float(input("Enter protein lost (in mg): ").strip())
                sport_activity.vitaminA_lost = float(input("Enter vitamin A lost (in mg): ").strip())
                sport_activity.vitaminB_lost = float(input("Enter vitamin B lost (in mg): ").strip())
                sport_activity.vitaminC_lost = float(input("Enter vitamin C lost (in mg): ").strip())
            except ValueError:
                print("Invalid input, setting values to 0.")
                sport_activity.energy_lost = 0
                sport_activity.fat_lost = 0
                sport_activity.protein_lost = 0
                sport_activity.vitaminA_lost = 0
                sport_activity.vitaminB_lost = 0
                sport_activity.vitaminC_lost = 0

        if self.user is not None:
            if not hasattr(self.user, "sport_schedule"):
                self.user.sport_schedule = []
            self.user.sport_schedule.append(sport_activity)
            self.sport_records.append(sport_activity)
            print("Sport activity recorded successfully!\n")
        else:
            print("No user information available. Please input user information first.\n")

    def add_schedule_event(self):
        print("\n--- Add Schedule Event ---")
        event_type = input("Enter event type (e.g., sport, eating): ").strip()
        event_date = input("Enter event date (YYYY-MM-DD): ").strip()
        from event import event as Event
        new_event = Event(event_type, event_date)
        self.schedule_events.append(new_event)
        if self.user is not None:
            if not hasattr(self.user, "schedule"):
                self.user.schedule = []
            self.user.schedule.append(new_event)
        print("Schedule event added successfully!\n")

    def view_schedule(self):
        print("\n--- View Schedule ---")
        if self.user is not None and hasattr(self.user, 'schedule'):
            if len(self.user.schedule) == 0:
                print("No schedule events found.\n")
            else:
                print("Your Schedule:")
                for event in self.user.schedule:
                    print(f"Type: {event.type}, Date: {event.date}")
                print("")
        else:
            print("No user or schedule available.\n")

    def show_nutritional_summary(self):
        print("\n--- Nutritional Summary ---")
        if self.user is None:
            print("No user information available.\n")
            return

        # Display BMI
        bmi = self.user.get_bmi() if hasattr(self.user, 'get_bmi') else None
        if bmi is not None:
            print(f"BMI: {bmi:.2f}")
        else:
            print("BMI: Not available")

        # Sum up nutritional data from food and sport events
        total_energy_gain = sum(event.energy_gain for event in getattr(self.user, 'eating_schedule', []))
        total_energy_lost = sum(event.energy_lost for event in getattr(self.user, 'sport_schedule', []))
        print(f"Total Energy Gained (kj): {total_energy_gain}")
        print(f"Total Energy Lost (kj): {total_energy_lost}")

        # Calculate predicted weight change
        try:
            predicted_weight = self.user.get_predict_weight() if hasattr(self.user, 'get_predict_weight') else self.user.weight
            print(f"Predicted Weight (grams): {predicted_weight:.2f}")
        except Exception as e:
            print("Error predicting weight:", e)

        # Display additional nutritional changes if available
        try:
            fat_change = self.user.get_fat_change() if hasattr(self.user, 'get_fat_change') else 0
            vitamin_change = self.user.get_vitaminA_change() if hasattr(self.user, 'get_vitaminA_change') else 0
            print(f"Net Fat Change: {fat_change}")
            print(f"Net Vitamin Change: {vitamin_change}")
        except Exception as e:
            print("Error calculating nutritional changes:", e)
        print("")

    def run_abonded(self):
        self.print_welcome_page()
        while True:
            self.display_main_menu()
            choice = self.get_user_choice()
            if choice == "1":
                self.input_user_info()
            elif choice == "2":
                self.record_food_consumption()
            elif choice == "3":
                self.record_sport_activity()
            elif choice == "4":
                self.add_schedule_event()
            elif choice == "5":
                self.view_schedule()
            elif choice == "6":
                self.show_nutritional_summary()
            elif choice == "7":
                self.update_user_weight()
            elif choice == "8":
                self.print_help()
            elif choice == "9":
                print("Exiting Nutiron and Fit. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            print("\n" + "=" * 60 + "\n")


    def update_user_weight(self):
        print("\n--- Update User Weight ---")
        if self.user is None:
            print("No user information available. Please input user information first.\n")
            return
        try:
            new_weight = self.user.get_predict_weight()
            print(f"Your predicted weight is {new_weight:.2f} grams.")
            confirm = input("Do you want to update your current weight to this predicted weight? (yes/no): ").strip().lower()
            if confirm == "yes":
                self.user.weight = new_weight
                print("User weight updated successfully!\n")
            else:
                print("User weight not updated.\n")
        except Exception as e:
            print("Error updating weight:", e, "\n")

    def print_help(self):
        print("\n--- Help Menu ---")
        print("1: Input User Information - Register your personal data such as ID, name, age, weight, and height.")
        print("2: Record Food Consumption - Log details of your food intake including nutritional values.")
        print("3: Record Sport Activity - Log your physical activities and choose predefined sports or input custom values.")
        print("4: Add Schedule Event - Add a new event to your schedule (e.g., planned meals or workouts).")
        print("5: View Schedule - Display all scheduled events.")
        print("6: Show Nutritional Summary - View your BMI, energy balance, and predicted weight changes.")
        print("7: Update User Weight - Update your weight based on predicted changes from your records.")
        print("8: Help - Display this help menu.")
        print("9: Exit - Close the application.")
        print("")

    def run(self):
        self.print_welcome_page()
        while True:
            self.display_main_menu()
            choice = self.get_user_choice()
            if choice == "1":
                self.input_user_info()
            elif choice == "2":
                self.record_food_consumption()
            elif choice == "3":
                self.record_sport_activity()
            elif choice == "4":
                self.add_schedule_event()
            elif choice == "5":
                self.view_schedule()
            elif choice == "6":
                self.show_nutritional_summary()
            elif choice == "7":
                self.update_user_weight()
            elif choice == "8":
                self.print_help()
            elif choice == "9":
                print("Exiting Nutiron and Fit. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            print("\n" + "=" * 60 + "\n")
    def show_nutritional_summary_abonded(self):
        print("\n--- Nutritional Summary ---")
        if self.user is None:
            print("No user information available.\n")
            return

        # Display BMI
        bmi = self.user.get_bmi() if hasattr(self.user, 'get_bmi') else None
        if bmi is not None:
            print(f"BMI: {bmi:.2f}")
        else:
            print("BMI: Not available")

        # Sum up nutritional data from food and sport events
        total_energy_gain = sum(event.energy_gain for event in getattr(self.user, 'eating_schedule', []))
        total_energy_lost = sum(event.energy_lost for event in getattr(self.user, 'sport_schedule', []))
        print(f"Total Energy Gained (kj): {total_energy_gain}")
        print(f"Total Energy Lost (kj): {total_energy_lost}")

        # Calculate predicted weight change
        try:
            predicted_weight = self.user.get_predict_weight() if hasattr(self.user, 'get_predict_weight') else self.user.weight
            print(f"Predicted Weight (grams): {predicted_weight:.2f}")
        except Exception as e:
            print("Error predicting weight:", e)

        # Display additional nutritional changes if available
        try:
            fat_change = self.user.get_fat_change() if hasattr(self.user, 'get_fat_change') else 0
            vitamin_change = self.user.get_vitaminA_change() if hasattr(self.user, 'get_vitaminA_change') else 0
            print(f"Net Fat Change: {fat_change}")
            print(f"Net Vitamin Change: {vitamin_change}")
        except Exception as e:
            print("Error calculating nutritional changes:", e)
        print("")

if __name__ == "__main__":
    ui_instance = UI()
    ui_instance.run()
