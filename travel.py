import characterCreation
from desert import desertIntro
from swamp import swampIntro
from mountain import mountainIntro
from volcano import volcanoIntro
from void import voidIntro
placesBeen = {"forest": True,"desert": False,"mountains": False,"swamp": False,"volcano": False, "void": False}

INTRO_SCENES = {
    "desert": desertIntro,
    "swamp": swampIntro,
    "mountains": mountainIntro,
    "volcano": volcanoIntro,
    "void": voidIntro
}


from utils import highlight, danger, name

def travel(place, hero):
    destinations = {
        "forest": ["desert", "mountains"],
        "desert": ["forest", "swamp"],
        "mountains": ["forest", "volcano"],
        "swamp": ["desert"],
        "volcano": ["mountains"],
        "void": ["forest"]
    }

    # Unlock void
    required = ["Dragon Scale", "Locust Wing", "Troll Hide", "Goblin Tooth", "Rat Tail"]
    if all(item in hero.inventory for item in required):
        if "void" not in destinations["forest"]:
            destinations["forest"].append("void")

    print(highlight("\n=== WORLD MAP ==="))
    print(f"Current Location: {name(place.title())}")
    print("-" * 40)

    options = destinations[place]

    # =========================
    # DISPLAY OPTIONS (COLORED + NUMBERED)
    # =========================
    for i, dest in enumerate(options, 1):
        print(f"{highlight(str(i) + '.')} {name(dest.title())}")

    print("-" * 40)

    # =========================
    # FAST INPUT (NUMBER ONLY)
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

    placesBeen[chosen] = True
    return chosen