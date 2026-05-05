from utils import slow_print, danger, lore, highlight
import combat


# =========================
# Shared Lore
# =========================
def show_void_lore():
    slow_print(highlight("Lore:"))
    slow_print("This is the Void—the birthplace of the Horror.")
    slow_print(lore("Not a place, but the absence of everything."))
    slow_print(lore("Time does not flow here. It fractures."))
    slow_print(danger("The Horror was not born… it leaked into existence."))
    slow_print(danger("And now it spreads, consuming reality piece by piece."))


# =========================
# Intro
# =========================
def voidIntro(hero):

    if hero.flags.get("void_intro_seen", False):
        return

    slow_print("You step beyond the edge of the known world… and something feels wrong immediately.")

    slow_print(danger("There is no wind. No sound. Not even your own footsteps."))
    slow_print("")

    slow_print(lore("The ground beneath you shifts—not like earth, but like a memory trying to hold its shape."))

    slow_print("Fragments of places you've been flicker in and out of existence around you.")
    slow_print("The forest burns… then regrows.")
    slow_print("The desert collapses… then stands whole again.")
    slow_print("")

    slow_print(danger("Time does not move here."))
    slow_print(danger("It stutters. Repeats. Breaks."))
    slow_print("")

    slow_print("A pressure builds in your chest, as if something vast is aware of you.")
    slow_print(lore("Not watching… but remembering."))
    slow_print("")

    slow_print("This is not a place.")
    slow_print(highlight("This is where reality ends."))
    slow_print("")
    slow_print(danger("This… is where the Horror began."))

    show_void_lore()

    hero.flags["void_intro_seen"] = True


# =========================
# Interaction
# =========================
def voidInteract(hero, place):
    if not hero.flags.get("void_intro_seen", False):
        slow_print("You step forward… but the ground does not respond.")
        slow_print(lore("It feels like you are moving, yet nothing changes."))

        slow_print("The world around you flickers—like a memory struggling to exist.")
        slow_print("")

        slow_print(danger("A voice echoes… not from ahead, but from within you."))
        slow_print("\"You should not be here.\"")

        slow_print("")
        slow_print("Shapes form in the distance—places you've been before.")
        slow_print("The forest. The desert. The mountains.")
        slow_print(danger("All of them… collapsing into nothing."))

        slow_print("")
        show_void_lore()

        slow_print("")
        slow_print(danger("Something here recognizes you."))

        hero.flags["void_intro_seen"] = True

    while True:
        action = input("What would you like to do? (Call, Observe, Advance, Exit): ").lower()

        if action == "observe":
            slow_print("You try to focus on your surroundings...")

            slow_print(lore("For a moment, you see countless versions of yourself."))
            slow_print("Some wounded. Some stronger. Some… dead.")

            slow_print(danger("They all turn and look at you at the same time."))
            slow_print("Then they vanish.")

        elif action == "call":
            slow_print("You call out into the emptiness...")

            slow_print(danger("Your voice echoes back—distorted."))
            slow_print("\"...hero...error...zero...\"")

            slow_print(lore("The Void does not understand you… but it is learning."))

        elif action == "advance":
            slow_print("You force yourself forward.")
            slow_print(danger("Each step feels heavier, like reality is resisting you."))

            slow_print("")
            slow_print(highlight("A shape begins to form ahead..."))

            slow_print(lore("It twists, pulling pieces of the world into itself."))
            slow_print("Eyes. Limbs. Shadows. Time itself.")

            slow_print("")
            slow_print(danger("The Horror sees you."))

            # Boss encounter
            enemy = combat.create_enemy("Cuthulu")
            result = combat.display_enemy(enemy, hero)

            if result == "dead":
                return
            else:
                slow_print(danger("The Void trembles… but it is not gone."))
                slow_print(lore("You have only scratched the surface of something far worse."))

        elif action == "exit":
            slow_print("You step back… or perhaps the Void lets you leave.")
            slow_print(lore("The world slowly reforms around you."))

            slow_print(danger("But something followed you… you can feel it."))
            break

        else:
            slow_print("That is not a valid action.")