import characterCreation
import shop
import travel
import combat
import inventory

if __name__ == "__main__":
    # -------------------- CHARACTER CREATION / LOAD --------------------
    hero = None

    while True:
        choice = input("New Game, Load Game or Show Slots? (New, Load, Show) ").strip().lower()

        if choice == "new":
            hero = characterCreation.create_character()
            characterCreation.show_slots()
            slot = characterCreation.choose_slot()
            hero.save_character(slot)
            characterCreation.hero = hero  # set global hero
            break

        elif choice == "load":
            characterCreation.show_slots()
            slot = characterCreation.choose_slot()        # ONLY CALLED ONCE
            hero = characterCreation.Character.load_character(slot)

            if hero:
                current_slot = slot
                print(f"Character loaded: {hero.name}")
                break
            else:
                print("Failed to load. Try again or start a new game.")

        elif choice == "show":
            characterCreation.show_slots()

        else:
            print("Invalid choice. Please choose New, Load, or Show.")

    # -------------------- MAIN ACTION LOOP --------------------
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