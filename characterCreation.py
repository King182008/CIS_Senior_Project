import json
import os
from shop import ShopItem, ShopWeapon, weapons


class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.mana = 50
        self.strength = 1
        self.intelligence = 1
        self.agility = 1
        self.xp = 0
        self.xp_to_next_level = 50 * (self.level ** 2)
        self.gold = 100
        self.weapon = None  # Equipped weapon
        self.inventory = {}

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "mana": self.mana,
            "strength": self.strength,
            "intelligence": self.intelligence,
            "agility": self.agility,
            "gold": self.gold,
            "weapon": self.weapon.to_dict() if self.weapon else None,
            "inventory": {item.to_dict()["name"]: item.to_dict() for item in self.inventory}
        }

    def save_character(self, slot):
        filename = f"save{slot}.json"
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)
        print(f"Game saved in slot {slot}!")

    @classmethod
    def load_character(cls, slot):
        filename = f"save{slot}.json"

        if not os.path.exists(filename):
            print("No save file in that slot.")
            return None

        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("Save file is corrupted.")
                return None

        hero = cls(data["name"])
        hero.health = data["health"]
        hero.gold = data["gold"]

        weapon_data = data.get("weapon")

        if weapon_data:
            weapon_name = weapon_data["name"]
            hero.weapon = weapons[weapon_name.lower()]
        else:
            hero.weapon = None

        print(f"Loaded character {hero.name} from slot {slot}")
        return hero

        if hero:
            current_slot = slot

        char = cls(data["name"])
        char.level = data.get("level", 1)
        char.health = data.get("health", 100)
        char.mana = data.get("mana", 50)
        char.strength = data.get("strength", 1)
        char.intelligence = data.get("intelligence", 1)
        char.agility = data.get("agility", 1)
        char.gold = data.get("gold", 100)

        weapon_data = data.get("weapon")
        if weapon_data and weapon_data.get("type") == "weapon":
            char.weapon = ShopWeapon(
                weapon_data["name"],
                weapon_data["price"],
                weapon_data["quantity"],
                weapon_data["damage"]
            )

        char.inventory = []
        for item_data in data.get("inventory", []):
            if item_data["type"] == "weapon":
                item = ShopWeapon(
                    item_data["name"],
                    item_data["price"],
                    item_data["quantity"],
                    item_data["damage"]
                )
            else:
                item = ShopItem(
                    item_data["name"],
                    item_data["price"],
                    item_data["quantity"]
                )
            char.inventory.append(item)

        print(f"Loaded character {char.name} from slot {slot}")
        return char


# -------------------- UTILITY --------------------

def choose_slot():
    slot = input("Choose save slot (1-3): ")
    while slot not in ["1", "2", "3"]:
        slot = input("Invalid slot. Choose 1-3: ")
    return slot


def show_slots():
    for i in range(1, 4):
        filename = f"save{i}.json"
        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)
                print(f"Slot {i}: USED ({data.get('name', 'Unknown')})")
            except json.JSONDecodeError:
                print(f"Slot {i}: CORRUPTED SAVE")
        else:
            print(f"Slot {i}: EMPTY")


def create_character():
    name = input("Enter your character's name: ").strip()
    while name == "":
        name = input("Name cannot be empty. Enter a name: ").strip()
    char = Character(name)
    print(f"Welcome, {char.name}!")
    return char

def delete_save(slot):
    filename = f"save{slot}.json"

    if os.path.exists(filename):
        os.remove(filename)
        print(f"Save slot {slot} deleted.")
    else:
        print("No save file to delete.")