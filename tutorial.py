from utils import slow_print, highlight, danger, lore, name
from forest import ForestIntro

import combat
import shop
import time
import random


# =========================================================
# SETUP
# =========================================================

Henrik = combat.create_enemy("Henrik")


# =========================================================
# UTILITY
# =========================================================

def get_attack_damage(hero):

    damage = hero.strength

    if hasattr(hero, "weapon") and hero.weapon:
        damage += hero.weapon.damage

    return damage


def get_spell_damage(hero):

    return 10 + hero.intelligence


# =========================================================
# COMBAT TUTORIAL
# =========================================================

def tutorial_combat(enemy, hero, slot):

    print(highlight("\n=== COMBAT TUTORIAL ==="))

    # =====================================================
    # ATTACK
    # =====================================================

    slow_print(
        f"{name('Henrik')}: "
        f"\"Start with a basic attack! "
        f"{highlight('(Press 1 or type attack)')}\""
    )

    while enemy.health > 45:

        action = input(
            f"{highlight('Attack')} or {highlight('1')}:\n>> "
        ).strip().lower()

        if action in ["attack", "1"]:

            damage = get_attack_damage(hero)

            slow_print(
                danger(f"\nYou attack Henrik for {damage} damage!")
            )

            enemy.take_damage(damage)

            slow_print(
                lore(f"Henrik's health is now {enemy.health}.")
            )

        else:

            slow_print(
                f"{name('Henrik')}: "
                f"\"Try attacking!\""
            )

    # =====================================================
    # SPELL
    # =====================================================

    slow_print("")
    slow_print(
        f"{name('Henrik')}: "
        f"\"Not bad! But you can do better!\""
    )

    slow_print(
        f"{name('Henrik')}: "
        f"\"Now try using a {highlight('Spell')}!\""
    )

    slow_print(
        "Henrik hands you a glowing red scroll covered in symbols."
    )

    while enemy.health > 40:

        action = input(
            f"{highlight('Spell')} or {highlight('2')}:\n>> "
        ).strip().lower()

        if action in ["spell", "2"]:

            damage = get_spell_damage(hero)

            slow_print(
                highlight(f"You cast Fireball for {damage} damage!")
            )

            enemy.take_damage(damage)

            slow_print(
                lore(f"Henrik's health is now {enemy.health}.")
            )

        else:

            slow_print(
                f"{name('Henrik')}: "
                f"\"Use a spell this time!\""
            )

    # =====================================================
    # FULL COMBAT
    # =====================================================

    slow_print("")
    slow_print(
        f"{name('Henrik')}: "
        f"\"You're getting the hang of it!\""
    )

    slow_print(
        f"{name('Henrik')}: "
        f"\"Now finish the fight!\""
    )

    while enemy.health > 0:

        action = input(
            f"{highlight('(1) Attack')} or "
            f"{highlight('(2) Spell')}:\n>> "
        ).strip().lower()

        if action in ["attack", "1"]:

            damage = get_attack_damage(hero)

            slow_print(
                danger(f"\nYou strike Henrik for {damage} damage!")
            )

            enemy.take_damage(damage)

        elif action in ["spell", "2"]:

            damage = get_spell_damage(hero)

            slow_print(
                highlight(f"You cast Fireball for {damage} damage!")
            )

            enemy.take_damage(damage)

        else:

            slow_print(danger("Invalid action!"))

            continue

        if enemy.health <= 0:
            break

        slow_print(
            lore(f"Henrik's health is now {enemy.health}.")
        )

    slow_print("")
    slow_print(
        f"{name('Henrik')}: "
        f"\"Great job! You're ready for the Ascension tomorrow!\""
    )


# =========================================================
# INTRO
# =========================================================

