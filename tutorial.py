import characterCreation
from forest import ForestIntro
import shop
import sys
import combat
import time
from utils import slow_print

Henrik = combat.create_enemy("Henrik")
characterCreation.fought_henrik_again = False


# -----------------------
# Utility
# -----------------------


def get_attack_damage(hero):
    damage = hero.strength
    if hasattr(hero, "weapon") and hero.weapon:
        damage += hero.weapon.damage
    return damage


def get_spell_damage(hero):
    return 10 + hero.intelligence


# -----------------------
# Combat Tutorial
# -----------------------

def tutorial_combat(enemy, hero):

    # Step 1: Attack
    while enemy.health > 45:
        action = input("Do you want to (Attack or 1)?").strip().lower()

        if action in ["attack", "1"]:
            damage = get_attack_damage(hero)
            slow_print(f"\nYou attack Henrik for {damage} damage!")
            enemy.take_damage(damage)
            slow_print(f"Henrik's health is now {enemy.health}.")
        else:
            slow_print("Henrik says, 'Try attacking!'")

    # Step 2: Spell
    slow_print("Henrik says, 'Not bad! But you can do better!'")
    slow_print("Let's try using a spell!")
    slow_print("Henrik hands you a red scroll with a summoning circle.")

    while enemy.health > 40:
        action = input("Do you want to (Spell or 2)? ").strip().lower()

        if action in ["spell", "2"]:
            damage = get_spell_damage(hero)
            slow_print(f"You cast fireball and deal {damage} damage!")
            enemy.take_damage(damage)
            slow_print(f"Henrik's health is now {enemy.health}.")
        else:
            slow_print("Henrik says, 'Use a spell this time!'")

    # Step 3: Full combat
    slow_print("Henrik says, 'You're getting the hang of it! Let's finish this!'")

    while enemy.health > 0:
        action = input("(1) Attack or (2) Spell? ").strip().lower()

        if action in ["attack", "1"]:
            damage = get_attack_damage(hero)
            slow_print(f"\nYou attack Henrik for {damage} damage!")
            enemy.take_damage(damage)

        elif action in ["spell", "2"]:
            damage = get_spell_damage(hero)
            slow_print(f"You cast fireball and deal {damage} damage!")
            enemy.take_damage(damage)

        else:
            slow_print("Invalid action!")
            continue

        if enemy.health <= 0:
            break

        slow_print(f"Henrik's health is now {enemy.health}.")

    slow_print("Henrik says, 'Great job! You're ready for the ascension tomorrow!'")

def doom(hero):
    slow_print("...")
    time.sleep(1)

    slow_print("You drift into a deep sleep.")
    time.sleep(2)

    slow_print("...")
    time.sleep(2)

    slow_print("BOOOOOOOOOOM!!!", 0.08)

    slow_print("Your eyes snap open.")
    slow_print("The ground trembles beneath you as another explosion echoes through the village.")

    slow_print("You hear screams outside.")
    slow_print("Panicked. Desperate.")

    slow_print("You rush to your window...")

    slow_print("Your breath catches in your throat.")

    slow_print("A massive beam of blinding light erupts from the cathedral, piercing straight into the sky.")
    slow_print("The clouds above twist and churn unnaturally around it.")

    slow_print("The air feels... wrong.")
    slow_print("Heavy. Suffocating.")

    slow_print("Then you see it.")

    slow_print("A shape moving beyond the light.")
    slow_print("Too large.")
    slow_print("Too many limbs.")
    slow_print("It doesn't make sense to look at.")

    slow_print("A dark beam flies past you and explodes in the center of town.")

    slow_print("Buildings crumble like paper.")
    slow_print("The Knights of the Covenant clash against it, but they are nothing to a beast like this.")

    slow_print("You hear Henrik shouting somewhere in the chaos.")

    slow_print("You see the creature charging up.")

    if "silver pendent" in hero.inventory:
        slow_print("Henrik runs to you and grabs the pendant from around your neck.")
    else:
        slow_print("Henrik pulls out a silver pendant.")

    slow_print("He pulls out a spell book you've never seen before and starts chanting.")
    slow_print("The pendant glows and opens into a small seed.")
    slow_print("Before you have time to process what's happening, the seed grows at an exorbitant rate.")

    slow_print("The tree takes root, but before the spell is finished, the monster unleashes its hyper beam.")
    slow_print("It pierces the tree, knocks Henrik into you, and throws both of you into a pile of rubble.")

    slow_print("Through blurred vision, you see Henrik get up and stumble back toward the tree.")

    slow_print("The Knights of the Covenant launch a ballista into the beast, stunning it.")

    slow_print("Henrik finishes his spell, and a flash of light erupts from the tree.")

    slow_print("The beast falls to the ground, and with one final quake, your vision goes black.")

    slow_print("...")

    ForestIntro(hero)


