from utils import slow_print, danger, highlight, name
import combat
import random
from inventory import add_item


# =========================
# ENTRY
# =========================
def enter_desert_dungeon(hero, place):
    place = "desert_dungeon"
    hero.currentPlace = "desert_dungeon"

    slow_print(highlight("\n=== DESERT DUNGEON ==="))
    slow_print("The staircase ends beneath the ruins.")
    slow_print("Time feels unstable here...")

    hero.flags["in_desert_dungeon"] = True
    hero.flags.setdefault("ritual_room_found", False)

    dungeon_loop(hero, place)


# =========================
# MAIN LOOP
# =========================
def dungeon_loop(hero, place):
    while hero.flags.get("in_desert_dungeon", False):

        if hero.health <= 0:
            return

        print(highlight("\n=== DUNGEON ACTIONS ==="))
        print("-" * 40)
        print(f"1. {name('Explore deeper')}")
        print(f"2. {name('Inspect surroundings')}")
        print(f"3. {name('Inventory')}")

        option_index = 4

        if hero.flags.get("ritual_room_found"):
            print(f"{option_index}. {name('Enter Ritual Room')}")
            ritual_option = str(option_index)
            option_index += 1
        else:
            ritual_option = None

        print(f"{option_index}. {danger('Attempt escape')}")
        print("-" * 40)

        action = input(highlight("Choose: ")).strip().lower()

        if action in ["1", "explore"]:
            explore(hero, place)

        elif action in ["2", "inspect"]:
            inspect_area(hero)

        elif action in ["3", "inventory"]:
            inventory(hero)

        elif ritual_option and action in [ritual_option, "ritual"]:
            ritual_room(hero)

        elif action in [str(option_index), "escape"]:

            escaped = attempt_escape(hero, place)

            if escaped:
                return

        else:
            slow_print(danger("Invalid choice."))


# =========================
# EXPLORE
# =========================
def explore(hero, place):
    slow_print("You move deeper into the ruins...")

    roll = random.randint(1, 100)

    if roll <= 45:
        encounter_enemy(hero, place)
    elif roll <= 70:
        find_loot(hero)
    elif roll <= 85:
        time_distortion(hero)
    elif roll <= 95:
        discover_ritual_room(hero)
    else:
        boss_encounter(hero)


# =========================
# RITUAL ROOM DISCOVERY
# =========================
def discover_ritual_room(hero):
    if hero.flags.get("ritual_room_found"):
        slow_print("You pass the ritual chamber again.")
        return

    slow_print(highlight("You discover a hidden chamber..."))
    slow_print(danger("Time pools unnaturally around an altar."))

    hero.flags["ritual_room_found"] = True


