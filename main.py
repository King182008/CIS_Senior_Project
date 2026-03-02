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
            slot = characterCreation.choose_slot()
            hero = characterCreation.Character.load_character(slot)
            if hero is not None:
                print(f"Character loaded: {hero.name}")
                characterCreation.hero = hero
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
        if characterCreation.hero is None:
            print("No character loaded. Exiting.")
            break

        if action == "shop":
            shop.display_shop(currentPlace, characterCreation.hero)

        elif action == "travel":
            currentPlace = travel.travel(currentPlace)

        elif action == "save":
            slot = characterCreation.choose_slot()
            characterCreation.hero.save_character(slot)

        elif action == "combat":
            if currentPlace in combat.Enemies and combat.Enemies[currentPlace]:
                enemy = combat.Enemies[currentPlace][0]  # Get the first enemy for the current location
                combat.display_enemy(enemy)
            else:
                print("No enemies here.")

        elif action == "inventory":
            inventory.show_inventory()

        elif action == "stop":
            print("Exiting game.")
            break

        else:
            print("Invalid action. Please choose Shop, Travel, Save, Combat, Inventory, or Stop.")