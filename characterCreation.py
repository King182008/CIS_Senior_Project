import os
import json
from items import Item, Weapon


# =========================
# SAVE SLOT UI
# =========================

def choose_slot():
    slot = input("Choose save slot (1-3): ").strip()
    while slot not in ["1", "2", "3"]:
        slot = input("Invalid slot. Choose 1-3: ").strip()
    return slot


def show_slots():
    print("\n=== SAVE SLOTS ===")

    for i in range(1, 4):
        file = f"save{i}.json"

        if not os.path.exists(file):
            print(f"Slot {i}: EMPTY")
            continue

        try:
            with open(file, "r") as f:
                data = json.load(f)

            print(f"Slot {i}: {data.get('name', 'Unknown')} (Level {data.get('level', 1)})")

        except:
            print(f"Slot {i}: CORRUPTED SAVE")


# =========================
# CHARACTER CLASS
# =========================

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
        self.xp_to_next_level = 50

        self.gold = 5

        self.weapon = Weapon("Fists", 0, 5)

        self.inventory = {}
        self.quest_log = {}
        self.flags = {}

    # =========================
    # SAVE
    # =========================
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

            "weapon": self.weapon.to_dict(),

            "inventory": {
                k: {
                    "item": v["item"].to_dict(),
                    "quantity": v["quantity"]
                }
                for k, v in self.inventory.items()
            },

            "quest_log": self.quest_log,
            "flags": self.flags
        }

    def save_character(self, slot):
        with open(f"save{slot}.json", "w") as f:
            json.dump(self.to_dict(), f, indent=4)
        print(f"Saved slot {slot}")

    # =========================
    # LOAD (FIXED & SAFE)
    # =========================
    @classmethod
    def load_character(cls, slot):
        path = f"save{slot}.json"

        if not os.path.exists(path):
            print("No save found.")
            return None

        with open(path, "r") as f:
            data = json.load(f)

        hero = cls(data.get("name", "Unknown"))

        # stats (safe defaults)
        hero.level = data.get("level", 1)
        hero.health = data.get("health", 100)
        hero.mana = data.get("mana", 50)

        hero.strength = data.get("strength", 1)
        hero.intelligence = data.get("intelligence", 1)
        hero.agility = data.get("agility", 1)

        hero.xp = data.get("xp", 0)
        hero.xp_to_next_level = data.get("xp_to_next_level", 50)
        hero.gold = data.get("gold", 0)

        hero.quest_log = data.get("quest_log", {})
        hero.flags = data.get("flags", {})

        # =========================
        # WEAPON LOAD (SAFE)
        # =========================
        w = data.get("weapon")

        if w and w.get("type") == "Weapon":
            hero.weapon = Weapon(
                w["name"],
                w.get("price", 0),
                w.get("damage", 0)
            )
        else:
            hero.weapon = Weapon("Fists", 0, 5)

        # =========================
        # INVENTORY LOAD (FIXED)
        # =========================
        hero.inventory = {}

        for k, v in data.get("inventory", {}).items():

            item = v.get("item", {})

            name = item.get("name", "Unknown")
            price = item.get("price", 0)
            damage = item.get("damage", 0)
            item_type = item.get("type", "Item")

            if item_type == "Weapon":
                obj = Weapon(name, price, damage)
            else:
                obj = Item(name, price)

            hero.inventory[k] = {
                "item": obj,
                "quantity": v["quantity"]
            }

        print(f"Loaded {hero.name}")
        return hero


# =========================
# CREATE CHARACTER
# =========================

def create_character():
    name = input("Enter name: ").strip()

    while not name:
        name = input("Name cannot be empty: ").strip()

    print(f"Welcome {name}")
    return Character(name)


# =========================
# DELETE SAVE
# =========================

def delete_save(slot):
    file = f"save{slot}.json"

    if os.path.exists(file):
        os.remove(file)
        print("Save deleted")
    else:
        print("No save found")