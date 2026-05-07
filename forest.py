from utils import (
    quest_board_menu,
    slow_print,
    actions,
    name, npc, danger, lore, highlight
)

# =========================
# Shared Lore Function
# =========================
def show_forest_lore():
    slow_print(highlight("Lore:"))
    slow_print(f"The {lore('Heartroot')} is the last anchor of ancient time magic.")
    slow_print(f"After the {danger('Great Blast')}, the Elves bound time itself into this tree.")
    slow_print("Without it, the world would have fallen into chaos.")
    slow_print("But the magic is fading… and something feeds on it from the shadows.")


# =========================
# Intro
# =========================
def ForestIntro(hero):
    slow_print("... ... ...")
    slow_print("Mother! Come! Quick!")
    slow_print(f"{name(hero.name)} is waking up.")
    slow_print("Good Morning Darling. I'm glad to see you're finally awake.")
    slow_print(f"It's been 100 years since the {danger('Great Blast')}.")
    slow_print("You were the only survivor from your village.")
    slow_print("We've kept you alive in hibernation with time magic.")
    slow_print(f"The {npc('Horror')}'s creation affected much of the world.")
    slow_print("Many beasts have emerged over the years.")
    slow_print(f"The {danger('Dragons')} currently wreak havoc in the mountains and volcano.")
    slow_print("We need your help, hero. Good luck!")
    actions(hero)


# =========================
# Forest Interaction
# =========================
def forestInteract(hero, place):
    if not hero.flags.get("forest_intro_seen", False):
        slow_print("You look around to see a vast clearing, bathed in soft golden light.")
        slow_print(f"At its center stands the {lore('Heartroot')}, an enormous ancient tree.")
        slow_print("Its trunk is wider than a castle tower.")
        slow_print("Its leaves shimmer faintly, pulsing with lingering time magic.")
        slow_print("Elegant wooden structures spiral around the trunk, forming the home of the Elves.")
        slow_print("Elves move gracefully between platforms, watching you with quiet curiosity.")
        slow_print("Beyond the clearing, a dense forest stretches endlessly, dark and whispering.")
        slow_print("You feel it… something in the woods is watching.")
        slow_print(f"The Head Elf, {npc('Galadriel')}, stands nearby.\n")

        show_forest_lore()
        hero.flags["forest_intro_seen"] = True

    while True:
        print(highlight("\n=== FOREST INTERACTION ==="))
        print("-" * 40)
        print(f"1. {name('Talk to Galadriel')}")
        print(f"2. {name('Quest Board')}")
        print(f"3. {name('Lore')}")
        print(f"4. {danger('Exit Forest')}")
        print("-" * 40)

        action = input(highlight("Choose an action (1-4 or name): ")).strip().lower()

        # =========================
        # TALK
        # =========================
        if action in ["1", "talk", "galadriel"]:
            talkToGaladriel(hero)

        # =========================
        # QUESTS
        # =========================
        elif action in ["2", "quest"]:
            quest_board_menu(hero)

        # =========================
        # LORE
        # =========================
        elif action in ["3", "lore"]:
            show_forest_lore()

        # =========================
        # EXIT
        # =========================
        elif action in ["4", "exit"]:
            if not hero.flags.get("forest_outro_seen", False):
                slow_print("You step away from the Heartroot clearing.")
                slow_print("The air grows colder as the sounds of the Elves fade behind you.")
                slow_print("Whatever lies ahead… it won't be as safe as this place.")
                hero.flags["forest_outro_seen"] = True
            break

        else:
            slow_print(danger("Invalid choice. Please select 1–4."))
# =========================
# Dialogue
# =========================
def talkToGaladriel(hero):
    slow_print(f"You approach {npc('Galadriel')}. Her gaze is calm, but ancient.")
    slow_print("\"You have many questions,\" she says softly.")
    slow_print("\"And little time to ask them.\"\n")

    while True:
        print(highlight("\n=== GALADRIEL DIALOGUE ==="))
        print("-" * 40)
        print(f"1. {name('Ask about the Heartroot')}")
        print(f"2. {name('Ask about the Great Blast')}")
        print(f"3. {name('Ask about the Dragons')}")
        print(f"4. {danger('Leave conversation')}")
        print("-" * 40)

        choice = input(highlight("Choose (1–4 or name): ")).strip().lower()

        # =========================
        # HEARTROOT
        # =========================
        if choice in ["1", "tree", "heartroot"]:
            slow_print(f"\"The {lore('Heartroot')} is older than memory,\" Galadriel explains.")
            slow_print("\"It binds the flow of time itself.\"")
            slow_print("\"But its power wanes. Something drains it from the shadows.\"")

        # =========================
        # GREAT BLAST
        # =========================
        elif choice in ["2", "blast", "great blast"]:
            slow_print(f"\"The {danger('Great Blast')} was no accident,\" she says grimly.")
            slow_print(f"\"It was the birth cry of the {npc('Horror')}\"")
            slow_print("\"Your village stood at the epicenter.\"")
            slow_print("\"That is why you alone were preserved.\"")

        # =========================
        # DRAGONS
        # =========================
        elif choice in ["3", "dragons"]:
            slow_print(f"\"The {danger('Dragons')} were once guardians,\" Galadriel says.")
            slow_print("\"But the Blast twisted them.\"")
            slow_print("\"Now they rage endlessly, drawn to destruction.\"")

        # =========================
        # EXIT
        # =========================
        elif choice in ["4", "leave", "exit"]:
            slow_print("\"Go then, hero,\" Galadriel says.")
            slow_print("\"Return if you seek guidance… or if you still draw breath.\"")
            break

        else:
            slow_print(danger("Galadriel does not understand your question."))