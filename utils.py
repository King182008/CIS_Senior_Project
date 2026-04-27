import shop
import travel
import combat
import inventory
import time
import characterCreation

def actions(hero):

    currentPlace = travel.currentPlace

    while True:
        action = input("What would you like to do? (Shop, Travel, Save, Combat, Inventory, Stop) ").strip().lower()

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