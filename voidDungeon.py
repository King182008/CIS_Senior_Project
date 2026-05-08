from utils import slow_print, danger, highlight, name, lore
import combat
import random


# =========================================================
# ENTRY
# =========================================================
def enter_void_dungeon(hero, place):

    place = "void_dungeon"

    slow_print(highlight("\n=== VOID DUNGEON ==="))
    slow_print("You step beyond reality.")
    slow_print(danger("The Void stares back."))

    hero.flags["in_void_dungeon"] = True

    return void_loop(hero, place)


# =========================================================
# MAIN LOOP
# =========================================================
def void_loop(hero, place):

    while hero.flags.get("in_void_dungeon", False):

        if hero.health <= 0:
            return "dead"

        print(highlight("\n=== VOID ACTIONS ==="))
        print("-" * 45)

        print(f"1. {name('Move Forward')}")
        print(f"2. {name('Observe Surroundings')}")
        print(f"3. {name('Challenge the Horror')}")
        print(f"4. {name('Inventory')}")
        print(f"5. {danger('Attempt Escape')}")

        print("-" * 45)

        action = input(highlight("Choose: ")).strip().lower()

        # =====================================================
        # MOVE
        # =====================================================
        if action in ["1", "move", "forward"]:

            result = explore_void(hero, place)

            if result == "dead":
                return "dead"

        # =====================================================
        # OBSERVE
        # =====================================================
        elif action in ["2", "observe", "inspect"]:

            observe_void(hero)

        # =====================================================
        # FINAL BOSS
        # =====================================================
        elif action in ["3", "challenge", "horror", "cthulu"]:

            result = cthulu_encounter(hero)

            if result == "win":
                return "win"

            elif result == "dead":
                return "dead"

        # =====================================================
        # INVENTORY
        # =====================================================
        elif action in ["4", "inventory"]:

            inventory(hero)

        # =====================================================
        # ESCAPE
        # =====================================================
        elif action in ["5", "escape"]:

            return attempt_escape(hero)

        else:
            slow_print(danger("Invalid choice."))


# =========================================================
# EXPLORE
# =========================================================
def explore_void(hero, place):

    slow_print("You drift deeper into the Void...")

    roll = random.randint(1, 100)

    if roll <= 20:
        return void_enemy(hero, place)

    elif roll <= 35:
        whisper_event(hero)

    elif roll <= 50:
        void_distortion(hero)

    elif roll <= 65:
        memory_event(hero)

    elif roll <= 78:
        return void_miniboss(hero)

    elif roll <= 86:
        mirror_event(hero)

    elif roll <= 93:
        cosmic_event(hero)

    elif roll <= 97:
        void_merchant(hero)

    else:
        abyss_event(hero)


# =========================================================
# VOID ENEMY
# =========================================================
def void_enemy(hero, place):
    from combat import display_enemy, create_enemy

    enemy_name = "Horror Spawn"
    enemy = create_enemy(enemy_name)

    slow_print(danger(f"A {enemy.name} crawls from the darkness."))

    return display_enemy(enemy, hero)

# =========================================================
# WHISPERS
# =========================================================
def whisper_event(hero):

    whispers = [

        "You hear your name whispered behind you.",

        "Something breathes beside your ear.",

        "A voice says, 'You should not be here.'",

        "You hear Henrik screaming in the distance.",

        "The Void whispers secrets you cannot understand."
    ]

    slow_print(danger(random.choice(whispers)))

    if random.random() < 0.3:

        hero.mana += 10

        slow_print(highlight("+10 Mana"))


# =========================================================
# DISTORTION
# =========================================================
def void_distortion(hero):

    slow_print(danger("Reality twists around you."))

    effect = random.choice([

        "damage",

        "heal",

        "mana",

        "nothing"
    ])

    if effect == "damage":

        dmg = random.randint(10, 20)

        hero.health -= dmg

        slow_print(danger(f"You suffer {dmg} damage."))

    elif effect == "heal":

        heal = random.randint(10, 20)

        hero.health += heal

        slow_print(highlight(f"You recover {heal} HP."))

    elif effect == "mana":

        mana = random.randint(15, 30)

        hero.mana += mana

        slow_print(highlight(f"+{mana} Mana"))

    else:

        slow_print("The distortion fades harmlessly.")


# =========================================================
# MEMORY
# =========================================================
def memory_event(hero):

    slow_print(highlight("A memory appears before you..."))

    memories = [

        "You see your village before the Great Blast.",

        "You see Henrik training beside you.",

        "You hear laughter from a life long gone.",

        "You watch the Heartroot glowing in the distance.",

        "You see the Horror watching you from the sky."
    ]

    slow_print(random.choice(memories))

    if random.random() < 0.4:

        hero.intelligence += 1

        slow_print(highlight("+1 Intelligence"))


