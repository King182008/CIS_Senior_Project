import characterCreation
from desert import desertIntro
from swamp import swampIntro
from mountain import mountainIntro
from volcano import volcanoIntro
from void import voidIntro
currentPlace = "forest"
placesBeen = {"forest": True,"desert": False,"mountains": False,"swamp": False,"volcano": False, "void": False}

INTRO_SCENES = {
    "desert": desertIntro,
    "swamp": swampIntro,
    "mountains": mountainIntro,
    "volcano": volcanoIntro,
    "void": voidIntro
}


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

    print("You're currently at the", place.title())
    print("You can travel to locations", [d.title() for d in destinations[place]])

    decision = input("Where would you like to go? ").strip().lower()

    if decision not in destinations[place]:
        print("You can't go there!")
        return place

    # Already visited
    if placesBeen[decision]:
        reAsk = input("You've been here, go anyway? (yes/no) ").strip().lower()
        if reAsk in ["yes", "y"]:
            print(f"You traveled to the {decision.title()}")
            return decision
        else:
            return place

    # FIRST TIME VISIT
    print(f"You travel to the {decision.title()}...")

    if decision in INTRO_SCENES:
        INTRO_SCENES[decision](hero)

    placesBeen[decision] = True
    return decision