from utils import slow_print, danger, lore, highlight, name
import combat


# =========================
# Shared Lore
# =========================
def show_void_lore():
    slow_print(highlight("Lore:"))
    slow_print("This is the Void—the birthplace of the Horror.")
    slow_print(lore("Not a place, but the absence of everything."))
    slow_print(lore("Time does not flow here. It fractures."))
    slow_print(danger("The Horror was not born… it leaked into existence."))
    slow_print(danger("And now it spreads, consuming reality piece by piece."))


# =========================
# Intro
# =========================
def voidIntro(hero):

    if hero.flags.get("void_intro_seen", False):
        return

    slow_print("You step beyond the edge of the known world…")
    slow_print(danger("Something is wrong."))

    slow_print("")
    slow_print(lore("The ground shifts like a memory trying to exist."))
    slow_print("Fragments of reality flicker in and out.")

    slow_print(danger("Time stutters. Breaks. Repeats."))

    slow_print("")
    slow_print(highlight("This is not a place."))
    slow_print(danger("This is where reality ends."))

    show_void_lore()

    hero.flags["void_intro_seen"] = True


# =========================
# Interaction
# =========================
def voidInteract(hero, place):
    if not hero.flags.get("void_interact_seen", False):
        hero.flags["void_interact_seen"] = True

    # Ensure boss flag exists
    hero.flags.setdefault("void_boss_defeated", False)

    # First-time entry flavor
    if not hero.flags.get("void_intro_seen", False):
        slow_print(lore("You move… but nothing changes."))
        slow_print(danger("A voice echoes inside you: \"You should not be here.\""))
        show_void_lore()
        hero.flags["void_intro_seen"] = True

    while True:
        print(highlight("\n=== VOID INTERACTION ==="))
        print("-" * 40)
        print(f"1. {name('Observe')}")
        print(f"2. {name('Call Out')}")
        print(f"3. {name('Advance')}")
        print(f"4. {danger('Exit')}")
        print("-" * 40)

        action = input("Choose action (1-4 or name): ").strip().lower()

        # =========================
        # OBSERVE
        # =========================
        if action in ["1", "observe"]:
            slow_print("You focus on your surroundings...")
            slow_print(lore("You see countless versions of yourself."))
            slow_print(danger("They all turn and stare at you."))
            slow_print("Then they vanish.")

        # =========================
        # CALL
        # =========================
        elif action in ["2", "call", "call out"]:
            slow_print("You call into the Void...")
            slow_print(danger("\"...hero...error...zero...\""))
            slow_print(lore("The Void is learning you."))

        # =========================
        # ADVANCE (BOSS)
        # =========================
        elif action in ["3", "advance"]:
            from voidDungeon import enter_void_dungeon
            result = enter_void_dungeon(hero, place)

        # =========================
        # RESULT HANDLING (FIXED)
        # =========================

            if result == "dead":
                return  # player died → exit immediately

            elif result in ["run", "escape", "flee", None]:
                slow_print(danger("You escape... but the Horror remains."))
                continue  # back to menu, no victory

            elif result == "win":
                hero.flags["void_boss_defeated"] = True
                from final import final_ending

                # Victory sequence
                slow_print("")
                slow_print(highlight("=== VICTORY ==="))

                slow_print(lore("The Void convulses violently."))
                slow_print(danger("The Horror collapses inward."))

                slow_print("")
                slow_print(lore("The time bubble shatters."))

                slow_print("Henrik falls to the ground, gasping.")
                slow_print(f"{name('Henrik')}: \"I thought... I was gone...\"")

                slow_print("")
                slow_print(f"{name('Henrik')} looks at you, shaken.")
                slow_print(f"{name('Henrik')}: \"That thing... it's not truly dead.\"")

                slow_print("")
                slow_print(danger("The Void still watches."))
                final_ending(hero)


            else:
                # fallback safety (in case combat returns something unexpected)
                slow_print(danger("The outcome is unclear... the Horror still exists."))
                continue
        # =========================
        # EXIT
        # =========================
        elif action in ["4", "exit"]:
            slow_print("You step away from the Void.")
            slow_print(lore("Reality slowly stabilizes around you."))
            if not hero.flags.get("void_outro_seen", False):
                hero.flags["void_outro_seen"] = True
            break

        else:
            slow_print(danger("Invalid action."))