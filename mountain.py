from utils import slow_print, danger, lore, highlight


# =========================
# Shared Lore
# =========================
def show_mountain_lore():
    slow_print(highlight("Lore:"))
    slow_print("These mountains were once a place of balance, where time flowed cleanly.")
    slow_print(f"After the {danger('Great Blast')}, fractures formed—tears in time itself.")
    slow_print(lore("Moments repeat, overlap, and collapse."))
    slow_print("Some who enter are said to meet their past… or their end… before it happens.")
    slow_print(f"At the peak lies the {lore('Time Rift')}, where reality bends completely.")


# =========================
# Intro
# =========================
def mountainIntro(hero):

    if hero.flags.get("mountain_intro_seen", False):
        return

    slow_print("The forest thins, giving way to jagged stone and thin, freezing air.")
    slow_print("Towering mountains pierce the sky, their peaks lost in swirling clouds.")

    slow_print(danger("But something feels… wrong."))

    slow_print("Snow falls upward for a moment… then snaps back down.")
    slow_print("A distant echo of your own footsteps rings out—before you even take them.")
    slow_print(lore("Time itself is unstable here."))

    show_mountain_lore()

    hero.flags["mountain_intro_seen"] = True


# =========================
# Interaction
# =========================
def mountainInteract(hero, place):
    if not hero.flags.get("mountain_intro_seen", False):
        slow_print("You step carefully along a narrow ridge.")
        slow_print("The wind howls—but sometimes it plays in reverse.")
        slow_print(lore("Shadows move before their owners."))

        slow_print("You see a figure in the distance… it looks like you.")
        slow_print(danger("It vanishes the moment you focus on it."))

        slow_print("")
        show_mountain_lore()

        hero.flags["mountain_intro_seen"] = True

    while True:
        action = input("What would you like to do? (Observe, Climb, Exit): ").lower()

        if action == "observe":
            slow_print("You focus on your surroundings...")
            slow_print("For a split second, everything freezes.")

            slow_print(danger("Then suddenly fast-forwards—clouds race, rocks crumble, then rebuild."))

            slow_print(lore("You feel a pressure in your head… like time is trying to rewrite you."))

        elif action == "climb":
            slow_print("You begin climbing higher into the mountains...")
            slow_print("The path shifts beneath your feet—stones appear where none existed.")

            slow_print(danger("You hear your own voice whisper:"))
            slow_print("\"Turn back… you already failed once.\"")

            slow_print(lore("Something is waiting higher up… something that knows you."))

            # Cabin scene
            slow_print("")
            slow_print(highlight("You reach a small cabin hidden in the mountains."))

            slow_print("Inside, dust hangs motionless in the air.")
            slow_print("On a table rests a worn diary, marked only with the initial " + highlight("H") + ".")

            slow_print(lore("The pages are filled with frantic, uneven writing—like someone running out of time."))

            slow_print("Some words repeat. Others overwrite themselves.")
            slow_print(danger("The ink looks fresh... and ancient at the same time."))

            slow_print("")
            slow_print("You can barely make out a single idea:")

            slow_print(highlight("The Void."))

            slow_print("")
            slow_print("Further in the diary is a crude drawing:")

            slow_print(lore("A tree at the center... surrounded by five symbols:"))
            slow_print("- A Leaf")
            slow_print("- A Mountain")
            slow_print("- A Dead Tree")
            slow_print("- A Pyramid")
            slow_print("- Fire encircling the center")

            slow_print(danger("At the center of it all... something labeled only as 'The Horror'."))

        elif action == "exit":
            slow_print("You descend carefully, leaving the unstable time currents behind.")
            slow_print(lore("The world begins to feel normal again… but not entirely."))
            break

        else:
            slow_print("That is not a valid action.")