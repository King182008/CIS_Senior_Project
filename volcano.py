from utils import (
    slow_print,
    danger,
    lore,
    highlight,
    name,
    actions
)
import combat


# =========================
# Shared Lore
# =========================
def show_volcano_lore():
    slow_print(highlight("Lore:"))
    slow_print("Once, Dragons were guardians of balance—keepers of fire and renewal.")
    slow_print(f"After the {danger('Great Blast')}, they were twisted into beings of pure destruction.")
    slow_print(danger("Now they hoard flame, rage, and ruin."))
    slow_print(f"At the heart of the volcano lies their strongest—an {lore('Ancient Dragon')}.")
    slow_print(danger("You feel its presence watching you."))


# =========================
# Intro
# =========================
def volcanoIntro(hero):
    slow_print("... ... ...")
    slow_print("The air thickens.")
    slow_print("Heat presses against your skin like a warning.")

    slow_print(f"You approach a mountain split open by the {danger('Great Blast')}.")
    slow_print("Molten light spills from its core, pulsing like a heartbeat.")

    slow_print(danger("A roar echoes from above—deep, ancient, alive."))

    slow_print("This is no natural place.")
    slow_print(highlight("This is Dragon territory."))

    show_volcano_lore()


# =========================
# Interaction
# =========================
def volcanoInteract(hero, place):
    if not hero.flags.get("volcano_intro_seen", False):
        slow_print("You step onto blackened stone, heat radiating in waves.")
        slow_print("Cracks glow beneath your feet, filled with slow-moving lava.")
        slow_print("The sky burns red through thick smoke.")
        slow_print("")

        slow_print("Massive bones lie scattered across the terrain.")
        slow_print(danger("Nothing survives here for long."))

        slow_print("")
        slow_print("High above, shadows circle through the smoke.")
        slow_print(danger("You are not alone."))

        hero.flags["volcano_intro_seen"] = True

    while True:
        print(highlight("\n=== VOLCANO INTERACTION ==="))
        print("-" * 40)
        print(f"1. {name('Explore the Volcano')}")
        print(f"2. {name('Challenge a Dragon')}")
        print(f"3. {name('Lore')}")
        print(f"4. {danger('Exit Volcano')}")
        print("-" * 40)

        action = input(highlight("Choose an action (1-4 or name): ")).strip().lower()

        # =========================
        # EXPLORE
        # =========================
        if action in ["1", "explore"]:
            slow_print("You move carefully across unstable ground...")
            slow_print(danger("Lava bubbles and bursts nearby."))

            slow_print("You discover deep claw marks carved into stone.")
            slow_print(danger("Whatever made them… is enormous."))

        # =========================
        # CHALLENGE
        # =========================
        elif action in ["2", "challenge", "dragon"]:
            slow_print("The air suddenly goes still...")

            if "Dragon Scale" in hero.inventory:
                slow_print(highlight("A massive shadow descends from above."))
                slow_print("Flames erupt as a Dragon crashes down before you.")
                slow_print(danger("Its eyes burn with fury."))
            else:
                slow_print(danger("A Dragon erupts from the lava, enraged."))
                slow_print("It does not hesitate.")

            slow_print("")
            slow_print(highlight("The Dragon attacks!"))

            enemy = combat.create_enemy("Dragon")
            result = combat.display_enemy(enemy, hero)

            if result == "dead":
                return
            else:
                slow_print("The Dragon retreats into the flames, wounded but not defeated.")

        # =========================
        # LORE
        # =========================
        elif action in ["3", "lore"]:
            show_volcano_lore()

        # =========================
        # EXIT
        # =========================
        elif action in ["4", "exit"]:
            if not hero.flags.get("volcano_outro_seen", False):
                slow_print("You turn away from the burning mountain.")
                slow_print("The heat fades slightly with each step.")
                slow_print(danger("But the roar of Dragons follows you..."))
                hero.flags["volcano_outro_seen"] = True
            break

        else:
            slow_print(danger("Invalid choice. Please select 1–4."))