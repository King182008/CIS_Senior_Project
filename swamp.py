from utils import slow_print, danger, lore, highlight, name
import combat
import sys


# =========================
# Shared Lore
# =========================
def show_swamp_lore():
    slow_print(highlight("Lore:"))
    slow_print("The swamp was not always like this.")

    slow_print("Long ago, this land was a quiet river basin, fed by clear waters from the mountains.")
    slow_print("Villages once stood here, thriving in peace.")

    slow_print(f"Then came the {danger('Great Blast')}.")

    slow_print("The rivers slowed... then stopped.")
    slow_print("Water pooled where it should not, rotting into thick, unmoving marsh.")
    slow_print(lore("Time itself began to decay here—lingering, stretching, refusing to move on."))

    slow_print("Creatures that died did not stay dead.")
    slow_print("Some rose again. Others... simply never left.")

    slow_print(danger("The air feels heavy, as if each breath is being watched."))
    slow_print("Whispers drift across the water, carried without wind.")

    slow_print("The Elves believe the swamp is where time goes to die.")
    slow_print(lore("Where broken moments collect and fester."))


# =========================
# Intro
# =========================
def swampIntro(hero):
    if hero.flags.get("swamp_intro_seen", False):
        return

    slow_print("Through the waves of heat you stumble toward a dark shaded area.")
    
    show_swamp_lore()

    hero.flags["swamp_intro_seen"] = True


# =========================
# Interaction
# =========================
def swampInteract(hero, place):
    if not hero.flags.get("swamp_interact_seen", False):
        slow_print("At the center of the swamp, something remains untouched by decay.")
        slow_print("A stone pedestal... dry, untouched by time or rot.")
        slow_print(lore("As if whatever rests here is being preserved... or protected."))

        slow_print("You feel a quiet intelligence behind it.")
        slow_print(danger("Something ancient. Something patient."))

        hero.flags["swamp_interact_seen"] = True

    while True:
        action = input("What would you like to do? (Inspect or Exit): ").strip().lower()

        if action == "inspect":
            slow_print("A letter and pen rest atop the pedestal.")
            slow_print(highlight("The Letter says:"))

            slow_print("No blood I shed, yet wars I lead,")
            slow_print("With silent moves, I plant the seed.")
            slow_print("Surrounded close, I must be kept")
            slow_print("If I fall, all hope has wept.")
            slow_print("Though slow I move, I'm worth it all")
            slow_print("Who am I that cannot fall?")

            answer = input("What is the answer? ").strip().lower()
            if hero.flags.get("rat_king_defeated", False):
                slow_print("The pedestal is silent. Whatever was bound here is gone.")
                continue

            if answer in ["king", "a king"]:
                slow_print(f"As you write '{answer}', the ground trembles...")
                slow_print(danger("Something claws its way to the surface."))

                enemy = combat.create_enemy("Rat King")
                result = combat.display_enemy(enemy, hero)

                if result != "dead":
                    hero.flags["rat_king_defeated"] = True

            else:
                slow_print("Nothing happens...")

        elif action == "exit":
            slow_print("You step away from the pedestal.")
            break

        elif action == "witch":
            slow_print(danger("A mysterious figure appears from the mist..."))
            slow_print("Before you can react, everything goes dark.")
            slow_print(highlight("You have been suffocated by giant breasts."))
            slow_print(danger("You Died"))
            sys.exit()

        else:
            slow_print("Invalid action.")