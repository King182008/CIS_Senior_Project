import time

# =========================
# Utility
# =========================
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# =========================
# COLOR SYSTEM
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


def name(text): return c(text, Color.CYAN)
def npc(text): return c(text, Color.MAGENTA)
def danger(text): return c(text, Color.RED)
def lore(text): return c(text, Color.GREEN)
def highlight(text): return c(text, Color.YELLOW)


# =========================
# MAIN ACTION LOOP
# =========================
def actions(hero):
    import travel, shop, characterCreation, combat, inventory

    while True:

        if hero is None:
            print(danger("No character loaded. Exiting."))
            break

        place = hero.currentPlace

        print(highlight("\n=== ACTION MENU ==="))
        print(f"Location: {name(place.title())}")
        print("-" * 40)

        print(f"1. {highlight('Shop')}")
        print(f"2. {highlight('Travel')}")
        print(f"3. {highlight('Save')}")
        print(f"4. {highlight('Combat')}")
        print(f"5. {highlight('Inventory')}")
        print(f"6. {highlight('Interact')}")
        print(f"7. {danger('Stop')}")
        print("-" * 40)

        action = input("Choose action (1-7 or name): ").strip().lower()

        # SHOP
        if action in ["1", "shop"]:
            shop.display_shop(place, hero)

        # TRAVEL
        elif action in ["2", "travel"]:
            hero.currentPlace = travel.travel(place, hero)

        # SAVE
        elif action in ["3", "save"]:
            print(highlight("\n=== SAVE GAME ==="))
            characterCreation.show_slots()
            slot = characterCreation.choose_slot()
            hero.save_character(slot)

        # COMBAT
        elif action in ["4", "combat"]:
            enemies = combat.Enemies.get(place)

            if not enemies:
                slow_print(lore(f"The {name(place)} is peaceful..."))
                continue

            enemy = combat.create_enemy(enemies[0])
            result = combat.display_enemy(enemy, hero)

            if result == "dead":
                characterCreation.delete_save(hero.slot)
                break

        # INVENTORY
        elif action in ["5", "inventory"]:
            inventory.show_inventory(hero)

        # INTERACT
        elif action in ["6", "interact"]:
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

            if place in INTERACTIONS:
                INTERACTIONS[place](hero, place)
            else:
                slow_print(danger(f"Nothing to interact with in {name(place)}."))

        # EXIT
        elif action in ["7", "stop"]:
            print(danger("Exiting game..."))
            break

        else:
            print(danger("Invalid action."))


# =========================
# QUEST SYSTEM
# =========================
forest_quest_board = {
    "Rat Problem": {"requirements": {"Rat Tail": 3}, "reward": {"gold": 10, "xp": 5}},
    "Goblin Threat": {"requirements": {"Goblin Tooth": 2}, "reward": {"gold": 20, "xp": 10}},
    "Dragon Slayer": {"requirements": {"Dragon Scale": 1}, "reward": {"gold": 100, "xp": 50}}
}

swamp_quest_board = {
    "Giant Rat Problem": {"requirements": {"Rat King's Crown": 3}, "reward": {"gold": 10, "xp": 5}}
}

quest_boards = {
    "forest": forest_quest_board,
    "swamp": swamp_quest_board
}


# =========================
# QUEST HANDLER
# =========================
def handle_quest(hero, quest_name):
    board = quest_boards[hero.currentPlace]
    quest = board[quest_name]

    if hero.quest_log.get(quest_name):
        slow_print(danger(f"Already completed {name(quest_name)}."))
        return

    # Check requirements
    for item, qty in quest["requirements"].items():
        if hero.inventory.get(item, {}).get("quantity", 0) < qty:
            slow_print(f"{danger('Missing:')} {highlight(qty)}x {name(item)}")
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

    slow_print(highlight("=== QUEST COMPLETE ==="))
    slow_print(name(quest_name))
    slow_print(
        f"{highlight('+')} {highlight(quest['reward']['gold'])} gold | "
        f"{highlight(quest['reward']['xp'])} XP"
    )


# =========================
# QUEST MENU
# =========================
def quest_board_menu(hero):
    while True:
        place = hero.currentPlace
        board = quest_boards[place]

        print(highlight(f"\n=== {place.upper()} QUEST BOARD ==="))
        print("-" * 40)

        for q_name in board:
            complete = hero.quest_log.get(q_name, False)
            status = highlight("✔ Complete") if complete else danger("✘ Incomplete")
            print(f"{name(q_name):<25} {status}")

        print("-" * 40)

        choice = input(f"Select quest or {danger('exit')}:\n>> ").strip().lower()

        if choice.lower() == "exit":
            break

        normalized_choice = choice.title()

        if normalized_choice in board:
            handle_quest(hero, normalized_choice)
        else:
            slow_print(danger("Invalid quest."))