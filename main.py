import characterCreation
import tutorial
from travel import currentPlace

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
            hero.slot = slot
            characterCreation.hero = hero
            tutorial.Begin_tutorial(hero)
            break

        elif choice == "load":
            characterCreation.show_slots()
            slot = characterCreation.choose_slot()
            hero = characterCreation.Character.load_character(slot)
            from utils import actions
            if hero:
                hero.slot = slot

                from utils import actions
                actions(hero, currentPlace)

                print(f"Character loaded: {hero.name}")
                break
            else:
                print("Failed to load. Try again or start a new game.")

        elif choice == "show":
            characterCreation.show_slots()

        else:
            print("Invalid choice. Please choose New, Load, or Show.")
