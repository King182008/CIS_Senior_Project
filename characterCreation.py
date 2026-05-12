import json
import os
from shop import ShopItem, ShopWeapon, weapons
from utils import highlight, danger, name
import sys


# =========================
# DEFAULT FLAG STATE
# =========================
DEFAULT_FLAGS = {
    "mountain_intro_seen": False,
    "desert_intro_seen": False,
    "swamp_intro_seen": False,
    "volcano_intro_seen": False,
    "forest_intro_seen": False,
    "void_intro_seen": False,

    "swamp_interact_seen": False,
    "desert_interact_seen": False,
    "mountain_interact_seen": False,
    "volcano_interact_seen": False,
    "forest_interact_seen": False,
    "void_interact_seen": False,

    "rat_king_defeated": False,
    "desert_boss_defeated": False,
    "void_boss_defeated": False,
    "void_beacon_destroyed": False,

    "ritual_room_found": False,
    "extra_turn": False,
    "void_password_unlocked": False,

    "volcano_outro_seen": False,
    "forest_outro_seen": False,
    "swamp_outro_seen": False,
    "desert_outro_seen": False,
    "mountain_outro_seen": False,
    "void_outro_seen": False,
}

DEFAULT_PLACES_BEEN = {
    "forest": True,
    "desert": False,
    "mountains": False,
    "swamp": False,
    "volcano": False,
    "void": False,
}


def initialize_flags(flags, current_place="forest"):
    if flags is None:
        flags = {}

    for key, default_value in DEFAULT_FLAGS.items():
        flags.setdefault(key, default_value)

    places = flags.get("placesBeen")
    if not isinstance(places, dict):
        flags["placesBeen"] = DEFAULT_PLACES_BEEN.copy()
    else:
        for place, default_value in DEFAULT_PLACES_BEEN.items():
            places.setdefault(place, default_value)

        if current_place in places:
            places[current_place] = True

    return flags


# =========================
# CHARACTER CLASS
# =========================

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.mana = 50
        self.spellList = set()
        self.strength = 0
        self.intelligence = 0
        self.agility = 0
        self.xp = 0
        self.xp_to_next_level = 50 * (self.level ** 2)
        self.gold = 5
        self.weapon = weapons["Wooden Sword"]
        self.inventory = {}
        self.quest_log = {}
        self.currentPlace = "forest"
        self.flags = initialize_flags({}, self.currentPlace)

    # =========================
    # SAVE DATA
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
            "weapon": self.weapon.to_dict() if hasattr(self.weapon, "to_dict") else None,
            "currentPlace": self.currentPlace,
            "spellList": list(self.spellList),

            "inventory": {
                item_name: {
                    "quantity": data["quantity"],
                    "item": data["item"].to_dict() if hasattr(data["item"], "to_dict") else {
                        "type": "item",
                        "name": data["item"].name
                    }
                }
                for item_name, data in self.inventory.items()
            },

            "quest_log": self.quest_log,
            "flags": self.flags
            
        }

    # =========================
    # SAVE GAME
    # =========================
    def save_character(self, slot):
        filename = f"save{slot}.json"

        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

        print(highlight(f"\n✔ Saved to Slot {slot}"))

    # =========================
    # LOAD GAME
    # =========================
    @classmethod
    def load_character(cls, slot):
        filename = f"save{slot}.json"

        if not os.path.exists(filename):
            print(danger("No save file found."))
            return None

        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(danger("Save file is corrupted."))
            return None

        hero = cls(data["name"])

        # ---------- STATS ----------
        hero.level = data.get("level", 1)
        hero.health = data.get("health", 100)
        hero.mana = data.get("mana", 50)
        hero.strength = data.get("strength", 1)
        hero.intelligence = data.get("intelligence", 1)
        hero.agility = data.get("agility", 1)
        hero.gold = data.get("gold", 100)
        hero.xp = data.get("xp", 0)
        hero.xp_to_next_level = data.get("xp_to_next_level", 50 * (hero.level ** 2))
        hero.currentPlace = data.get("currentPlace", "forest")
        hero.spellList = set(data.get("spellList", []))

        hero.quest_log = data.get("quest_log", {})
        hero.flags = initialize_flags(data.get("flags", {}), hero.currentPlace)

        # ---------- WEAPON ----------
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

        # ---------- INVENTORY ----------
        hero.inventory = {}

        for item_name, item_data in data.get("inventory", {}).items():
            saved_item = item_data["item"]
            quantity = item_data["quantity"]

            if saved_item.get("type") == "weapon":
                item_obj = ShopWeapon(
                    saved_item["name"],
                    saved_item.get("price", 0),
                    1,
                    saved_item["damage"]
                )

            elif saved_item.get("type") == "item" and "price" in saved_item:
                item_obj = ShopItem(
                    saved_item["name"],
                    saved_item["price"],
                    1
                )

            else:
                from combat import Item
                item_obj = Item(saved_item["name"])

            hero.inventory[item_name] = {
                "item": item_obj,
                "quantity": quantity
            }

        print(highlight(f"\n✔ Loaded {hero.name} from Slot {slot}"))
        return hero


# =========================
# SAVE SLOT UI
# =========================

def show_slots():
    print(highlight("\n=== SAVE SLOTS ==="))
    print("-" * 45)

    for i in range(1, 4):
        filename = f"save{i}.json"

        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)

                name_text = data.get("name", "Unknown")
                level_text = data.get("level", 1)

                print(highlight(f"{i}. {name_text} (Lv. {level_text})"))

            except json.JSONDecodeError:
                print(danger(f"{i}. CORRUPTED SAVE"))
        else:
            print(f"{i}. EMPTY")

    print("-" * 45)


# =========================
# SLOT SELECTOR
# =========================

def choose_slot():
    print(highlight("\n=== SAVE MENU ==="))

    slot = input(
        f"Choose slot {highlight('(1-3)')}:\n>> "
    ).strip()

    while slot not in ["1", "2", "3"]:
        slot = input(danger("Invalid slot. Choose 1-3:\n>> ")).strip()

    return slot


# =========================
# CREATE CHARACTER
# =========================

def create_character():
    print(highlight("\n=== NEW CHARACTER ==="))

    name = input("Enter name: ").strip()

    while name == "":
        name = input(danger("Name cannot be empty:\n>> ")).strip()

    char = Character(name)

    print(highlight(f"\n✔ Welcome, {char.name}!"))
    return char


# =========================
# DELETE SAVE
# =========================

def delete_save(slot):
    filename = f"save{slot}.json"

    if os.path.exists(filename):
        os.remove(filename)
        print(highlight(f"Slot {slot} deleted"))
        sys.exit()