# =========================================================
# MIRROR EVENT
# =========================================================
def mirror_event(hero):

    slow_print(highlight("\nA mirror forms in the darkness."))

    slow_print(lore("Inside it... you see yourself."))

    slow_print(danger("But something is wrong."))

    result = random.choice([

        "power",

        "fear",

        "knowledge",

        "nothing"
    ])

    if result == "power":

        hero.strength += 1

        slow_print(highlight("+1 Strength"))

    elif result == "fear":

        dmg = random.randint(10, 20)

        hero.health -= dmg

        slow_print(danger(f"-{dmg} HP"))

    elif result == "knowledge":

        hero.intelligence += 1

        slow_print(highlight("+1 Intelligence"))

    else:

        slow_print("The mirror shatters.")


# =========================================================
# COSMIC EVENT
# =========================================================
def cosmic_event(hero):

    slow_print(highlight("\nThe stars begin moving."))

    slow_print(danger("Constellations rearrange into an eye."))

    result = random.choice([

        "mana",

        "madness",

        "blessing"
    ])

    if result == "mana":

        gain = random.randint(25, 50)

        hero.mana += gain

        slow_print(highlight(f"+{gain} Mana"))

    elif result == "madness":

        loss = random.randint(15, 30)

        hero.health -= loss

        slow_print(danger(f"-{loss} HP"))

    else:

        hero.flags["void_blessing"] = True

        slow_print(highlight("The cosmos acknowledges you."))


# =========================================================
# VOID MERCHANT
# =========================================================
def void_merchant(hero):

    slow_print(highlight("\nA hooded merchant emerges from the dark."))

    slow_print(lore("\"Everything has a price.\""))

    print("\n1. Void Potion (25 gold)")
    print("2. Forbidden Knowledge (50 gold)")
    print("3. Leave")

    choice = input("\nChoose: ").strip().lower()

    if choice == "1":

        if hero.gold >= 25:

            hero.gold -= 25

            hero.health += 40

            slow_print(highlight("+40 HP"))

        else:

            slow_print(danger("Not enough gold."))

    elif choice == "2":

        if hero.gold >= 50:

            hero.gold -= 50

            hero.intelligence += 2

            slow_print(highlight("+2 Intelligence"))

        else:

            slow_print(danger("Not enough gold."))

    else:

        slow_print("The merchant disappears.")


# =========================================================
# ABYSS EVENT
# =========================================================
def abyss_event(hero):

    slow_print(danger("The Void notices you."))

    if random.random() < 0.5:

        hero.health -= 25

        slow_print(danger("-25 HP"))

    else:

        hero.mana += 50

        slow_print(highlight("+50 Mana"))


# =========================================================
# MINI BOSS
# =========================================================
def void_miniboss(hero):

    if hero.flags.get("void_beacon_destroyed"):

        slow_print("The shattered beacon drifts silently.")

        return

    slow_print(danger("\nTHE VOID BEACON AWAKENS."))

    enemy = combat.create_enemy("Void Beacon")

    result = combat.display_enemy(enemy, hero)

    if result == "win":

        hero.flags["void_beacon_destroyed"] = True

        slow_print(highlight("The Beacon collapses."))

    return result


# =========================================================
# FINAL BOSS
# =========================================================
def cthulu_encounter(hero):

    if not hero.flags.get("void_beacon_destroyed"):

        slow_print(danger("A force blocks your path."))

        return

    if hero.flags.get("void_boss_defeated"):

        slow_print("The Horror's corpse drifts endlessly.")

        return

    slow_print(danger("\nTHE HORROR DESCENDS."))

    enemy = combat.create_enemy("Horror")

    result = combat.display_enemy(enemy, hero)

    if result == "win":

        hero.flags["void_boss_defeated"] = True
        hero.flags["in_void_dungeon"] = False

        slow_print(highlight("\n=== VICTORY ==="))

        slow_print(lore("The Void convulses violently."))

        slow_print(danger("The Horror collapses inward."))

    return result


# =========================================================
# OBSERVE
# =========================================================
def observe_void(hero):

    observations = [

        "The ground shifts like liquid shadow.",

        "You see distant stars blinking out.",

        "Something massive moves far away.",

        "You feel eyes watching you.",

        "Reality flickers around you."
    ]

    slow_print(random.choice(observations))


# =========================================================
# INVENTORY
# =========================================================
def inventory(hero):
    from inventory import show_inventory
    show_inventory(hero)


# =========================================================
# ESCAPE
# =========================================================
def attempt_escape(hero):

    slow_print("You attempt to escape the Void...")

    if random.random() < 0.35:

        hero.flags["in_void_dungeon"] = False

        slow_print(highlight("Reality bends. You escape."))

        return "escape"

    else:

        slow_print(danger("The Void refuses to release you."))

        return None