def intro(hero, slot):

    slow_print(highlight("\n=== PROLOGUE ===\n"))

    slow_print(highlight("Wake up..."))
    slow_print(highlight("Wake up..."))
    slow_print(f"{name(hero.name)}! Wake up!")

    slow_print("Your eyes slowly open.")

    slow_print(
        f"You awaken beneath the massive branches of the "
        f"{highlight('World Tree')}."
    )

    slow_print(
        f"Standing above you is your childhood friend "
        f"{name('Henrik')}."
    )

    slow_print(
        f"He grins while holding "
        f"{highlight('two wooden swords')}."
    )

    slow_print("")

    slow_print(
        f"{name('Henrik')}: "
        f"\"Finally! I thought you'd sleep through the "
        f"{highlight('Ascension')} tomorrow.\""
    )

    slow_print(
        f"{name('Henrik')}: "
        f"\"Come on! Let's train before the ceremony!\""
    )

    slow_print("")

    slow_print(
        "Henrik grabs your arm and drags you toward the training grounds."
    )

    slow_print(
        "Rows of armored soldiers train with brutal precision."
    )

    slow_print(
        f"They are the {highlight('Knights of the Covenant')}."
    )

    slow_print(
        lore("Protectors of the realm.")
    )

    slow_print("")

    slow_print(
        f"{name('Henrik')}: "
        f"\"I know you're nervous about tomorrow...\""
    )

    slow_print(
        f"{name('Henrik')}: "
        f"\"But don't worry. Let's practice the basics.\""
    )

    tutorial_combat(Henrik, hero, slot)

    slow_print("")

    slow_print(
        f"{name('Henrik')}: "
        f"\"Nice work. Let's head home and rest before tomorrow.\""
    )


# =========================================================
# DOOM SEQUENCE
# =========================================================

def doom(hero, slot):

    slow_print("")
    slow_print(lore("..."))

    time.sleep(1)

    slow_print(lore("You drift into a deep sleep."))

    time.sleep(2)

    slow_print(lore("..."))

    time.sleep(2)

    slow_print(danger("BOOOOOOOOOOM!!!"), 0.08)

    slow_print("")
    slow_print(danger("Your eyes snap open."))

    slow_print(
        "The ground trembles beneath you as another explosion shakes the village."
    )

    slow_print(danger("You hear screams outside."))

    slow_print(lore("Panicked. Desperate. Dying."))

    slow_print("")
    slow_print("You rush toward the window.")

    slow_print(danger("Your breath catches in your throat."))

    slow_print("")

    slow_print(
        f"A massive beam of {highlight('blinding light')} erupts from the cathedral."
    )

    slow_print(
        "The clouds twist unnaturally around it."
    )

    slow_print(lore("The air feels wrong."))

    slow_print(lore("Heavy. Suffocating."))

    slow_print("")

    slow_print(danger("Then you see it."))

    slow_print("A shape moving beyond the light.")

    slow_print(danger("Too large."))
    slow_print(danger("Too many limbs."))
    slow_print(danger("It hurts to look at."))

    slow_print("")

    slow_print(
        "A beam of darkness crashes into the center of town."
    )

    slow_print(danger("Buildings collapse instantly."))

    slow_print(
        "The Knights of the Covenant charge the creature."
    )

    slow_print(
        lore("They are nothing compared to it.")
    )

    slow_print("")

    slow_print(
        f"You hear {name('Henrik')} shouting somewhere in the chaos."
    )

    slow_print(danger("The creature begins charging another attack."))

    slow_print("")

    if "silver pendent" in hero.inventory:

        slow_print(
            f"{name('Henrik')} rips the "
            f"{highlight('Silver Pendant')} from your neck."
        )

    else:

        slow_print(
            f"{name('Henrik')} pulls out a "
            f"{highlight('Silver Pendant')}."
        )

    slow_print(
        f"He opens a forbidden {danger('spell book')} and begins chanting."
    )

    slow_print(
        "The pendant glows before unfolding into a tiny seed."
    )

    slow_print(
        lore("The seed grows at an impossible speed.")
    )

    slow_print("")

    slow_print(
        f"A colossal {highlight('golden tree')} erupts from the earth."
    )

    slow_print(danger("The monster fires."))

    slow_print(danger("The beam pierces the tree."))

    slow_print(
        danger("The explosion throws you into a pile of rubble.")
    )

    slow_print("")

    slow_print(
        "Through blurred vision, you see Henrik stumble back toward the tree."
    )

    slow_print(
        "A Covenant ballista crashes into the beast."
    )

    slow_print(
        f"{name('Henrik')} finishes the spell."
    )

    slow_print(
        highlight("A flash of golden light consumes everything.")
    )

    slow_print("")

    slow_print("The creature crashes to the ground.")

    slow_print(lore("The world shakes one final time."))

    slow_print("")

    slow_print(danger("Your vision fades to black."))

    slow_print(lore("..."))

    # =====================================================
    # REMOVE STARTING ITEMS
    # =====================================================

    hero.gold = 0

    if hasattr(hero, "weapon") and hero.weapon:

        slow_print(
            lore(f"Your {hero.weapon.name} is lost beneath the rubble.")
        )

        hero.weapon = None

    if "Wooden Sword" in hero.inventory:
        del hero.inventory["Wooden Sword"]

    # Default to fists if no weapon equipped
    if hero.weapon is None:
        hero.weapon = shop.weapons["fists"]

    hero.save_character(slot)
    ForestIntro(hero)


