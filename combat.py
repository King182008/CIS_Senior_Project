import time
import random
from utils import slow_print, danger, highlight
from characterCreation import delete_save


# =========================
# LEVEL SYSTEM
# =========================
def check_level_up(hero):
    while hero.xp >= hero.xp_to_next_level:
        hero.xp -= hero.xp_to_next_level
        hero.level += 1
        hero.xp_to_next_level = 50 * (hero.level ** 2)

        hero.strength += 2
        hero.intelligence += 2
        hero.agility += 1

        slow_print(highlight(f"\nLEVEL UP! Level {hero.level}"))
        slow_print("+2 STR | +2 INT | +1 AGI")


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
        "Dragon": Enemy("Dragon", 250, 20, 50, 200, Item("Dragon Scale")),
        "Horror": Enemy("Cthulu", 1000, 30, 100, 500, Item("Cthulu's Eye")),
        "Rat King": Enemy("Rat King", 75, 12, 35, 100, Item("Rat King's Crown")),
        "Chrono Guardian": Enemy("Chrono Guardian", 120, 15, 50, 100, Item("Core of Time")),
        "Henrik": Enemy("Henrik", 50, 5, 50, 100, None),
        "Time-Worn Husk": Enemy("Time-Worn Husk", 35, 8, 15, 20, Item("Withered Bone")),
        "Aged Goblin": Enemy("Aged Goblin", 25, 6, 12, 15, Item("Cracked Tooth")),
        "Sand Phantom": Enemy("Sand Phantom", 40, 10, 20, 30, Item("Sand Essence")),
        "Void Beacon": Enemy("Void Beacon", 175, 22, 100, 250, Item("Void Core")),
        "Horror Spawn": Enemy("Horror Spawn", 35, 8, 12, 18, Item("Void Shard")
)
    }
    return enemies.get(enemy_type)


Enemies = {
    "forest": ["Rat"],
    "desert": ["Goblin"],
    "mountains": ["Troll"],
    "swamp": ["Locust Swarm"],
    "desert_dungeon": ["Time-Worn Husk", "Aged Goblin", "Sand Phantom"]
}


# =========================
# HELPERS
# =========================
def divider():
    print("\n" + "-" * 50 + "\n")


def enemy_intro(enemy):
    divider()
    print(f"A wild {enemy.name} appears!")
    print(f"HP: {enemy.health} | ATK: {enemy.attack}")
    divider()


