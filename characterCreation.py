import json
import os

class Character:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.mana = 50
        self.strength = 1
        self.intelligence = 1
        self.agility = 1
        self.gold = 100
        self.inventory = []

    # Convert object -> dictionary (needed for JSON)
    def to_dict(self):
        return self.__dict__

    def save_character(self, slot):

        filename = f"save{slot}.json"

        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

        print(f"Game saved in slot {slot}!")


    @classmethod
    def load_character(cls, slot):

        filename = f"save{slot}.json"

        try:
            with open(filename, "r") as file:
                data = json.load(file)

            character = cls(data["name"])
            character.__dict__.update(data)

            print(f"Loaded save slot {slot}")

            return character

        except FileNotFoundError:
            print("No save file in that slot.")
            return None
        
def choose_slot():

    slot = input("Choose save slot (1-3): ")

    while slot not in ["1","2","3"]:
        slot = input("Invalid slot. Choose 1-3: ")

    return slot

def show_slots():

    for i in range(1,4):

        filename = f"save{i}.json"

        if os.path.exists(filename):

            with open(filename, "r") as file:
                data = json.load(file)

            print(f"Slot {i}: USED ({data['name']})")

        else:
            print(f"Slot {i}: EMPTY")
        
def create_character():

    name = input("Enter your character's name: ").strip()

    # Optional safety check
    while name == "":
        name = input("Name cannot be empty. Enter a name: ").strip()

    character = Character(name)

    print(f"Welcome, {character.name}!")

    return character


while True:
    choice = input("New Game, Load Game or Show Slots? ").lower()

    if choice == "new":
        hero = create_character()

        show_slots()

        slot = choose_slot()

        hero.save_character(slot)

        break

    elif choice == "load":
        show_slots()
        slot = choose_slot()
        hero = Character.load_character(slot)
        print(hero.__dict__)

        if hero is not None:
            break

    elif choice == "show":
        show_slots()

    else:
        print("Invalid choice. Please choose New Game, Load Game or Show Slots.")


