from utils import slow_print, danger, lore, highlight, name

import combat


# =========================
# Shared Lore
# =========================
def show_desert_lore():
    slow_print(highlight("Lore:"))
    slow_print("These ruins were once a thriving city—built on trade, knowledge, and timekeeping.")
    slow_print("Its people studied the flow of time, charting stars and seasons with perfect precision.")

    slow_print(f"When the {danger('Great Blast')} occurred, time did not stop here.")
    slow_print(danger("It accelerated."))

    slow_print("Days became years.")
    slow_print("Years became dust.")

    slow_print("The city collapsed in on itself, aging beyond recognition in mere moments.")
    slow_print("Only this staircase remained... untouched.")

    slow_print("The Elves believe it leads to something buried long before the Blast.")
    slow_print("Something the desert was never meant to reveal.")

    slow_print("Even now, the air around it feels... wrong.")
    slow_print("Like stepping closer might pull you somewhere you cannot return from.")


# =========================
# Intro
# =========================
def desertIntro(hero):

    if hero.flags.get("desert_intro_seen", False):
        return

    slow_print("You emerge from the forest—and the world changes instantly.")
    slow_print(f"A crushing wave of heat {danger('slams')} into you, stealing the breath from your lungs.")

    slow_print("The wind howls across endless dunes, carrying grains of sand that sting your skin.")
    slow_print("The sky above is pale and empty... unnaturally still.")

    slow_print("In the distance, broken silhouettes rise from the sand—ruins of a long-dead civilization.")
    slow_print("As you approach, you realize the buildings are not just destroyed...")
    slow_print(danger("They are worn down, as if centuries passed in moments."))

    slow_print("At the center of the ruins stands a massive stone staircase descending into the earth.")
    slow_print(f"A group of {danger('goblins')} gather near its entrance, chittering nervously.")

    slow_print("They are not guarding it.")
    slow_print(highlight("They are watching it."))

    slow_print("Something cold creeps up your spine.")
    slow_print(f"Whatever lies below... even the {danger('goblins')} fear it.")

    hero.flags["desert_intro_seen"] = True


# =========================
# Interaction
# =========================
def desertInteract(hero, place):
    if not hero.flags.get("desert_interact_seen", False):
        slow_print("You stand before the staircase once more.")
        slow_print("It descends far below the desert, swallowed by darkness.")
        slow_print(f"A faint, murky aura {danger('leaks')} from its depths... pulsing slowly.")
        slow_print("")

        show_desert_lore()
        hero.flags["desert_interact_seen"] = True

    while True:
        action = input("What would you like to do (Descend or Exit): ").strip().lower()

        if action == "descend":
            if "Goblin Tooth" in hero.inventory:
                slow_print("You step past the goblins. They scatter, unwilling to follow.")
                slow_print("As you descend, the heat fades... replaced by something far worse.")
                slow_print(danger("The air grows cold. Heavy."))
                slow_print("Each step echoes longer than it should.")
                slow_print(danger("It feels like the staircase is stretching beneath your feet."))

                slow_print(highlight("You descend into the Desert Dungeon... (Feature Not Added Yet)"))
                break
            else:
                slow_print("The goblins hiss and block your path.")
                slow_print(f"You must prove your strength before entering. ({name('Goblin Tooth')} required)")
                break

        elif action == "exit":
            slow_print("You step away from the staircase.")
            slow_print(danger("For a moment... you swear something below was watching you leave."))
            break

        else:
            slow_print("Invalid action.")