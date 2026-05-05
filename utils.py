import time


# =========================
# Color System
# =========================
class Color:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RED = "\033[91m"
    YELLOW = "\033[93m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

# Semantic helpers
def name(text): return c(text, Color.CYAN)
def npc(text): return c(text, Color.MAGENTA)
def danger(text): return c(text, Color.RED)
def lore(text): return c(text, Color.GREEN)
def highlight(text): return c(text, Color.YELLOW)

# =========================
# Utility
# =========================
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# =========================
# Actions Loop
# =========================
def actions(hero, currentPlace):
    import combat
    import shop
    import characterCreation
    import inventory
    while True:
        action = input(
            f"\nWhat would you like to do? "
            f"({highlight('Shop')}, {highlight('Travel')}, {highlight('Save')}, "
            f"{highlight('Combat')}, {highlight('Interact')}, {highlight('Inventory')}, {highlight('Stop')}): "
        ).strip().lower()

        if hero is None:
            print("No character loaded. Exiting.")
            break

        if action in ["shop", "1"]:
            shop.display_shop(currentPlace, hero)

        elif action in ["travel", "2"]:
            import travel  # ✅ local import avoids circular dependency
            currentPlace = travel.travel(currentPlace, hero)

        elif action in ["save", "3"]:
            slot = characterCreation.choose_slot()
            hero.save_character(slot)

        elif action in ["combat", "4"]:

            enemies = combat.Enemies.get(currentPlace, None)

            if not enemies or len(enemies) == 0:
                slow_print(lore(f"The {currentPlace} is quiet..."))
                slow_print("There is nothing to fight here.")
                slow_print("Try interacting with the area instead.")
                continue

            enemy_type = enemies[0]
            enemy = combat.create_enemy(enemy_type)
            result = combat.display_enemy(enemy, hero)

            if result == "dead":
                characterCreation.delete_save(hero.slot)
                break

        elif action in ["inventory", "5"]:
            inventory.show_inventory(hero)

        elif action in ["interact", "6"]:
            from forest import forestInteract
            from desert import desertInteract
            from swamp import swampInteract
            from mountain import mountainInteract
            from volcano import volcanoInteract
            from void import voidInteract

            INTERACTIONS = {
                "forest": forestInteract,
                "desert": desertInteract,
                "swamp": swampInteract,
                "mountains": mountainInteract,
                "volcano": volcanoInteract,
                "void": voidInteract
            }

            key = currentPlace.strip().lower()

            if key in INTERACTIONS:
                INTERACTIONS[key](hero, currentPlace)
            else:
                slow_print(f"No interaction defined for {danger(currentPlace)}.")

        elif action == "stop":
            print("Exiting game.")
            break

        else:
            print("Invalid action.")

# =========================
# Quest Boards
# =========================
forest_quest_board = {
    "Rat Problem": {
        "requirements": {"Rat Tail": 3},
        "reward": {"gold": 10, "xp": 5}
    },
    "Goblin Threat": {
        "requirements": {"Goblin Tooth": 2},
        "reward": {"gold": 20, "xp": 10}
    },
    "Dragon Slayer": {
        "requirements": {"Dragon Scale": 1},
        "reward": {"gold": 100, "xp": 50}
    }
}

swamp_quest_board = {
    "Giant Rat Problem": {
        "requirements": {"Rat King's Crown": 3},
        "reward": {"gold": 10, "xp": 5}
    }
}

quest_boards = {
    "forest": forest_quest_board,
    "swamp": swamp_quest_board
}

# =========================
# Quest Logic
# =========================
def handle_quest(hero, quest_name, currentPlace):
    board = quest_boards[currentPlace]
    quest = board[quest_name]

    if hero.quest_log.get(quest_name, False):
        slow_print(f"You already completed {name(quest_name)}.")
        return

    # Check requirements
    for item, qty in quest["requirements"].items():
        if hero.inventory.get(item, {}).get("quantity", 0) < qty:
            slow_print(f"You need {highlight(qty)}x {name(item)}.")
            return

    # Remove items
    for item, qty in quest["requirements"].items():
        hero.inventory[item]["quantity"] -= qty
        if hero.inventory[item]["quantity"] <= 0:
            del hero.inventory[item]

    # Rewards
    hero.gold += quest["reward"]["gold"]
    hero.xp += quest["reward"]["xp"]
    hero.quest_log[quest_name] = True

    slow_print(f"{highlight('Quest Complete')}: {name(quest_name)}")
    slow_print(f"+{highlight(quest['reward']['gold'])} gold, +{highlight(quest['reward']['xp'])} XP")

# =========================
# Quest Menu
# =========================
def quest_board_menu(hero, currentPlace):
    while True:
        print(f"\n{highlight('--- Quest Board ---')}")

        board = quest_boards[currentPlace]

        for q_name, quest in board.items():
            status = highlight("Complete") if hero.quest_log.get(q_name, False) else "Incomplete"
            print(f"- {name(q_name)} ({status})")

        choice = input("\nSelect quest or type 'exit': ").title()

        if choice == "Exit":
            break

        if choice in board:
            handle_quest(hero, choice, currentPlace)
        else:
            slow_print("Invalid quest.")