# =========================
# RITUAL ROOM
# =========================
def ritual_room(hero):
    slow_print(highlight("\n=== RITUAL ROOM ==="))
    slow_print("The altar hums with power.")

    inv = hero.inventory

    sacrifices = {
        "Ancient Coin": ("gold", 25),
        "Cracked Relic": ("strength", 1),
        "Time Shard": ("heal", 20),
        "Void Shard": ("intelligence", 1)
    }

    required = [
        "Ancient Coin",
        "Cracked Relic",
        "Time Shard",
        "Core of Time",
        "Rat King's Crown"
    ]

    valid = [
        item for item in sacrifices
        if item in inv and inv[item]["quantity"] > 0
    ]

    if not valid:
        slow_print(danger("You have nothing the altar accepts."))
        return

    # =========================
    # FULL RITUAL
    # =========================
    if all(item in inv and inv[item]["quantity"] > 0 for item in required):

        slow_print(highlight("The relics resonate together..."))
        slow_print(danger("Time bends to your will."))

        hero.flags["extra_turn"] = True

        for item in required:

            qty = inv[item]["quantity"]

            slow_print(danger(f"The altar consumes all {qty} {item}(s)..."))

            del inv[item]

        slow_print(highlight("You now act twice in battle."))
        return

    # =========================
    # SACRIFICE MENU
    # =========================
    print(highlight("\nSacrifice Options"))
    print("-" * 30)

    for i, item in enumerate(valid, 1):
        print(f"{i}. {item} x{inv[item]['quantity']}")

    print("-" * 30)

    choice = input("Choose item: ").strip()

    if not choice.isdigit():
        slow_print(danger("Invalid choice."))
        return

    choice = int(choice) - 1

    if choice < 0 or choice >= len(valid):
        slow_print(danger("Invalid choice."))
        return

    item = valid[choice]
    effect, amount = sacrifices[item]

    qty = inv[item]["quantity"]

    slow_print(danger(f"You sacrifice all {qty} {item}(s)."))

    # =========================
    # EFFECTS SCALE WITH QTY
    # =========================
    if effect == "gold":
        total = amount * qty
        hero.gold += total
        slow_print(highlight(f"+{total} Gold"))

    elif effect == "strength":
        total = amount * qty
        hero.strength += total
        slow_print(highlight(f"+{total} Strength"))

    elif effect == "intelligence":
        total = amount * qty
        hero.intelligence += total
        slow_print(highlight(f"+{total} Strength"))

    elif effect == "heal":
        total = amount * qty
        hero.health += total
        slow_print(highlight(f"+{total} HP"))

    elif effect == "time":
        hero.flags["time_mastery"] = True
        slow_print(highlight("Time bends around you."))

    # remove all
    del inv[item]
# =========================
# ENEMY
# =========================
def encounter_enemy(hero, place):
    enemy_name = random.choice(combat.Enemies.get(place, ["Goblin"]))
    slow_print(danger(f"A {enemy_name} appears!"))

    enemy = combat.create_enemy(enemy_name)
    result = combat.display_enemy(enemy, hero)

    if result == "dead":
        return


# =========================
# LOOT
# =========================
def find_loot(hero):
    from combat import Item

    loot_table = [
        Item("Ancient Coin"),
        Item("Cracked Relic"),
        Item("Time Shard")
    ]

    item = random.choice(loot_table)

    slow_print(highlight(f"You obtained: {item}"))
    add_item(item, hero)


# =========================
# TIME EVENT
# =========================
def time_distortion(hero):
    if hero.flags.get("time_mastery"):
        slow_print(highlight("You stabilize time."))
        return

    effect = random.choice(["heal", "damage", "nothing"])

    if effect == "heal":
        num = random.randint(5, 15)
        hero.health = hero.health + num
        slow_print(f"+{num} HP")

    elif effect == "damage":
        num = random.randint(5, 15)
        hero.health -= num
        slow_print(danger(f"-{num} HP"))

    else:
        slow_print("Nothing happens...")


# =========================
# BOSS
# =========================
def boss_encounter(hero):
    if hero.flags.get("desert_boss_defeated"):
        return

    slow_print(highlight("THE CHRONO GUARDIAN AWAKENS"))

    enemy = combat.create_enemy("Chrono Guardian")

    if hero.flags.get("time_mastery"):
        enemy.health -= 30

    result = combat.display_enemy(enemy, hero)

    if result == "win":
        hero.flags["desert_boss_defeated"] = True


# =========================
# INSPECT
# =========================
def inspect_area(hero):
    slow_print("The walls shift unnaturally...")


# =========================
# INVENTORY
# =========================
def inventory(hero):
    from inventory import show_inventory
    show_inventory(hero)


# =========================
# ESCAPE
# =========================
def attempt_escape(hero, place):
    slow_print("You try to leave...")

    if hero.flags.get("desert_boss_defeated"):
        slow_print(highlight("You escape the dungeon."))

        hero.flags["in_desert_dungeon"] = False
        hero.currentPlace = "desert"

        return True

    else:
        slow_print(danger("There is no exit."))
        return False