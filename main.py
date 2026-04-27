import characterCreation
import tutorial

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
            tutorial.Begin_tutorial(hero)  # Start the tutorial
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
