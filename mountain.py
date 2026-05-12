from utils import slow_print, danger, lore, highlight, name, npc


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
    if not hero.flags.get("mountain_interact_seen", False):
        hero.flags["mountain_interact_seen"] = True

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
        print(highlight("\n=== MOUNTAIN INTERACTION ==="))
        print("-" * 40)
        print(f"1. {name('Observe the Rift')}")
        print(f"2. {name('Climb Higher')}")
        print(f"3. {name('Lore')}")
        print(f"4. {danger('Leave Mountains')}")
        print("-" * 40)

        action = input(highlight("Choose an action (1-4 or name): ")).strip().lower()

        # =========================
        # OBSERVE
        # =========================
        if action in ["1", "observe", "rift"]:
            slow_print("You focus on your surroundings...")
            slow_print("For a split second, everything freezes.")

            slow_print(danger("Then suddenly fast-forwards—clouds race, rocks crumble, then rebuild."))

            slow_print(lore("You feel a pressure in your head… like time is trying to rewrite you."))

        # =========================
        # CLIMB
        # =========================
        elif action in ["2", "climb", "higher"]:
            slow_print("You begin climbing higher into the mountains...")
            slow_print("The path shifts beneath your feet—stones appear where none existed.")

            slow_print(danger("You hear your own voice whisper:"))
            slow_print("\"Turn back… you already failed once.\"")

            slow_print(lore("Something is waiting higher up… something that knows you."))

            # Cabin scene
            slow_print("")
            slow_print(highlight("You reach a small cabin hidden in the mountains."))

            slow_print("Inside, dust hangs motionless in the air.")
            slow_print(f"On a table rests a worn diary, marked only with the initial {highlight('H')}.")

            slow_print(lore("The pages are filled with frantic, uneven writing—like someone running out of time."))

            slow_print("Some words repeat. Others overwrite themselves.")
            slow_print(danger("The ink looks fresh... and ancient at the same time."))

            slow_print("")
            slow_print("You can barely make out a single idea:")
            slow_print(highlight("The Void."))

            slow_print("")
            slow_print("Further in the diary is a crude drawing:")

            slow_print(lore("A tree at the center... surrounded by five symbols:"))
            slow_print(f"- {name('A Leaf')}")
            slow_print(f"- {name('A Mountain')}")
            slow_print(f"- {name('A Dead Tree')}")
            slow_print(f"- {name('A Pyramid')}")
            slow_print(f"- {name('Fire encircling the center')}")

            slow_print(danger("At the center of it all... something labeled only as 'The Horror'."))

            while True:
                print("")
                print(highlight("\n=== THE DIARY ==="))
                print("-" * 40)
                print(f"1. {name('Continue Reading')}")
                print(f"2. {danger('Close the Diary')}")
                print("-" * 40)

                read_choice = input(highlight("Choose an action (1-2 or name): ")).strip().lower()

                # =========================
                # CONTINUE READING
                # =========================
                if read_choice in ["1", "continue", "read", "continue reading"]:

                    slow_print("")
                    slow_print(lore("The writing grows worse the deeper you read."))
                    slow_print(lore("Entire sentences overlap each other, as if written hundreds of times."))

                    slow_print("")
                    slow_print(danger("\"") + f"{npc('Time')} {danger('is not breaking.')}\"")
                    slow_print(danger("\"It already broke.\""))

                    slow_print("")
                    slow_print("Several pages are scratched out violently.")
                    slow_print("Yet the words beneath still somehow remain visible.")

                    slow_print("")
                    slow_print(lore("\"The Void does not exist somewhere.\""))
                    slow_print(lore("\"It exists between moments.\""))

                    slow_print("")
                    slow_print("You turn another page.")

                    slow_print(danger("Your own handwriting stares back at you."))

                    slow_print("")
                    slow_print("\"I saw the tree again.\"")
                    slow_print("\"Five roots. Five paths.\"")
                    slow_print("\"Every path ends the same way.\"")

                    slow_print("")
                    slow_print(highlight("THE HORROR WAITS AT THE CENTER."))

                    slow_print("")
                    slow_print("The next pages make less and less sense.")

                    slow_print(lore("\"The mountain remembers names that no longer exist.\""))
                    slow_print(lore("\"The dead speak backwards beyond the Rift.\""))
                    slow_print(lore("\"The stars are moving closer every loop.\""))

                    slow_print("")
                    slow_print(f"One page {npc('is')} completely covered in repeated words:")

                    for _ in range(3):
                        slow_print(danger("DON'T LOOK INTO THE VOID DON'T LOOK INTO ") + npc("THE") + danger(" VOID DON'T LOOK INTO THE VOID"))
                    slow_print("")
                    slow_print("At the very end of the diary, one final sentence remains.")

                    slow_print("")
                    slow_print(highlight(f"\"If you are reading this... it means the {npc('Horror')}")  + highlight(" noticed you too.\""))
                    slow_print("")
                    slow_print(danger("The cabin suddenly creaks around you."))

                    break

                # =========================
                # EXIT
                # =========================
                elif read_choice in ["2", "exit", "close", "leave", "close diary"]:

                    slow_print("")
                    slow_print("You close the diary.")
                    slow_print(lore("For a moment, the whispering inside the cabin stops."))

                    slow_print("")
                    slow_print(danger("But deep in the mountains... something still watches."))

                    break

                else:
                    slow_print(danger("Invalid choice."))


        # =========================
        # LORE
        # =========================
        elif action in ["3", "lore"]:
            show_mountain_lore()

        # =========================
        # EXIT
        # =========================
        elif action in ["4", "exit", "leave"]:
            if not hero.flags.get("mountain_outro_seen", False):
                slow_print("You descend carefully, leaving the unstable time currents behind.")
                slow_print(lore("The world begins to feel normal again… but not entirely."))
                hero.flags["mountain_outro_seen"] = True
            break

        else:
            slow_print(danger("Invalid choice. Please select 1–4."))