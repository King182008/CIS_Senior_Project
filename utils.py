import shop
import travel
import combat
import inventory
import time
import characterCreation
from travel import currentPlace

def actions(hero):

    currentPlace = travel.currentPlace

    while True:
        action = input("What would you like to do? (Shop, Travel, Save, Combat, Interact, Inventory, Stop) ").strip().lower()

        # Ensure hero exists
        if hero is None:
            print("No character loaded. Exiting.")
            break

        if action == "shop" or action == "1":
            shop.display_shop(currentPlace, hero)

        elif action == "travel" or action == "2":
            currentPlace = travel.travel(currentPlace, hero)

        elif action == "save" or action == "3":
            slot = characterCreation.choose_slot()
            hero.save_character(slot)

        elif action == "combat" or action == "4":
            if currentPlace in combat.Enemies and combat.Enemies[currentPlace]:
                enemy_type = combat.Enemies[currentPlace][0] 
                enemy = combat.create_enemy(enemy_type)        # Create a fresh Enemy object
                result = combat.display_enemy(enemy, hero)

            if result == "dead":
                characterCreation.delete_save(slot)
                break

        elif action == "inventory" or action == "5":
            inventory.show_inventory(hero)
        
        elif action == "interact" or action == "6":
            from forest import forestInteract
            INTERACTIONS = {
                "forest": forestInteract,
            }
            INTERACTIONS[currentPlace](hero, currentPlace)

        elif action == "stop":
            print("Exiting game.")
            break

        else:
            print("Invalid action. Please choose Shop, Travel, Save, Combat, Inventory, or Stop.")

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

forest_quest_board = {
    "Rat Problem": {
        "requirements": {"Rat Tail": 3},
        "reward": {"gold": 10, "xp": 5},
        "completed": False
    },
    "Goblin Threat": {
        "requirements": {"Goblin Ear": 2},
        "reward": {"gold": 20, "xp": 10},
        "completed": False
    },
    "Dragon Slayer": {
        "requirements": {"Dragon Scale": 1},
        "reward": {"gold": 100, "xp": 50},
        "completed": False
    }
}

quest_boards = {
    "forest": forest_quest_board
}

def handle_quest(hero, quest_name):
    quest = quest_boards[currentPlace][quest_name]

    if hero.quest_log.get(quest_name, False):
        slow_print("You already completed this quest.")
        return

    # Check requirements
    for item, qty in quest["requirements"].items():
        if hero.inventory.get(item, {}).get("quantity", 0) < qty:
            slow_print(f"You need {qty}x {item}.")
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

    slow_print(f"Quest Complete: {quest_name}")
    slow_print(f"+{quest['reward']['gold']} gold, +{quest['reward']['xp']} XP")

def quest_board_menu(hero):
    while True:
        print("\n--- Quest Board ---")

        board = quest_boards[currentPlace]

        for name, quest in board.items():
            status = "Complete" if hero.quest_log.get(name, False) else "Incomplete"
            print(f"- {name} ({status})")

        choice = input("\nSelect quest or type 'exit': ").title()

        if choice == "Exit":
            break

        if choice in board:
            handle_quest(hero, choice)
        else:
            slow_print("Invalid quest.")