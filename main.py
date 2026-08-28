import json # JSON data handling
from datetime import date # Current date
import os # Operating system interaction
import time # Pauses

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "habits.json")

# -- HELPER FUNCTIONS -- #

def print_success(message):
    print(f"\033[92m{message}\033[0m")

def print_error(message):
    print(f"\033[91m{message}\033[0m")

def pause():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(habits):
    with open(DATA_FILE, "w") as file:
        json.dump(habits, file)

def add_habit(habits, name):
    if name not in habits:
        habits[name] = []
        save_data(habits)
        print_success(f"Habit '{name}' added and saved successfully!")
    else:
        print_error("This habit already exists!")
    pause()

def list_habits(habits):
    if not habits:
        print("No habits registered!")
        pause()
        return
    for name, days in habits.items():
        print(f"- {name} | Days completed: {len(days)}")
    pause()

def mark_habit(habits, name):
    today = str(date.today())
    if name not in habits:
        print_error("Habit not found!")
    elif today in habits[name]:
        print_error(f"Habit '{name}' has already been marked as done today!")
    else:
        habits[name].append(today)
        save_data(habits)
        print_success(f"Habit '{name}' marked as done for today!")
    pause()

def delete_habit(habits, name):
    if name in habits:
        del habits[name]
        save_data(habits)
        print_success(f"Habit '{name}' deleted successfully!")
    else:
        print_error("Habit not found!")
    pause()

# -- MAIN PROGRAM -- 
def main():
    habits = load_data()  # Loads habits from the JSON file or starts an empty dictionary
    while True: 
        print("\033[94m ------------------------------------------------")
        print(" Welcome to the Habit Tracker!")
        print(" ------------------------------------------------ \033[0m")
        print("1. Add habit")
        print("2. List habits") 
        print("3. Mark habit as done")
        print("4. Delete habit")
        print("5. Exit")
        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                name = input("Enter the name of the habit to add: ")
                add_habit(habits, name)
            elif choice == 2:
                list_habits(habits)
            elif choice == 3:
                name = input("Enter the name of the habit to mark as done: ")
                mark_habit(habits, name)
            elif choice == 4:
                name = input("Enter the name of the habit to delete: ")
                delete_habit(habits, name)
            elif choice == 5:
                save_data(habits)
                print_success("Progress saved. See you!")
                break
            else:
                print_error("Invalid option, please try again!")
                
        except ValueError:
            print_error("Invalid input, please enter a number matching the options.")
            input("Press Enter to try again...")
            os.system('cls' if os.name == 'nt' else 'clear')

        
if __name__ == "__main__":
    main()
