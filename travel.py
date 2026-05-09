import characterCreation
from desert import desertIntro
from swamp import swampIntro
from mountain import mountainIntro
from volcano import volcanoIntro
from void import voidIntro

from utils import highlight, danger, name


INTRO_SCENES = {
    "desert": desertIntro,
    "swamp": swampIntro,
    "mountains": mountainIntro,
    "volcano": volcanoIntro,
    "void": voidIntro
}


# =========================
# TRAVEL
# =========================
def travel(place, hero):

    # =========================
    # CREATE FLAGS IF MISSING
    # =========================
    if "placesBeen" not in hero.flags:
        hero.flags["placesBeen"] = {
            "forest": True,
            "desert": False,
            "mountains": False,
            "swamp": False,
            "volcano": False,
            "void": False
        }

    placesBeen = hero.flags["placesBeen"]

    destinations = {
        "forest": ["desert", "mountains"],
        "desert": ["forest", "swamp"],
        "mountains": ["forest", "volcano"],
        "swamp": ["desert"],
        "volcano": ["mountains"],
        "void": ["forest"]
    }

    # =========================
    # UNLOCK VOID
    # =========================
    required = [
        "Dragon Scale",
        "Locust Wing",
        "Troll Hide",
        "Goblin Tooth",
        "Rat Tail"
    ]

    if all(item in hero.inventory for item in required):
        if "void" not in destinations["forest"]:
            destinations["forest"].append("void")

    print(highlight("\n=== WORLD MAP ==="))
    print(f"Current Location: {name(place.title())}")
    print("-" * 40)

    options = destinations[place]

    # =========================
    # DISPLAY OPTIONS
    # =========================
    for i, dest in enumerate(options, 1):
        print(f"{highlight(str(i) + '.')} {name(dest.title())}")

    print("-" * 40)

    # =========================
    # INPUT
    # =========================
    decision = input(
        f"Choose destination {highlight('(number)')} or {danger('exit')}:\n>> "
    ).strip().lower()

    if decision == "exit":
        return place

    if not decision.isdigit():
        print(danger("Invalid input. Use numbers only."))
        return place

    index = int(decision) - 1

    if index < 0 or index >= len(options):
        print(danger("You can't go there!"))
        return place

    chosen = options[index]

    # =========================
    # VOID PASSWORD
    # =========================
    if chosen == "void":

        # Create flag if missing
        if "void_password_unlocked" not in hero.flags:
            hero.flags["void_password_unlocked"] = False

        # Only ask once
        if not hero.flags["void_password_unlocked"]:

            password = input(
                danger("A voice whispers: 'Speak the password.'\n>> ")
            ).strip().lower()

            if password != "time is the horror":
                print(danger("The Void rejects you."))
                return place

            # Unlock permanently
            hero.flags["void_password_unlocked"] = True

            print(highlight("The Void remembers your name."))

    # =========================
    # REVISIT CHECK
    # =========================
    if placesBeen[chosen]:
        reAsk = input(
            f"You've been to {name(chosen.title())}. Travel anyway? {highlight('(y/n)')}:\n>> "
        ).strip().lower()

        if reAsk not in ["y", "yes"]:
            return place

    print(highlight(f"\nTraveling to {chosen.title()}...\n"))

    # =========================
    # FIRST TIME INTRO
    # =========================
    if not placesBeen[chosen] and chosen in INTRO_SCENES:
        INTRO_SCENES[chosen](hero)

    # =========================
    # SAVE VISIT
    # =========================
    placesBeen[chosen] = True

    return chosen