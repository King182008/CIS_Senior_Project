import characterCreation
import tutorial



if __name__ == "__main__":
    from utils import highlight, danger, name, lore

    hero = None

    print(highlight("\n================================"))
    print(highlight("      TEXT RPG ADVENTURE"))
    print(highlight("================================"))

    while True:

        print(highlight("\n=== MAIN MENU ==="))
        print(f"1. {highlight('New Game')}")
        print(f"2. {highlight('Load Game')}")
        print(f"3. {highlight('Show Save Slots')}")
        print(f"4. {danger('Exit')}")
        print("-" * 35)

        choice = input("Select option (1-4 or name): ").strip().lower()

        # =========================
        # NEW GAME
        # =========================
        if choice in ["1", "new"]:
            hero = characterCreation.create_character()

            characterCreation.show_slots()
            slot = characterCreation.choose_slot()

            hero.save_character(slot)
            hero.slot = slot

            characterCreation.hero = hero

            print(lore("\nStarting tutorial...\n"))
            tutorial.Begin_tutorial(hero)
            break

        # =========================
        # LOAD GAME
        # =========================
        elif choice in ["2", "load"]:
            characterCreation.show_slots()

            slot = characterCreation.choose_slot()
            hero = characterCreation.Character.load_character(slot)

            if hero:
                hero.slot = slot

                print(lore(f"\nWelcome back, {name(hero.name)}!\n"))

                from utils import actions
                actions(hero)

                break
            else:
                print(danger("Failed to load game. Try again."))

        # =========================
        # SHOW SLOTS
        # =========================
        elif choice in ["3", "show"]:
            characterCreation.show_slots()

        # =========================
        # EXIT
        # =========================
        elif choice in ["4", "exit"]:
            print(danger("Exiting game..."))
            break

        else:
            print(danger("Invalid choice. Please try again."))