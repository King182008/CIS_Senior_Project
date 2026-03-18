import json
import os
from shop import ShopItem, ShopWeapon, weapons


class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.mana = 50
        self.spellList = set()
        self.strength = 1
        self.intelligence = 1
        self.agility = 1
        self.xp = 0
        self.xp_to_next_level = 50 * (self.level ** 2)
        self.gold = 100
        self.weapon = weapons["fists"]  # Equipped weapon
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
            "xp": self.xp,
            "xp_to_next_level": self.xp_to_next_level,
            "gold": self.gold,
            "weapon": self.weapon.to_dict() if hasattr(self.weapon, "to_dict") else None,
            "inventory": {
                item_name: {
                    "quantity": data["quantity"],
                    "item": data["item"].to_dict() if hasattr(data["item"], "to_dict") else {
                        "type": "item",
                        "name": data["item"].name
                    }
                }
                for item_name, data in self.inventory.items()
            }
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

        # ---------- Basic Stats ----------
        hero.level = data.get("level", 1)
        hero.health = data.get("health", 100)
        hero.mana = data.get("mana", 50)
        hero.strength = data.get("strength", 1)
        hero.intelligence = data.get("intelligence", 1)
        hero.agility = data.get("agility", 1)
        hero.gold = data.get("gold", 100)
        hero.xp = data.get("xp", 0)
        hero.xp_to_next_level = data.get("xp_to_next_level", 50 * (hero.level ** 2))

        # ---------- Load Equipped Weapon ----------
        weapon_data = data.get("weapon")
        if weapon_data and weapon_data.get("type") == "weapon":
            hero.weapon = ShopWeapon(
                weapon_data["name"],
                weapon_data["price"],
                1,
                weapon_data["damage"]
            )
        else:
            hero.weapon = None

        # ---------- Load Inventory ----------
        hero.inventory = {}

        for item_name, item_data in data.get("inventory", {}).items():

            saved_item = item_data["item"]
            quantity = item_data["quantity"]

            # Weapon
            if saved_item.get("type") == "weapon":
                item_obj = ShopWeapon(
                    saved_item["name"],
                    saved_item.get("price", 0),
                    1,
                    saved_item["damage"]
                )

            # ShopItem
            elif saved_item.get("type") == "item" and "price" in saved_item:
                item_obj = ShopItem(
                    saved_item["name"],
                    saved_item["price"],
                    1
                )

            # Combat drop (like Rat Tail)
            else:
                from combat import Item
                item_obj = Item(saved_item["name"])

            hero.inventory[item_name] = {
                "item": item_obj,
                "quantity": quantity
            }

        print(f"Loaded character {hero.name} from slot {slot}")
        return hero


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