# =========================================================
# TRAVEL SYSTEM
# =========================================================

def travel(place, hero, slot):

    destinations = {
        "training grounds": ["village", "home"],
        "village": ["training grounds", "home"],
        "home": ["village", "training grounds"]
    }

    print(highlight("\n=== TRAVEL ==="))
    print(f"You are currently at {name(place.title())}")
    print("-" * 40)

    for i, destination in enumerate(destinations[place], 1):
        print(f"{highlight(str(i) + '.')} {name(destination.title())}")

    print("-" * 40)

    decision = input(
        f"Choose destination {highlight('(number or name)')}:\n>> "
    ).strip().lower()

    options = destinations[place]

    if decision.isdigit():

        index = int(decision) - 1

        if index < 0 or index >= len(options):

            slow_print(danger("You can't go there!"))

            return place

        decision = options[index]

    if decision not in options:

        slow_print(danger("You can't go there!"))

        return place

    slow_print(
        highlight(f"\nTraveling to {decision.title()}...\n")
    )

    return decision

# =========================================================
# VILLAGE
# =========================================================

def village(hero, current_place, slot):

    print(highlight("\n=== VILLAGE ==="))
    print("-" * 40)
    print(f"1. {name('Travel')}")
    print(f"2. {highlight('Shop')}")
    print("-" * 40)

    action = input("Choose action:\n>> ").strip().lower()

    if action in ["travel", "1"]:

        return travel(current_place, hero, slot)

    elif action in ["shop", "2"]:

        shop.display_shop(current_place, hero)

        return current_place

    else:

        slow_print(danger("Invalid action!"))

        return current_place


# =========================================================
# HOME
# =========================================================

def home(hero, current_place, slot):

    if "Get Bread" not in hero.quest_log:

        slow_print(
            f"{name('Mother')}: "
            f"\"Could you get some {highlight('Bread')} from the shop?\""
        )

        hero.quest_log["Get Bread"] = "Incomplete"

    elif (
        hero.quest_log["Get Bread"] == "Incomplete"
        and "Bread" in hero.inventory
    ):

        slow_print(
            f"You hand the {highlight('Bread')} to your mother."
        )

        hero.quest_log["Get Bread"] = "Complete"

        del hero.inventory["Bread"]

    if hero.quest_log["Get Bread"] == "Complete":

        print(highlight("\n=== HOME ==="))
        print("-" * 40)
        print(f"1. {name('Travel')}")
        print(f"2. {highlight('Sleep')}")
        print("-" * 40)

        action = input("Choose action:\n>> ").strip().lower()

        if action in ["travel", "1"]:

            return travel(current_place, hero, slot)

        elif action in ["sleep", "2"]:

            doom(hero, slot)

        else:

            slow_print(danger("Invalid action!"))

    else:

        action = input(
            f"{highlight('(1) Travel')}:\n>> "
        ).strip().lower()

        if action in ["travel", "1"]:

            return travel(current_place, hero, slot)

    return current_place


# =========================================================
# TRAINING GROUNDS
# =========================================================

def training_grounds(hero, current_place, slot):

    print(highlight("\n=== TRAINING GROUNDS ==="))
    print("-" * 40)
    print(f"1. {name('Travel')}")
    print(f"2. {danger('Fight Henrik')}")
    print("-" * 40)

    action = input("Choose action:\n>> ").strip().lower()

    if action in ["travel", "1"]:

        return travel(current_place, hero, slot)

    elif action in ["fight", "2", "henrik"]:

        if not hasattr(hero, "fought_henrik_again"):
            hero.fought_henrik_again = False

        if hero.fought_henrik_again:

            slow_print(
                f"{name('Henrik')}: "
                f"\"Save some strength for tomorrow.\""
            )

            return current_place

        enemy = combat.create_enemy("Henrik")

        combat.display_enemy(enemy, hero)

        hero.fought_henrik_again = True

        slow_print(
            f"{name('Henrik')}: "
            f"\"That's enough practice for today!\""
        )

        return current_place

    else:

        slow_print(danger("Invalid action!"))

        return current_place


# =========================================================
# BEGIN TUTORIAL
# =========================================================

def Begin_tutorial(hero, slot):

    current_place = "training grounds"

    locations = {
        "training grounds": training_grounds,
        "village": village,
        "home": home
    }

    intro(hero, slot)

    while True:

        current_place = locations[current_place](hero, current_place, slot)