# =========================
# MAIN COMBAT
# =========================
def display_enemy(enemy, hero):
    import random
    from inventory import add_item

    enemy_intro(enemy)

    while enemy.health > 0 and hero.health > 0:

        # ================= PLAYER ACTION COUNT =================
        actions = 2 if hero.flags.get("extra_turn", False) else 1

        # ================= PLAYER TURNS =================
        for turn in range(actions):

            if enemy.health <= 0:
                break

            print("\n" + "=" * 45)
            print(highlight("             BATTLE"))
            print("=" * 45)

            print(
                f"HP: {highlight(str(hero.health))} | "
                f"Mana: {highlight(str(hero.mana))}"
            )

            print(
                f"{enemy.name}: "
                f"{danger(str(enemy.health))}/{enemy.max_health}"
            )

            print(
                f"XP: {hero.xp}/{hero.xp_to_next_level} | "
                f"Level: {hero.level}"
            )

            if turn > 0:
                print(highlight("\nTime bends — you act again!"))

            print("\n1. Attack")
            print("2. Spell")
            print("3. Run")

            action = input("\n> ").strip().lower()

            # =====================================================
            # ATTACK
            # =====================================================
            if action in ["1", "attack"]:

                damage = hero.strength

                if hero.weapon:
                    damage += hero.weapon.damage

                enemy.take_damage(damage)

                print(
                    highlight(
                        f"\nYou strike {enemy.name} "
                        f"for {damage} damage!"
                    )
                )

                # mana gain
                if hero.weapon:
                    hero.mana += hero.weapon.mana_gain
                else:
                    hero.mana += 5

            # =====================================================
            # SPELLS
            # =====================================================
            elif action in ["2", "spell"]:

                hero.spellList.add("heal")

                if hero.weapon:

                    w = hero.weapon.name.lower()

                    if "fire" in w:
                        hero.spellList.add("fireball")

                    elif "water" in w:
                        hero.spellList.add("crash")

                    elif "poison" in w:
                        hero.spellList.add("poison cloud")

                spells = {

                    "heal": {
                        "mana": 20,
                        "heal": 20,
                        "desc": "Restore health"
                    },

                    "fireball": {
                        "mana": 50,
                        "damage": 30,
                        "desc": "Massive fire damage"
                    },

                    "crash": {
                        "mana": 35,
                        "damage": 25,
                        "desc": "Water blast attack"
                    },

                    "poison cloud": {
                        "mana": 15,
                        "damage": 15,
                        "desc": "Poison damage over time"
                    }
                }

                # ================= SPELL MENU =================
                print(highlight("\n=== SPELLS ==="))
                print("-" * 45)

                available_spells = list(hero.spellList)

                for i, spell_name in enumerate(available_spells, start=1):

                    spell = spells.get(spell_name)

                    if not spell:
                        continue

                    mana = spell["mana"]
                    desc = spell["desc"]

                    if "heal" in spell:
                        power = f"Heal: {spell['heal']}"
                    else:
                        power = f"Damage: {spell['damage']}"

                    print(
                        f"{i}. "
                        f"{highlight(spell_name.title())} | "
                        f"Mana: {mana} | "
                        f"{power} | "
                        f"{desc}"
                    )

                print("-" * 45)

                spell_input = input("\nCast > ").strip().lower()

                # number support
                if spell_input.isdigit():

                    index = int(spell_input) - 1

                    if 0 <= index < len(available_spells):
                        spell_choice = available_spells[index]
                    else:
                        print(danger("Invalid spell"))
                        continue

                else:
                    spell_choice = spell_input

                if spell_choice not in spells:
                    print(danger("Invalid spell"))
                    continue

                spell = spells[spell_choice]

                if hero.mana < spell["mana"]:
                    print(danger("Not enough mana"))
                    continue

                hero.mana -= spell["mana"]

                # ================= HEAL =================
                if "heal" in spell:

                    heal = spell["heal"] + hero.intelligence

                    hero.health += heal

                    print(
                        highlight(
                            f"\nYou restore {heal} HP!"
                        )
                    )

                # ================= DAMAGE =================
                else:

                    dmg = spell["damage"] + hero.intelligence

                    enemy.take_damage(dmg)

                    print(
                        danger(
                            f"\n{spell_choice.title()} hits "
                            f"{enemy.name} for {dmg} damage!"
                        )
                    )

            # =====================================================
            # RUN
            # =====================================================
            elif action in ["3", "run"]:

                if random.random() < 0.6:
                    print(highlight("\nYou escaped successfully!"))
                    return "ran"

                else:
                    print(danger("\nFailed to escape!"))

            # =====================================================
            # INVALID
            # =====================================================
            else:
                print(danger("Invalid action"))
                continue

            # =====================================================
            # ENEMY DEAD
            # =====================================================
            if enemy.health <= 0:
                break

        # =========================================================
        # ENEMY TURN
        # =========================================================
        if enemy.health > 0:

            print(
                danger(
                    f"\n{enemy.name} attacks!"
                )
            )

            hero.health -= enemy.attack

            print(
                danger(
                    f"You take {enemy.attack} damage!"
                )
            )

        # =========================================================
        # PLAYER DEAD
        # =========================================================
        if hero.health <= 0:

            print(danger("\nYou have fallen..."))

            delete_save(hero.slot)

            return "dead"

    # =============================================================
    # VICTORY
    # =============================================================
    divider()

    print(
        highlight(
            f"{enemy.name} defeated!"
        )
    )

    hero.gold += enemy.gold
    hero.xp += enemy.xp

    add_item(enemy.loot, hero)

    print(
        highlight(
            f"+{enemy.gold} Gold | "
            f"+{enemy.xp} XP | "
            f"Loot: {enemy.loot}"
        )
    )

    check_level_up(hero)

    return "win"