from utils import slow_print, danger, lore, highlight
import combat


# =========================
# Shared Lore
# =========================
def show_volcano_lore():
    slow_print(highlight("Lore:"))
    slow_print("Once, Dragons were guardians of balance—keepers of fire and renewal.")
    slow_print(f"After the {danger('Great Blast')}, they were twisted into beings of pure destruction.")
    slow_print(danger("Now they hoard flame, rage, and ruin."))
    slow_print(f"At the heart of the volcano lies their strongest—an {lore('ancient Dragon')}.")
    slow_print(danger("You feel its presence watching you."))


# =========================
# Intro
# =========================
def volcanoIntro(hero):

    if hero.flags.get("volcano_intro_seen", False):
        return

    slow_print("The air grows unbearably hot as you approach the mountain’s peak.")
    slow_print(danger("The ground cracks beneath your feet, glowing with molten light."))

    slow_print("Smoke chokes the sky, turning it a deep crimson.")
    slow_print("")

    slow_print(danger("A distant roar shakes the earth itself."))
    slow_print("Not thunder… something alive.")

    slow_print("")
    slow_print("Rivers of lava carve through the land like veins of fire.")

    slow_print(danger("You feel it immediately—this place is claimed."))

    slow_print(highlight("This is the domain of the Dragons."))

    show_volcano_lore()

    hero.flags["volcano_intro_seen"] = True


# =========================
# Interaction
# =========================
def volcanoInteract(hero, place):
    if not hero.flags.get("volcano_intro_seen", False):
        slow_print("You step onto scorched stone, heat radiating from every direction.")
        slow_print(danger("The ground trembles beneath you, as if something massive moves below."))

        slow_print("")
        slow_print("Charred bones litter the area—remains of creatures that came too close.")
        slow_print(danger("Even the air feels hostile, burning your lungs with every breath."))
        slow_print("")

        show_volcano_lore()
        hero.flags["volcano_intro_seen"] = True

    while True:
        action = input("What would you like to do? (Explore, Challenge, Lore, Exit): ").lower()

        if action == "explore":
            slow_print("You move carefully across unstable ground...")
            slow_print(danger("Lava bubbles nearby, occasionally bursting with violent force."))
            slow_print("You find massive claw marks etched into stone.")
            slow_print(danger("Whatever made them… is enormous."))

        elif action == "challenge":
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

        elif action == "lore":
            show_volcano_lore()

        elif action == "exit":
            slow_print("You retreat from the volcano, the heat slowly fading behind you.")
            break

        else:
            slow_print("That is not a valid action.")