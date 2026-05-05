import time
import random
from utils import slow_print, danger, highlight, lore


# =========================
# ENEMY SYSTEM
# =========================

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Enemy:
    def __init__(self, name, health, attack, gold, xp, loot):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.gold = gold
        self.xp = xp
        self.loot = loot

    def take_damage(self, dmg):
        self.health -= dmg


# =========================
# ENEMY FACTORY
# =========================

def create_enemy(enemy_type):
    enemies = {
        "Rat": Enemy("Rat", 10, 2, 5, 5, Item("Rat Tail")),
        "Goblin": Enemy("Goblin", 20, 5, 10, 10, Item("Goblin Tooth")),
        "Troll": Enemy("Troll", 50, 10, 25, 25, Item("Troll Hide")),
        "Locust Swarm": Enemy("Locust Swarm", 30, 7, 15, 30, Item("Locust Wing")),
        "Dragon": Enemy("Dragon", 100, 20, 50, 200, Item("Dragon Scale")),
        "Cuthulu": Enemy("Cuthulu", 200, 30, 100, 500, Item("Cuthulu's Eye")),
        "Rat King": Enemy("Rat King", 75, 12, 35, 100, Item("Rat King's Crown"))
    }
    return enemies.get(enemy_type)


# =========================
# REGION ENEMIES
# =========================

Enemies = {
    "forest": ["Rat"],
    "desert": ["Goblin"],
    "mountains": ["Troll"],
    "swamp": ["Locust Swarm"],
    "volcano": ["Dragon"],
    "void": []
}


# =========================
# COMBAT UI HELPERS
# =========================

def combat_pause(text="", delay=0.02):
    """Fast animation text for combat feel"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def divider():
    print("\n" + "-" * 50 + "\n")


def enemy_intro(enemy):
    divider()
    combat_pause(f"A wild {enemy.name} appears...")
    time.sleep(0.4)
    combat_pause(f"HP: {enemy.health} | ATK: {enemy.attack}")
    divider()


# =========================
# MAIN COMBAT
# =========================

def display_enemy(enemy, hero):
    from inventory import add_item
    enemy_intro(enemy)

    while enemy.health > 0:

        combat_pause(f"\nYour HP: {hero.health} | Mana: {hero.mana}")
        combat_pause(f"{enemy.name} HP: {enemy.health}/{enemy.max_health}")
        print()

        action = input("(1) Attack  (2) Spell  (3) Run > ").strip().lower()

        # ================= ATTACK =================
        if action in ["1", "attack"]:

            damage = hero.strength + (hero.weapon.damage if hero.weapon else 0)

            combat_pause(f"\nYou strike the {enemy.name}...")
            time.sleep(0.2)
            combat_pause(f"Dealt {damage} damage!")

            enemy.take_damage(damage)

            hero.mana += 5
            combat_pause("You recover 5 mana from the clash.")

        # ================= SPELL =================
        elif action in ["2", "spell"]:

            hero.spellList.add("heal")

            weapon = hero.weapon.name.lower()

            if "fire" in weapon:
                hero.spellList.add("fireball")
            elif "water" in weapon:
                hero.spellList.add("crash")
            elif "poison" in weapon:
                hero.spellList.add("poison cloud")

            combat_pause(f"Spells available: {list(hero.spellList)}")

            spell_choice = input("Cast spell > ").strip().lower()

            if spell_choice not in hero.spellList:
                combat_pause(danger("Invalid spell."))
                continue

            spell = {
                "heal": {"mana": 20, "heal": 20},
                "fireball": {"mana": 50, "damage": 30},
                "crash": {"mana": 35, "damage": 25},
                "poison cloud": {"mana": 15, "damage": 15}
            }[spell_choice]

            if hero.mana < spell["mana"]:
                combat_pause(danger("Not enough mana."))
                continue

            hero.mana -= spell["mana"]

            if "heal" in spell:
                heal = spell["heal"] + hero.intelligence
                hero.health += heal
                combat_pause(f"You heal for {heal} HP!")
            else:
                dmg = spell["damage"] + hero.intelligence
                enemy.take_damage(dmg)
                combat_pause(f"You cast {spell_choice} for {dmg} damage!")

        # ================= RUN =================
        elif action in ["3", "run"]:
            if random.random() < 0.6:
                combat_pause("You escape successfully...")
                return "ran"
            else:
                combat_pause("You failed to escape!")

        else:
            combat_pause("Invalid action.")
            continue

        # ================= ENEMY TURN =================
        if enemy.health > 0:
            combat_pause(f"\n{enemy.name} attacks!")
            hero.health -= enemy.attack
            combat_pause(f"You take {enemy.attack} damage.")

            if hero.health <= 0:
                combat_pause(danger("You have fallen in battle..."))
                return "dead"

    # ================= WIN =================
    divider()
    combat_pause(f"{enemy.name} defeated!")
    hero.gold += enemy.gold
    add_item(enemy.loot, hero)

    combat_pause(f"You gain {enemy.gold} gold and {enemy.loot}.")
    return "win"