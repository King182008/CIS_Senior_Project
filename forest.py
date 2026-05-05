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
        slow_print(f"The Head Elf, {npc('Galadriel')}, stands nearby.")
        slow_print("")

        show_forest_lore()
        hero.flags["forest_intro_seen"] = True

    while True:
        action = input("What would you like to do (Talk, Quest, Lore, Exit): ").lower()

        if action in ["talk", "1"]:
            talkToGaladriel(hero)

        elif action in ["quest", "2"]:
            quest_board_menu(hero, place)  # FIXED

        elif action in ["lore", "3"]:
            show_forest_lore()

        elif action == "exit":
            if not hero.flags.get("forest_outro_seen", False):
                slow_print("You step away from the Heartroot clearing.")
                slow_print("The air grows colder as the sounds of the Elves fade behind you.")
                slow_print("Whatever lies ahead… it won't be as safe as this place.")
                hero.flags["forest_outro_seen"] = True
            break

        else:
            slow_print("That is not a valid action.")


# =========================
# Dialogue
# =========================
def talkToGaladriel(hero):
    slow_print(f"You approach {npc('Galadriel')}. Her gaze is calm, but ancient.")
    slow_print("")
    slow_print("\"You have many questions,\" she says softly.")
    slow_print("\"And little time to ask them.\"")
    slow_print("")

    while True:
        choice = input("Ask about (Tree, Blast, Dragons, Leave): ").lower()

        if choice == "tree":
            slow_print(f"\"The {lore('Heartroot')} is older than memory,\" Galadriel explains.")
            slow_print("\"It binds the flow of time itself.\"")
            slow_print("\"But its power wanes. Something drains it from the shadows.\"")

        elif choice == "blast":
            slow_print(f"\"The {danger('Great Blast')} was no accident,\" she says grimly.")
            slow_print(f"\"It was the birth cry of the {npc('Horror')}\"")
            slow_print("\"Your village stood at the epicenter.\"")
            slow_print("\"That is why you alone were preserved.\"")

        elif choice == "dragons":
            slow_print(f"\"The {danger('Dragons')} were once guardians,\" Galadriel says.")
            slow_print("\"But the Blast twisted them.\"")
            slow_print("\"Now they rage endlessly, drawn to destruction.\"")

        elif choice == "leave":
            slow_print("\"Go then, hero,\" Galadriel says.")
            slow_print("\"Return if you seek guidance… or if you still draw breath.\"")
            break

        else:
            slow_print("Galadriel tilts her head slightly, not understanding your question.")