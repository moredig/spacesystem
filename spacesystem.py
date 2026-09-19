import json
import os
import typer
import thefuzz

CONFIG_FILE = "systembuddy.json"

def get_persistent_input():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            data = json.load(file)
            print("Loading previously saved data...")
            # FIXED: Return both values as a tuple
            return data["user_input"], data["user_age"]
            
    else:
        user_input = input("This is a one-time setup. Please enter your data: ")
        user_age = input("And your age? ")
        
        with open(CONFIG_FILE, "w") as file:
            json.dump({"user_input": user_input, "user_age": user_age}, file)
            
        print("Data saved successfully!")
        return user_input, user_age

saved_name, saved_age = get_persistent_input()

print(f"Your name is {saved_name}, and your age is {saved_age}, correct?")
mainchoice = input("Now, what can I do you for? Fuel Inspection, Crew Headcount, or do you just want to eat? ")



# Use typer AFTER their first use?
# Use the fuzz