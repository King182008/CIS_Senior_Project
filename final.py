from utils import slow_print, highlight, danger, lore, npc
import sys


# =========================
# FINAL ENDING
# =========================
def final_ending(hero):

    slow_print(highlight("\n=== JOURNEY COMPLETE ===\n"))

    flags = hero.flags

    # =========================
    # ALL POSSIBLE FLAGS
    # =========================
    required_flags = {

        # Intro Flags
        "mountain_intro_seen": False,
        "desert_intro_seen": False,
        "swamp_intro_seen": False,
        "volcano_intro_seen": False,
        "forest_intro_seen": False,
        "void_intro_seen": False,

        # Interaction Flags
        "swamp_interact_seen": False,
        "desert_interact_seen": False,

        # Bosses / Events
        "rat_king_defeated": False,
        "desert_boss_defeated": False,
        "void_boss_defeated": False,
        "void_beacon_destroyed": False,

        # Special Discoveries
        "ritual_room_found": False,
        "extra_turn": False,
        "void_password_unlocked": False,

        # Outros
        "volcano_outro_seen": False,
        "forest_outro_seen": False
    }

    # =========================
    # PLACES
    # =========================
    required_places = [
        "forest",
        "desert",
        "mountains",
        "swamp",
        "volcano",
        "void"
    ]

    total_flags = len(required_flags) + len(required_places)
    completed_flags = 0

    # =========================
    # COUNT FLAGS
    # =========================
    for flag in required_flags:

        if flags.get(flag, False):
            completed_flags += 1

    # =========================
    # COUNT PLACES
    # =========================
    places = flags.get("placesBeen", {})

    for place in required_places:

        if places.get(place, False):
            completed_flags += 1

    # =========================
    # PERCENTAGE
    # =========================
    completion = int((completed_flags / total_flags) * 100)

    slow_print(
        f"Completion: {highlight(str(completion) + '%')}"
    )

    slow_print(
        f"Progress: {completed_flags}/{total_flags} objectives completed.\n"
    )

    # =========================
    # ENDINGS
    # =========================

    # TRUE ENDING
    if completion >= 100:

        slow_print(highlight("=== TRUE ENDING ==="))

        slow_print(
            lore("You leave nothing unfinished.")
        )

        slow_print(
            lore("Every Horror defeated. Every secret uncovered.")
        )

        slow_print(
            lore("The Void collapses behind you as reality heals.")
        )

        slow_print(
            highlight("You became the legend the world needed.")
        )

    # HERO ENDING
    elif completion >= 90:

        slow_print(highlight("=== HERO ENDING ==="))

        slow_print(
            lore("The world survives because of you.")
        )

        slow_print(
            lore("Most threats were destroyed, though some mysteries remain.")
        )

        slow_print(
            highlight("Your name will be remembered for generations.")
        )

    # GOOD ENDING
    elif completion >= 80:

        slow_print(highlight("=== GOOD ENDING ==="))

        slow_print(
            lore("The greatest evils are gone.")
        )

        slow_print(
            lore("Peace slowly returns to the lands.")
        )

        slow_print(
            highlight("Not every path was explored... but you survived.")
        )

    # BAD ENDING
    elif completion >= 65:

        slow_print(danger("=== BAD ENDING ==="))

        slow_print(
            lore("You escaped the darkness... barely.")
        )

        slow_print(
            lore("Many horrors still wander the world.")
        )

        slow_print(
            danger("The story ends, but the nightmare does not.")
        )

    # WORST ENDING
    else:

        slow_print(danger("=== WORST ENDING ==="))

        slow_print(
            lore("Too much was left unfinished.")
        )

        slow_print(
            lore("The Void spreads silently across the world.")
        )

        slow_print(
            danger("This was not the ending fate intended.")
        )

    slow_print(highlight("\nThank you for playing.\n"))
    slow_print(npc("\nTime is important, go outside, thank your parents, or spend time with your loved ones, one day it'll be too late"))
    sys.exit()