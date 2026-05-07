from utils import slow_print, danger, highlight, name
import combat
import random
from inventory import add_item


# =========================
# ENTRY
# =========================
def enter_desert_dungeon(hero, place):
    place = "desert_dungeon"

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
            show_inventory(hero)

        elif ritual_option and action in [ritual_option, "ritual"]:
            ritual_room(hero)

        elif action in [str(option_index), "escape"]:
            attempt_escape(hero, place)
            return  # exit loop cleanly

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

    def has(item):
        return item in inv and inv[item]["quantity"] > 0

    # ================= CORE RITUAL =================
    required_items = [
    "Ancient Coin",
    "Cracked Relic",
    "Time Shard",
    "Core of Time",
    "Rat King's Crown" 
]
    
    if all(has(i) for i in required_items):
        slow_print(highlight("The altar begins to resonate with every relic you carry..."))
        slow_print(danger("Time shatters completely."))

        # Grant combat ability
        hero.flags["extra_turn"] = True

        # Remove items
        for item in required_items:
            inv[item]["quantity"] -= 1
            if inv[item]["quantity"] <= 0:
                del inv[item]

        slow_print(highlight("You bend time itself. You will now act twice in battle."))

        return

    # ================= MINOR =================
    elif has("Time Shard"):
        heal = 25
        hero.health = hero.health + heal
        slow_print(f"+{heal} HP")

        inv["Time Shard"]["quantity"] -= 1
        if inv["Time Shard"]["quantity"] <= 0:
            del inv["Time Shard"]

    elif has("Cracked Relic"):
        slow_print("Your cracked relics hum on the alter and fade into fragments of time disapering slowly")
        if random.random() < 0.5:
            hero.strength += 2
            slow_print(highlight("+2 Strength"))
        else:
            hero.health -= 10
            slow_print(danger("-10 HP"))

        inv["Cracked Relic"]["quantity"] -= 1
        if inv["Cracked Relic"]["quantity"] <= 0:
            del inv["Cracked Relic"]

    else:
        slow_print("Nothing happens.")


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
        hero.health = hero.health + random.randint(5, 15)
        slow_print("+HP")

    elif effect == "damage":
        hero.health -= random.randint(5, 15)
        slow_print(danger("-HP"))

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
        hero.flags["in_desert_dungeon"] = False


# =========================
# INSPECT
# =========================
def inspect_area(hero):
    slow_print("The walls shift unnaturally...")


# =========================
# INVENTORY
# =========================
def show_inventory(hero):
    if not hero.inventory:
        slow_print("You carry nothing.")
        return

    items = ", ".join(
        f"{k} x{v['quantity']}" for k, v in hero.inventory.items()
    )
    slow_print(f"You carry: {items}")


# =========================
# ESCAPE
# =========================
def attempt_escape(hero, place):
    slow_print("You try to leave...")

    if hero.flags.get("desert_boss_defeated"):
        slow_print(highlight("You escape the dungeon."))
        hero.flags["in_desert_dungeon"] = False
        if hero.flags["in_desert_dungeon"] == False:
            place = "desert"
    else:
        slow_print(danger("There is no exit."))