# -----------------------
# Travel System
# -----------------------

def travel(place, hero):
    destinations = {
        "training grounds": ["village", "home"],
        "village": ["training grounds", "home"],
        "home": ["village", "training grounds"]
    }

    print("You're currently at the", place.title())
    print("You can travel to:", [d.title() for d in destinations[place]])

    decision = input("Where would you like to go? ").strip().lower()

    if decision not in destinations[place]:
        print("You can't go there!")
        return place

    print("You traveled to the", decision.title())
    return decision


# -----------------------
# Location Handlers
# -----------------------

def village(hero, current_place):
    action = input("Do you want to (Travel(1)) or (Shop(2))? ").strip().lower()

    if action in ["travel", "1"]:
        return travel(current_place, hero)

    elif action in ["shop", "2"]:
        shop.display_shop(current_place, hero)
        return current_place

    else:
        slow_print("Invalid action!")
        return current_place


def home(hero, current_place):

    # Start quest
    if "Get Bread" not in hero.quest_log:
        slow_print("Your mother says, 'Can you go get some bread from the shop?'")
        hero.quest_log["Get Bread"] = "Incomplete"

    # Turn in quest
    elif hero.quest_log["Get Bread"] == "Incomplete" and "Bread" in hero.inventory:
        slow_print("You give the bread to your mother.")
        hero.quest_log["Get Bread"] = "Complete"
        del hero.inventory["Bread"]

    # Already completed
    if hero.quest_log["Get Bread"] == "Complete":
        action = input("Do you want to (Travel(1)) or (Sleep(2))? ").strip().lower()

        if action in ["travel", "1"]:
            return travel(current_place, hero)

        elif action in ["sleep", "2"]:
            slow_print("You go to sleep and prepare for the ascension tomorrow...")
            doom(hero)

        else:
            slow_print("Invalid action!")

    else:
        action = input("Do you want to (Travel(1))? ").strip().lower()

        if action in ["travel", "1"]:
            return travel(current_place, hero)
        else:
            slow_print("Invalid action!")

    return current_place


def training_grounds(hero, current_place):
    action = input("Do you want to (Travel(1)) or (Fight(2))? ").strip().lower()

    if action in ["travel", "1"]:
        return travel(current_place, hero)

    elif action in ["fight", "2"]:
        if not hasattr(hero, "fought_henrik_again"):
            hero.fought_henrik_again = False

        if hero.fought_henrik_again:
            slow_print("Henrik says, 'You've already beaten me twice today... save some strength for tomorrow.'")
            return current_place

        enemy = combat.create_enemy("Henrik")
        combat.display_enemy(enemy, hero)

        hero.fought_henrik_again = True
        slow_print("Henrik says, 'Alright, that's enough practice for today!'")

        return current_place

    else:
        slow_print("Invalid action!")
        return current_place


# -----------------------
# Intro + Main Loop
# -----------------------

def intro(hero):
    slow_print("Wake up!")
    slow_print("Wake up!")
    slow_print(f"{hero.name} wake up!")
    slow_print("Your awoken to the excitment of your childhood friend Henrik jostling you awake.")
    slow_print("You look around and see that you are in a large village in the center of town under a tree.")
    slow_print("You see your friend standing there with a big smile on his face and two wooden swords in his hands.")
    slow_print("He says, 'Hey! Your finally awake! I've been waiting, your dad said we could sword fight before our acension tomorrow!'")
    slow_print("He grabs your arm and drags you to the training grounds where you see a group of soilders known as the Covenant of Universal Light & Truth.")
    slow_print("The Knights of the Covenant are the protectors of the realm and are imbued with magic powers during their acension.")
    slow_print("Henrik says, 'I know your nervous about the acension tomorrow but don't worry, Lets bursh up on the basics.'")

    slow_print("Henrik says, 'Lets start with the basic attack(Press 1 or type attack)'")
    tutorial_combat(Henrik, hero)

    slow_print("Henrik says, 'Now that you know the basics of combat, Let's go home and get some rest for the big day tomorrow!'")


def Begin_tutorial(hero):
    current_place = "training grounds"

    locations = {
        "training grounds": training_grounds,
        "village": village,
        "home": home
    }

    intro(hero)

    while True:
        current_place = locations[current_place](hero, current_place)